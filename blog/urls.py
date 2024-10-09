from django.urls import path
from .views import index, about, add_post, post_list, post_detail, post_edit, post_delete


app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/add/', add_post, name='add_post'),
    path('post/', post_list, name='post_list'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),

]