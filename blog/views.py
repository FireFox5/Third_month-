import datetime
import random

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


def create_blog(request):
    if request.method == "POST":
        data = request.POST

        title = data["title"]
        descripction = data["description"]

        context = {"image": request.FILES.get('image'), 'title': title, 'description':descripction}
        return render(request, "click_photo.html", context)
    elif request.method == "GET":
        return render(request, 'hm_blog.html')


def test_form(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"your name {first_name} your surname {last_name}")
    elif request.method == "GET":
        return render(request, 'file.html')


def show_photo(request):
    if request.method == "GET":

        return render(request, "click_photo_2.html",)
