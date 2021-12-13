from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import google.oauth2.credentials
import google_auth_oauthlib.flow
from django.http import HttpResponseRedirect



SCOPES = ['https://www.googleapis.com/auth/calendar']
mystate = None
myresponse = None


def oauthcallback(request):
	state = mystate
	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_secret.json',scopes=SCOPES,state=state)
	flow.redirect_uri = 'https://myauth-django.herokuapp.com/oauthcallback'
	return render(request,'oauthcallback.html',context={"myrequest":request})



def connect_google():
	print("connecting")
	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_secret.json',scopes=SCOPES)
	flow.redirect_uri = 'https://myauth-django.herokuapp.com/'
	authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')
	return authorization_url,state


def login(request):
	authorization_url,state = connect_google()
	mystate = state
	# response = redirect(to=authorization_url)
	return HttpResponseRedirect(authorization_url)

	return render(request,'login.html')


def index(request):

	return render(request,'index.html')