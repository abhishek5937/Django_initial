from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blog_home(request):
	return HttpResponse("<h1>Hello charul</h1>")
