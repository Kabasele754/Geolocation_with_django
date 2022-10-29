from django.shortcuts import render
import requests
import json
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name= "geo/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/24.48.0.1')#+ip_data['ip']
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        context['data'] = location_data
        return context
