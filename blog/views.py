import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView

from blog.forms import BlogForms
from blog.models import Blog


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


class CreateBlogView(CreateView):
    model = Blog
    template_name = "hm_blog_creation.html"
    fields = [
        "image",
        "title",
        "description",
    ]

def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'view of the blogs.html', context={"blogs": blogs})


def dop_information(request):
    return render(request, 'dop-information about blog.html')


def test_form(request):
    if request.method == "POST":
        data = request.POST
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"your name {first_name} your surname {last_name}")
    elif request.method == "GET":
        return render(request, 'file.html')


class DetailBogView(DetailView):
    template_name = 'detail-blog.html'
    queryset = Blog.objects.filter()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def change_blog_view(request, pk):

    blog = Blog.objects.filter(id=pk).first()
    forms = BlogForms
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        if data.get("title"):
            blog.title = data["title"]
        if data.get("description"):
            blog.description = data["description"]
        if file.get("image"):
            blog.image = file["image"]
        blog.save()
        return redirect(f"/blog/{blog.id}/")
    elif request.method == "GET":
        context = {"blog": blog, 'form': forms}
        return render(request, "blog-update.html", context)
