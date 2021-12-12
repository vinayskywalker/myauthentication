from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import google.oauth2.credentials
import google_auth_oauthlib.flow


SCOPES = ['https://www.googleapis.com/auth/calendar']



def connect_google():
	print("connecting")
	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_secret.json',scopes=SCOPES)
	flow.redirect_uri = 'https://myauth-django.herokuapp.com/oauth2callback'
	authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')




def login(request):
	
	if request.method == 'POST':
		print(request)

	return render(request,'login.html')


def index(request):
	return render(request,'index.html')