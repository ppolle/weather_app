from django.shortcuts import render,redirect
from django.conf import settings
import requests
import nexmo

client = nexmo.Client(key=settings.NEXMO_KEY, secret=settings.NEXMO_SECRET)

# Create your views here.
def index(request):
	'''
	View function to render the index page
	'''
	if request.GET.get("city"):
		endpoint = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={weather_api}'
		city =request.GET.get("city")
		weather_api = settings.WEATHER_API
		url = endpoint.format(city = city,weather_api = weather_api)

		response = requests.get(url).json()

		city_weather = {
		'city':city,
		'temp':response['main']['temp'],
		'description':response['weather'][0]['description'],
		'icon':response['weather'][0]['icon'],
		}
		return render(request,'weather/index.html',{"city_weather":city_weather})
	else:
		endpoint = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={weather_api}'
		city ='Nairobi'
		weather_api = settings.WEATHER_API
		url = endpoint.format(city = city,weather_api = weather_api)

		response = requests.get(url).json()

		city_weather = {
		'city':city,
		'temp':response['main']['temp'],
		'description':response['weather'][0]['description'],
		'icon':response['weather'][0]['icon'],
		}
		return render(request,'weather/index.html',{"city_weather":city_weather})
