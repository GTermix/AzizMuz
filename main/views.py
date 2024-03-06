import json
from datetime import datetime,timedelta
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.views.decorators.cache import cache_page
from pytube import YouTube
from .models import *
from django.http import FileResponse
from .forms import *

'''from pytube import YouTube

yt = YouTube('[VIDEO_URL]')
duration = yt.length
'''


class Index(View):
    email_field = SubscribeNews

    def get(self, req):
        o = VisitorCounter.objects.create()
        print(o.id,o.date,o.time)
        try:
            latest_music = Video.objects.latest('id')
        except:
            latest_music = None
        try:
            musics = list(enumerate(Music.objects.order_by('-id')[:5], start=1))
        except:
            musics = None
        try:
            videos_list = Video.objects.order_by('-id')[1:4]
        except:
            videos_list = []
        return_context = {"latest_music": latest_music, "emailfield": self.email_field, "musics": musics,
                          "videos": videos_list}
        return render(req, 'main/index.html',context=return_context)


class About(View):
    email_field = SubscribeNews
    def get(self, req):
        return render(req, 'main/about.html',context={"emailfield": self.email_field})


class ContactView(View):
    contact = ContactForm
    email_field = SubscribeNews
    def get(self, req):
        return render(req, 'main/contact.html', context={"contact":self.contact,"emailfield": self.email_field})

    def post(self, req):
        phone_numbers = Contact.objects.values_list('phone_number', flat=True)
        form = ContactForm(req.POST)
        pn=''
        response_json = json.dumps({'message': 'Ma\'lumotlarda xatolik mavjud '\
            'sahifani yangilab qayta urinib ko\'ring'})
        status_code=200
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            for i in phone_number:
                    if i in ['0','1','2','3','4','5','6','7','8','9']:
                        pn+=i
            pn=pn[-9:]
            two_days_ago = datetime.now() - timedelta(days=2)
            count = Contact.objects.filter(phone_number=pn,date__gte=two_days_ago).count()
            if not pn in phone_numbers or count<2:
                instance = form.save(commit=False)
                instance.phone_number=pn
                instance.save()
                response_json = json.dumps({"message":"Xabar muvoffaqiyatli yuborildi"})
            else:
                filtered_contacts = Contact.objects.filter(phone_number=pn, date__gt=two_days_ago).order_by('-date')[:2]
                bl=True
                days_passed=[]
                for i in filtered_contacts:
                    current_date = datetime.now()
                    target_datetime = datetime.combine(i.date, datetime.min.time())
                    time_diff = (current_date - target_datetime).days
                    days_passed.append(time_diff)
                    bl *= time_diff>=2
                if not bl:
                    response_json = json.dumps({'message': f"Siz bilan bog'lanishadi, yoki {2-min(days_passed)}"\
                    f" kundan keyin qayta xabar jo'natishingiz mumkin"})
                else:
                    instance = form.save(commit=False)
                    instance.phone_number=pn
                    instance.save()
                    response_json = json.dumps({"message":"Xabar muvoffaqiyatli yuborildi"})
        return HttpResponse(response_json, content_type='application/json', status=status_code)



class MusicsView(View):
    email_field = SubscribeNews
    def get(self, req):
        try:
            musics = list(enumerate(Music.objects.order_by('-id'), start=1))
        except:
            musics = None
        return render(req, 'main/musics.html', {'musics': musics,"emailfield": self.email_field})


class VideosView(View):
    email_field = SubscribeNews
    def get(self, req):
        try:
            latest_video = Video.objects.order_by('-id')[0]
            # latest_video.link = latest_video.link.split('=')[1]
            videos_list = Video.objects.order_by('-id')[1:]
        except:
            latest_video = None
            videos_list = []
        return render(req, 'main/videos.html', {"latest": latest_video, 'list': videos_list,"emailfield": self.email_field})


class AlbumView(View):
    email_field = SubscribeNews
    def get(self, req):
        album = Image.objects.order_by('-id')[:10]
        resp = render(req, 'main/album.html', {"album": album,"emailfield": self.email_field})
        return resp


class PostBlogView(View):
    email_field = SubscribeNews
    def get(self,req):
        posts = Post.objects.order_by('-id')[:10]
        return render(req,"main/blog.html",{'post':posts,"emailfield": self.email_field})


class BlogDetailView(View):
    def get(self,req,pk):
        post = Post.objects.get(id=pk)
        post.increase_views
        return render(req,'main/full_blog.html',{"post":post})


def get_picture_links(request,number):
    try:
        number=int(number)
        all_data = Image.objects.order_by('-id').values('image', 'title', 'date')[10:]
        paginator = Paginator(all_data, 10)  # Split the data into pages with 20 objects per page

        page_number = number
        page = paginator.get_page(page_number)
        formatted_data = []
        if paginator.num_pages >= number:
            for item in page:
                date_object = item['date']
                formatted_date = date_object.strftime('%b. %d, %Y')
                formatted_item = {
                    'image': item['image'],
                    'title': item['title'],
                    'date': formatted_date
                }
                formatted_data.append(formatted_item)
    except:
        formatted_data = []
    return JsonResponse(formatted_data, safe=False)

def get_picture_links_count(request):
    try:
        all_data = Image.objects.order_by('-id').values('image', 'title', 'date')[10:]
        paginator = Paginator(all_data, 10)
        formatted_data = {"p":paginator.num_pages}
    except:
        formatted_data=[]
    return JsonResponse(formatted_data, safe=False)

def music_download(request, music_name):
    music = get_object_or_404(Music, music="musics/" + music_name)
    music_path = music.music.path
    return FileResponse(open(music_path, 'rb'), as_attachment=False)

def image_download(request, image_name):
    s=image_name.split("_")[0][-1]=="c"
    if not s:
        image = get_object_or_404(Image, image="images/" + image_name)
        image_path = image.image.path
    else:
        image = get_object_or_404(Image, compressed_image="images/" + image_name)
        image_path = image.compressed_image.path
    return FileResponse(open(image_path, 'rb'),as_attachment=False)

def image_download_blog(request, image_name):
    image = get_object_or_404(ImageForBlog, image="images/" + image_name)
    image_path = image.image.path
    return FileResponse(open(image_path, 'rb'),as_attachment=False)

def subscribe_email(req):
    if req.method == 'POST':
        form = SubscribeNews(req.POST)
        resp=json.dumps({"message":"Xatolik! Sahifani yangilab qayta urinib ko'ring"})
        if form.is_valid():
            try:
                element = SubscribeEmail.objects.get(email=form.cleaned_data['email'])
                if element:
                    resp=json.dumps({"message":"Siz allaqachon yangiliklarga a'zo bo'lgansiz"})
            except SubscribeEmail.DoesNotExist:
                resp=json.dumps({"message":"Yangiliklarga muvoffaqiyatli a'zo bo'lindi!"})
                form.save()            
        return HttpResponse(resp,content_type='application/json',status=200)
    return JsonResponse({'message': 'Unsupported method'}, status=405)