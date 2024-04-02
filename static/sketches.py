class SendVideoData(View):
    def  get(self,request,code):
        obj = Video.objects.get(code=code)
        videos_list = Video.objects.order_by('-id')[1:]
        paginator = Paginator(videos_list, 6)  # 6 videos per page

        # Calculate the page number containing the obj
        index = list(videos_list).index(obj) + 1  # Adding 1 to convert from 0-based index to 1-based position
        page_number = (index + 5) // 6  # Calculate the page number

        print(index,page_number)

        page_obj = paginator.get_page(page_number)
        data_=[]
        for i in page_obj:
            data_.append(i.link)
        return JsonResponse({"links":data_,"index":index%6,"page":page_number},status=200)


