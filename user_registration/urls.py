from django.urls import path
from . import views

app_name = 'user_r'

urlpatterns = [
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('profil/<str:username>/', views.see_profil, name='profil'),
    path('subscription_to/<str:subscriber>/<str:subscribed_to>/', views.subscription_to, name='subscription_to'),
  #  path('test/', views.subscriber_page,name='test')
    
]
