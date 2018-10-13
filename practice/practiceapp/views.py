from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
	return render(request,"index.html",{'bgimg':'bg.jpg'})
	
def loginpage(request):
	name = request.GET.get("name")
	lname = request.GET.get("cast")
	roll = request.GET.get("roll")
	clg = request.GET.get("clg")
	course = request.GET.get("course")
	focc = request.GET.get("focc")
	mocc = request.GET.get("mocc")
	add = request.GET.get("add")
	cntry = request.GET.get("cntry")
	
	
	return render(request,"login.html",{'name':name,'lname':lname,\
	'roll':roll,'clg':clg,'course':course,'focc':focc,'mocc':mocc,\
	'add':add,'cntry':cntry})