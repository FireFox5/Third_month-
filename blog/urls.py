from django.urls import path
from .views import *

urlpatterns = [
    path("", blog_view, name='blogs'),
    path("hello-world/", date_view),
    path("random/", random_view),
    path("file/", test_form),
    path("create/", CreateBlogView.as_view(), name='create'),
    path("extra-info/", dop_information),
    path('<int:pk>/', DetailBogView.as_view(), name='detail'),
    path('change/<int:pk>/', change_blog_view, name='change')
    # path("click_photo_2",show_photo),
]
