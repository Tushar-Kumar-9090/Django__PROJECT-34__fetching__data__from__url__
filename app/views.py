from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display(request,tushar):
    return HttpResponse(f"<center><h1>Hii Good Morning {tushar} </h1></center>")
    
