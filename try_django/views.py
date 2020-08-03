from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
import os


def home_page(request):
	return HttpResponse("<h1> Hello World!</h1>")


def about_page(request):
	return render(request,"about.html",{"title":"About Us"})

def contact_page(request):
	return HttpResponse("<h1> Contact us</h1>")

def home_page1(request):
	my_title="'Hello There....'"
	#define variables and pass then as a dictionary and use the key in other page to display the corresponding value
	return render(request,"helloworld.html",{"title":my_title})

def example_page(request):
	context       ={"title":"Example"}
	template_name ="helloworld.html"
	template_obj  =get_template(template_name)
	rendered_item =template_obj.render(context)
	return HttpResponse(rendered_item)

