from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-create-list'),
    path('comments/', views.CommentList.as_view(), name='comment-create-list'),
    path('<pk>/', views.PostDetail.as_view(), name='blog-r-u-d'),
]
