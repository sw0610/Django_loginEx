from django.shortcuts import render

# Create your views here.
def create(request):
    blog = Blog()
    blog.titlek = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return
