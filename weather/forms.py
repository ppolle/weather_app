from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	'''
	Model form class to create a sign up form
	'''
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	phone_number = forms.IntegerField()
	
	
	class Meta:
		model = User
		fields = ('username', 'email','phone_number','password1', 'password2',)

	def __init__(self,*args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['phone_number'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'

