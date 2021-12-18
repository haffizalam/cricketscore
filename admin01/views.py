from django.shortcuts import render,redirect
from .models import Item,Team,Heading,Overs,Over_count,Maindata,welcomepage,show_over


# Create your views here.
def index(request):
	
	obj=Item.objects.all()
	tobj=Team.objects.all()
	hobj=Heading.objects.all()
	blobj=Overs.objects.all()
	ovtobj=Over_count.objects.all()
	for j in ovtobj:
		box=int(j.over)
		print(box+1)

	datain=[]
	for i in range(1,box+1):
		datain.append(i)
	print(datain)
	
	a=['Updated successfully !']
	return render(request,'adminpanel.html',{'obj':obj,'tobj':tobj,'hobj':hobj,'a':a,'blobj':blobj,'datain':datain,'ovtobj':ovtobj})

def upload_Vlink(request):
	
	if request.method=='POST':
		link=request.POST['vlink']
		vlobj=Item(video=link)
		vlobj.save()
		
		return redirect('/admin01/index/')
		
			
	return redirect('/admin01/index/')
def upload_heading(request):
	hobj=Heading.objects.all()
	if request.method=='POST':
		header=request.POST['upper_heading']
		hobj.update(heading_data=header)
		
	return redirect('/admin01/index/')


def update_link(request):
	vobj=Item.objects.all()
	if request.method=='POST':
		link=request.POST['ulink']
		vobj.update(video=link)
	return redirect('/admin01/index/')
'''def add_over(request):

	
	if request.method=='POST':
		
		ovr_data=request.POST['ovr']
		ovtobj=Over_count(over=ovr_data)
		ovtobj.save()
		
		data=int(ovr_data)
		datain=[]
		for i in range(1,data+1):
			datain.append(i)
		print(datain)
	return redirect('/admin01/index/')'''

def add_team(request):
	if request.method=='POST':
		tname=request.POST['T_name']
		capname=request.POST['cap_name']
		tscore=request.POST['t_score']
		twicket=request.POST['t_wicket']

		tobj=Team(team_name=tname,team_captain=capname,team_score=tscore,team_wicket=twicket)
		tobj.save()
	return redirect('/admin01/index/')
def welcome_header(request):
	wpobj=welcomepage.objects.all()
	if request.method=='POST':
		heading1=request.POST['header1']
		heading2=request.POST['header2']
		

		wpobj.update(h1=heading1,h2=heading2)
		a="Homepage Updated Successfully !"
	return redirect('/admin01/index/')

def show_team(request,id):
	ovtobj=Over_count.objects.all()
	for j in ovtobj:
		box=int(j.over)
		print(box+1)

	datain=[]
	for i in range(1,box+1):
		datain.append(i)
	print(datain)
	
	tdata=Team.objects.filter(id=id)
	global datateam
	def datateam(request,a=1):
		return tdata
    	
	obj=Item.objects.all()
	tobj=Team.objects.all()


	

	return render(request,'adminpanel.html',{'obj':obj,'tobj':tobj,'tdata':tdata,'ovtobj':ovtobj,'datain':datain})
def score_card(request):
	hobj=Heading.objects.all()
	dtobj=Team.objects.all()
	return render(request,'scorecard.html',{'dtobj':dtobj,'hobj':hobj})




def update_team(request):
	
	sovrobj=show_over.objects.all()	
	a=1
	tdata=datateam(request,a)
	obj=Item.objects.all()
	tobj=Team.objects.all()
	ballobj=Overs.objects.all()
	mobj=Maindata.objects.all()
	s=[]
	for i in ballobj:
		s.append(i.b1)
	for k in s:
		print(k)

	ovtobj=Over_count.objects.all()
	for j in ovtobj:
		box=int(j.over)
		print(box+1)

	datain=[]
	for n in range(1,box+1):
		datain.append(n)
	print(datain)
	try:

		if request.method=='POST':
			tscore=request.POST['t_score']
			twicket=request.POST['t_wicket']
			tdata.update(team_score=tscore,team_wicket=twicket)
		if request.method=='POST':
			ball_1=request.POST['b_1']
			ball_2=request.POST['b_2']
			ball_3=request.POST['b_3']
			ball_4=request.POST['b_4']
			ball_5=request.POST['b_5']
			ball_6=request.POST['b_6']
			ballobj.update(b1=ball_1,b2=ball_2,b3=ball_3,b4=ball_4,b5=ball_5,b6=ball_6)
		if request.method=='POST':
			ovtobj=Over_count.objects.all()
			ovr_data=request.POST['ovr']
			ovtobj.update(over=ovr_data)
			a='Data updated successfully !'
		if request.method=='POST':
			tname=request.POST['t_name']
			capname=request.POST['t_captain']
			tscore=request.POST['t_score']
			twicket=request.POST['t_wicket']

			mobj.update(team_name=tname,team_captain=capname,team_score=tscore,team_wicket=twicket)
			a=['Updated successfully !']
			
		if request.method=='POST':
			sovrs=request.POST['ovrs']
			sovrobj.update(sover=sovrs)
			
		return render(request,'adminpanel.html',{'obj':obj,'tobj':tobj,'tdata':tdata,'ballobj':ballobj,'datain':datain,'sovrobj':sovrobj})
	except:
		return render(request,'adminpanel.html',{'obj':obj,'tobj':tobj,'tdata':tdata,'ballobj':ballobj,'datain':datain,'sovrobj':sovrobj})


def del_team(request,id):
	pass

def showover(request):
	if request.method=='POST':
		#sovrobj=show_over.objects.all()
		svr=request.POST['sovr']
		ovtobj=show_over(sover=svr)
		ovtobj.save()


