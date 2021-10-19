from django.urls import path
from .views import *

urlpatterns = [
    path ("",blog_view),
    path("hello-world", date_view),
    path("random", random_view),
    path("file", test_form),
    path("create", create_blog),
    path("extra-info",dop_information),
    # path("click_photo_2",show_photo),

]