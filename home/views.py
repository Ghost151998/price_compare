from django.shortcuts import render
from django.templatetags.static import static
import json

# Create your views here.

db_file_path = static('database/out_DB.json')[1:]
db_file = open(db_file_path)
json_data = json.load(db_file)


def home(request):
    return render(request, 'home/home.html', {'data': json_data})


def home_lucky(request):
    return render(request, 'home/home-lucky.html', {'data': json_data})
