from django.urls import path
from . import views

app_name= 'post'

urlpatterns = [
    path('self_posts', views.see_self_post,name='self_posts'),
    path('create_post', views.create_post ,name='create_post'),
    path('all_posts', views.see_all_post, name='all_posts'),
    
]
