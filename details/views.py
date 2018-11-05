from django.shortcuts import render
from django.templatetags.static import static
import json
# Create your views here.

db_file_path = static('database/out_DB.json')[1:]
db_file = open(db_file_path)
json_data = json.load(db_file)


def details(request, phone_id):
    phone_details = json_data[phone_id]
    # edit keys in the phone details, create new list to be passed as phone details
    return render(request, 'details/details.html', {'phone_id': phone_id, 'phone_details': phone_details})
