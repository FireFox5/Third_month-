import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


def create_blog(request):
    if request.POST:
        data= request.POST
        files = request.FILES
        title = data["title"]
        descripction = data["description"]
        image = files["image"]
        blog = Blog.objects.create(title=title, description=descripction, image=image)
        # context = {"image": request.FILES.get('image'), 'title': title, 'description':descripction}
        return HttpResponse("блог успешно добавлен ")
    elif request.method == "GET":
        return render(request, 'hm_blog_creation.html')
def blog_view(request):
    blogs = Blog.objects.all()
    return render(request,'view of the blogs.html',context={"blogs":blogs})
def dop_information(request):
    return render(request,'dop-information about blog.html')

def test_form(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"your name {first_name} your surname {last_name}")
    elif request.method == "GET":
        return render(request, 'file.html')


