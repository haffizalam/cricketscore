from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from admin01.models import Item,Team,Heading,Overs,Over_count,Maindata,welcomepage,show_over,Target_run,Batsman_name,opponent
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def index(request):
	opobj=opponent.objects.all()
	nameobj=Batsman_name.objects.all()
	trobj=Target_run.objects.all()
	sovrobj=show_over.objects.all()
	obj=Item.objects.all()
	mobj=Maindata.objects.all()
	hobj=Heading.objects.all()
	Ovobj=Overs.objects.all()
	ovtobj=Over_count.objects.all()
	
	return render(request,'index.html',{'opobj':opobj,'obj':obj,'hobj':hobj,'Ovobj':Ovobj,'ovtobj':ovtobj,'mobj':mobj,'sovrobj':sovrobj,'trobj':trobj,'nameobj':nameobj}) 

def start(request):
	wpage=welcomepage.objects.all()
	return render(request,'start.html',{'wpage':wpage})

def admin_signup(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		email=request.POST['email']
		mobile=request.POST['phone']
		utype=request.POST['usrtype']
		pwd=request.POST['pwd']

		
		userobj=User(first_name=fname,last_name=lname,username=uname,password=make_password(pwd),email=email)
		userobj.save()

		user_profile=UserProfile(user=userobj,usertype=utype,mobile=mobile)
		user_profile.save()
		messages.success(request,"Account registered Successfully!")
		return redirect('/index/')
		
		messages.error(request,"Please check the data you have entered.")
		return redirect('/index/')
	
	return render(request,'index.html')
def admin_login(request):
	if request.method=='POST':
		usernm=request.POST['usrnm']
		pwd=request.POST['passwd']

		user=authenticate(username=usernm,password=pwd)
		if user:
			login(request,user)
			profileobj=UserProfile.objects.get(user__username=request.user)
			if profileobj.usertype=='Admin':
				return redirect('/admin01/index/')
			else:
				return HttpResponse("<h1>Invalid Credentials</h1>")

			
		else:
			return HttpResponse("<h1>Invalid Credentials</h1>")


@login_required
def logout_call(request):
	logout(request)
	return redirect('/index/')
