from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'addpg/', views.AddPG, name='AddPG'),
    url(r'home/', views.home, name='home'),

]
