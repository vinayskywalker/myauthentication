from django.shortcuts import render

# Create your views here.






def connect_google():
	print("connecting")


def login(request):
	if request.method == 'POST':
		print(request)
	return render(request,'login.html')


def index(request):
	return render(request,'index.html')