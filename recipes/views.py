#importing Modules
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

from .models import recipes, post, testerStatus, uatStatus
User = get_user_model()
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, postForm
from django.http import HttpResponse


#Here is our views for main page, recipe page,  login, register and logout
def recipesmain(request, request_id):
	get_recipes = recipes.objects.filter(id=request_id)
	context = {
		'get_recipes':get_recipes,

	}
	return render(request, 'reciepes.html', context)



#This function is used to get the recipes name and display in index.html 
def index(request):
	get_objects = recipes.objects.all()
	update_status = testerStatus.objects.filter(user = request.user, status='on-going {0}'.format(request.user))
	uat_update_status = uatStatus.objects.filter(user=request.user, status='on-going {0}'.format(request.user))
	getUatLiveTestingProfile = uatStatus.objects.all()
	getDevLiveTestingProfile = testerStatus.objects.all()
	totalTestingQuery = testerStatus.objects.all()
	totalUatTestingQuery = uatStatus.objects.all()
	if totalTestingQuery:
		totalTestingOnGoing = len(totalTestingQuery)
	else:
		totalTestingOnGoing = 0
	if totalUatTestingQuery:
		uatLenOnGoing = len(totalUatTestingQuery)
	else:
		uatLenOnGoing = 0
	context = {
			'get_objects':get_objects,
			'checkbox_status': update_status,
			'ttOnGoing': totalTestingOnGoing,
			'checkUat': uat_update_status,
			'totaluat': uatLenOnGoing,
			'getUatUserList': getUatLiveTestingProfile,
			'getDevUserList': getDevLiveTestingProfile
	}
	return render(request, 'index.html', context)


#django.contrib.auth module for login 
def login_view(request):
	#printing user auth in boolean if its active return True on server logs , just for curious 
	print(request.user.is_authenticated())
	#Getting form fields from forms.py class UserLoginForm 
	form = UserLoginForm(request.POST or None)
	#checking if form input is valid, make login
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password  = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		#if username and password is matched to db redirect to homepage which is index.html adress 127.0.0.1
		return redirect("/")
	


	return render(request, "form.html", {"form":form,'title':'login'})

#django.contrib.auth module for registration
def register_view(request):
	print(request.user.is_authenticated())
	#title for context, anyway we can declare direct in context dictonary
	title = "Register"
	#Getting form fields from forms.py class UserLoginForm 
	form = UserRegisterForm(request.POST or None)
	#checking if form input is valid, make registration complete and redirect to homepage 
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		#getting detail and commiting
		user.save()
		new_user = authenticate(username=user.username, password=password)

		login(request, new_user)
		#if registration is complete commit changes and redirect to homepage which is index.html adress 127.0.0.1
		return redirect('/')


		
	context = {
		"form":form,
		"title": title
	}
	#return to form if this view is called from urls.py
	return render(request, "form.html", context)

#small function for logout
def logout_view(request):
	logout(request)
	return redirect("/login")

def postRecipe(request):
	getPost = post.objects.all().order_by("-timestamp")
	forms = postForm(request.POST or None)
	if forms.is_valid():
		instance = forms.save(commit=False)
		instance.save()
		instance = forms.cleaned_data
		
	context = {
			'form':forms,
			'getPost':getPost,
	}
	return render(request, 'post.html',context)

#End of code
def startTesting(request):
	setTestingStatus = testerStatus(user=request.user, status='on-going {0}'.format(request.user))
	setTestingStatus.save()
	return redirect("/")

def startUatTesting(request):
	setUatStatus = uatStatus(user=request.user, status='on-going {0}'.format(request.user))
	setUatStatus.save()
	return redirect("/")

def stopTesting(request):
	if(request.user):
		deleteStatus = testerStatus.objects.get(user=request.user)
		deleteStatus.delete()
	
	return redirect("/")

def stopUatTesting(request):
	if(request.user):
		deleteStatus = uatStatus.objects.get(user=request.user)
		deleteStatus.delete()
	
	return redirect("/")