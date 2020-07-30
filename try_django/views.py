from django.http import HttpResponse
from django.shortcuts import render
import os


def home_page(request):
	return HttpResponse("<h1> os.path</h1>")


def about(request):
	return HttpResponse("<h1> About us</h1>")

def contact(request):
	return HttpResponse("<h1> Contact us</h1>")

def home_page1(request):
	return render(request,"helloworld.html")


