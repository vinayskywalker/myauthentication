from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
import google.oauth2.credentials
import google_auth_oauthlib.flow
from django.http import HttpResponseRedirect
from googleapiclient.discovery import build
from django.urls import reverse
import datetime
from datetime import timedelta
import time
from django.http import HttpResponse
import random
from uuid import uuid4, uuid5
import pytz




SCOPES = ['https://www.googleapis.com/auth/calendar']
mystate = None
myresponse = None


def oauthcallback(request):
	state = mystate
	state = request.session['state']

	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_secret.json',scopes=SCOPES,state=state)
	flow.redirect_uri = 'https://myauth-django.herokuapp.com/oauthcallback/'
	authorization_response = request.build_absolute_uri()
	flow.fetch_token(authorization_response=authorization_response)
	credentials = flow.credentials
	service = build('calendar','v3',credentials=credentials)
	calendar_ids = []
	page_token = None
	while True:
		calendar_list = service.calendarList().list(pageToken=page_token).execute()
		for calendar_list_entry in calendar_list['items']:
			calendar_ids.append(calendar_list_entry['id'])
		page_token = calendar_list.get('nextPageToken')
		if not page_token:
			break
	# return HttpResponseRedirect(reverse('calendar_details',kwargs={'caldetails':calendar_ids}))
	return render(request,'oauthcallback.html',context={"myrequest":request,"service":calendar_ids})

def caldetails(request,caldetails=None):
	return render(request,'cal_details.html',context={"caldetails":caldetails})

def connect_google():
	print("connecting")
	flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('client_secret.json',scopes=SCOPES)
	flow.redirect_uri = 'https://myauth-django.herokuapp.com/oauthcallback/'
	authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')
	return authorization_url,state


def login(request):
	authorization_url,state = connect_google()
	mystate = state
	request.session['state'] = state
	return HttpResponseRedirect(authorization_url)



def index(request):

	return render(request,'index.html',context={"myrequest":request})