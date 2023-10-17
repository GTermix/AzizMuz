import requests
from django.test import TestCase

# Create your tests here.
v = 'https://drive.google.com/file/d/1ArQLnKvYr4TSM2Py7Mhg4yraY_d4W5aH/edit'
r = requests.get(v)
print(r.text)