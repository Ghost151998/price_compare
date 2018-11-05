from django.conf.urls import url
from . import views

app_name = 'details'

urlpatterns = [
    url(r'(?P<phone_id>.*)/$', views.details, name="details"),
]
