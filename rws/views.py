from django.http import HttpResponse as hr
from django.http import JsonResponse as jr
from django.http import HttpResponseRedirect as hrr

import pickle

from django.shortcuts import render

a=[ {"review":"TEST 1 2 3"},{"review":"STILL TESTING ! @ #"}
]

def home(request):
	return render(request,"rws.html",{"main":a})

def process(request):
	temp={"review":request.GET["review"]}
	a.append(temp)
	return hrr("/home")

def disp(request):
	return render(request,"disp.html",{"main":a})

def loop(request):
	return hrr("/disp")

def save(request):
	return hrr("/home")