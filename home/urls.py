from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'lucky/', views.home_lucky, name="home_lucky"),
    url(r'^$', views.home, name="home"),
]

