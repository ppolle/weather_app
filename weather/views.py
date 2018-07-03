from django.shortcuts import render,redirect
from django.conf import settings
from .forms import SignUpForm
from django.contrib import messages
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

def signup(request):
	'''
	View to create a user instance
	'''
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.save()

			user.refresh_from_db()
			user.profile.phone_number = form.cleaned_data.get('phone_number')
			
			user.save()

			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = user.username,password = raw_password)
			user_login(request,user)
			messages.success(request, 'Success! You have succesfullly created a new sacco!')
			return redirect('index')
		# else:
		# 	messages.error(request,f'Error having the form as valid')
		# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		form = SignUpForm()
	return render(request,'weather/authenticate/signup.html',{"form":form})

