from django.urls import path
from .views import *

urlpatterns = [
    path("hello-world", date_view),
    path("random", random_view),
    path("file/", test_form),
    path("hm_blog", create_blog),
    path("click_photo_2",show_photo),

]