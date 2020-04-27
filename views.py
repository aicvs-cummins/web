from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')