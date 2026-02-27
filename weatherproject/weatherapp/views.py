from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'        

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5cf7d7e1d373b26b22af7fd539c5f734'
    PARAMS = {'units':'metric'} 
    API_KEY = ''
    SEARCH_ENGINE_ID = 'c607985d4a4af416e'

    try:
        data = requests.get(url, PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'index.html', {'description':description, 'icon': icon, 'temp': temp, 'day': day, 'city':city, 'exception_occurred':False}, )
    except:
        exception_occurred = True
        messages.error(request, 'entered data is not available to API')
        date=datetime.date.today()

        return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred } )
           