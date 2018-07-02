from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.
def index(request):
	'''
	View function to render the index page
	'''
	endpoint = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={weather_api}'
	city = 'Las Vegas'
	weather_api = settings.WEATHER_API
	url = endpoint.format(city = city,weather_api = weather_api)

	response = requests.get(url).json()

	city_weather = {
	'city':city,
	'temp':response['main']['temp'],
	'description':response['weather'][0]['description'],
	'icon':response['weather'][0]['icon'],
	}

	return render(request,'index/index.html',{"city_weather":city_weather})