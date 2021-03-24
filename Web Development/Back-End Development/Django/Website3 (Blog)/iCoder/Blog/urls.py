from django.urls import path, include
from . import views

urlpatterns = [
    path('PostComment', views.postComment, name="postComment"),
    path('', views.bloghome, name="BlogHome"),
    path('<str:slug>', views.blogpost, name="Blogpost"),
]