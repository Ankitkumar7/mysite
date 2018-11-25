from django import forms
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)
#Self defined models fields importing from models.py model-"post"
from .models import post
#saving user model  into User variable
User = get_user_model(
	)
#Class for login form extending forms class
class UserLoginForm(forms.Form):
	#models fields
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	#defining clean function for validation 
	def clean(self, *args, **kargs):
			username = self.cleaned_data.get("username")
			password  = self.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			#if username and password contain something or is True then make authentication
			if username and password:
				user = authenticate(username=username, password=password)
				#if user is not valid , execute this line
				if not user:
					raise forms.ValidationError("This user does not exit")
					#if user provide wrong password, execute this line
				if not user.check_password(password):
					raise forms.ValidationError("Incorrect password")
					#if user is logout, execute this line
				if not user.is_active:
					raise forms.ValidationError("This user is no longer active.")
			return super(UserLoginForm, self).clean(*args, **kargs)

#class for registration 
class UserRegisterForm(forms.ModelForm):
	#model fields, email2 is used to compare email id if its matched then proceed
	email = forms.EmailField(label="Confirm Email")
	email2 = forms.EmailField(label="Email Address")
	password = forms.CharField(widget=forms.PasswordInput)
	#In this class, fields are default getting from django admin model fields
	class Meta:
		model = User
		fields =[
				'username',
				'email2',
				'email',
				'password'
		]
		#defining clean function for validation 
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		#simple validation if emailid is not same, execute this function
		if email != email2:
			raise forms.ValidationError("Email must match")
		email_qs = User.objects.filter(email=email)
		#if email already register, execute this line
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registerd")
		return email

class postForm(forms.ModelForm):
	class Meta:
		model = post
		fields = [

			"name",
			"content",

		]

#End of code