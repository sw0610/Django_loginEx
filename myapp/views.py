from django.shortcuts import render
from .models import Blog

# Create your views here.
def create(request):
    blog = Blog()
    blog.titlek = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return    

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})