from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),  # гл страница
    path('group/<slug:slug>/', views.group_posts, name='group_list'),  # группа
    path('profile/<str:username>/', views.profile, name='profile'),  # стр.пользователя
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # стр. записи(id)
    path('create/', views.post_create, name='post_create'),  # создание поста
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # редактирование поста
]
