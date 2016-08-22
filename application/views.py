from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import datetime

# from application.templates import *



# Create your views here.
def index(request):
	return render(request,'index.html')













# def synapten(request):
# 	return render(request, "registration.html")
# def test_login(request):
# 	uname=request.GET['uname']
# 	pwd=request.GET['pwd']
# 	try:
# 		obj=Login.objects.get(username=uname)
# 	except:
# 		return HttpResponse("user not available")
# 	if obj:
# 		if obj.password==pwd:
# 			return render(render, 'details.html')
# 			return HttpResponse("login successfull")




# 		else: 
# 			return HttpResponse("user is not available")
# def signup_login(request):
# 	return render(request, details.html)

	




# def test_login(request):
# 	uname=request.GET['uname']
# 	pwd=request.GET['pwd']
# 	try:
# 		obj= Login.objects.get(username=uname)
# 	except:
# 		return HttpResponse("user not available")
# 	if obj:
# 		if obj.password==pwd:
# 			return render(request,'details.html')

# 			#return HttpResponse("Login successfull")
# 		else:
# 			return HttpResponse("incorrect password")
# def jamal(request):
# 	return render(request,'details.html')
# def sign_up(request):
# 	return render(requast,'sign_up.html')
# def login(request):
	# return HttpResponse(' i am succesfull login')
# @csrf_protect
# def cal(request):
# 	now = datetime.datetime.now()
#     # html = "<html><body>It is now %s.</body></html>" % now
#     # return HttpResponse()
#     return render_to_response(request,'cal1.html',{'data':now})
# def jamal(request):
	# return render(request, 'modelwindow.html')