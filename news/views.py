from django.shortcuts import render, redirect
from .models import Newspaper, Category, Verificateuser
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import DetailView
import time
from random import randint
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):

	news = Newspaper.objects.order_by('-date')[0:4]
	categories = Category.objects.all()
	try:
		verif = Verificateuser.objects.get(user_v=request.user)

		if request.method == 'POST':
			try:
				images = request.FILES['Profile_Image']
				verif.image = images
				verif.save()
			except:
				messages.warning(request, 'Upload Photo Failed')
	except:
		return render(request, 'index.html', {'news':news, 'categories':categories})

	
	return render(request, 'index.html', {'news':news, 'categories':categories, 'verif':verif})
user = None
veryfication_number = None
def login(request):
	
	if request.method == 'POST':
		try:
			username = request.POST['Username_up']
			true = True
			for i in username:
				if i.isdigit():
					true = False
			if true == False:
				messages.warning(request, 'Username Should Only Have Letters')
			password = request.POST['Password_up']
			if len(password) < 8:
				messages.warning(request, 'Very Insecure Password')
			email = request.POST['Email_up']
			if email == '':
				messages.warning(request, 'Please Enter Your Valid Email')
			try:
				global veryfication_number
				veryfication_number = randint(1000, 9999)
				send_mail('Veryfication', f'Your Veryfication Number is {veryfication_number}', 'raz.miqayelyan@gmail.com', [email], fail_silently=False)
			except:
				redirect('login')
			if User.objects.filter(username=username).exists():
				messages.warning(request, 'Username Taken')
				return redirect('login')
			if User.objects.filter(email=email).exists() and email != '':
				messages.warning(request, 'Email Taken')
				return redirect('login')

			elif email != '' and true != False and len(password) >= 8:
				global user
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				messages.warning(request, 'User Created Successfully')
				return redirect('emailconf')

		except:
			username = request.POST['Username']
			password = request.POST['Password']
			user = auth.authenticate(username=username, password=password)
			if user == None:
				messages.warning(request, 'Login or Password is not Correct')
			else:
				auth.login(request, user)
				return redirect('index')

	return render(request, 'login.html')

@login_required
def logout(request):
	auth.logout(request)
	return redirect('index')

def NewsDetail(request,pk,slug):
	new = Newspaper.objects.get(id=pk)
	news = Newspaper.objects.filter(category__slug=slug)[0:4]
	return render(request, 'single.html', {'new_one':new, 'news':news})

@login_required
def delete(request, pk):
	news = Newspaper.objects.get(id=pk)
	news.delete()
	delete_message = messages.warning(request, 'Your News Are Deleted Successfully')
	return redirect('index')

def kategorya(request, slug):
	news = Newspaper.objects.filter(category__slug=slug)
	categories = Category.objects.all()
	return render(request, 'index.html', {'news':news, 'categories':categories})


u = None
reset_email = None
def reset(request):
	x = 1
	if request.method == 'POST':
		username = request.POST['Username']
		if User.objects.filter(username=username).exists():
			global u
			u = User.objects.get(username=username)
			global reset_email
			reset_email = randint(1000, 9999)
			send_mail('Veryfication', f'Your Veryfication Number is {reset_email}', 'raz.miqayelyan@gmail.com', [u.email], fail_silently=False)
			return redirect('resetconf')
		else:
			messages.warning(request, 'Unknown Username')
	return render(request, 'login.html', {'x':x}) 

def resetconf(request):
	y = 2
	if request.method == 'POST':
			password = request.POST['Password']
			password_c = request.POST['Password_c']
			res = request.POST['Reset_email']
			if password == password_c and res == str(reset_email):
				u.set_password(password)
				u.save()
				messages.warning(request, 'Password Changed Successfully')
				return redirect('index')
			else:
				messages.warning(request, 'Confirm Password or Security Number are Incorrect')

	return render(request, 'login.html', {'y':y}) 

def emailconf(request):
	l = 1
	if user != None and veryfication_number != None:
		if request.method == 'POST':
			email_confirmm = request.POST['Email_confirm']
			if email_confirmm ==  str(veryfication_number):
				veryfi = Verificateuser.objects.create(user_v=user, verificated=True)
				return redirect('login')
			else:
				messages.warning(request, 'Security Number are Incorrect')
				veryfi = Verificateuser.objects.create(user_v=user, verificated=False)
				return redirect('login')


	
	return render(request, 'login.html', {'l':l})

def search(request):
	query = request.GET['query']
	allPosts = Newspaper.objects.filter(title__icontains=query)
	
	return render(request, 'index.html', {'allPosts':allPosts})