from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
from django.core import serializers
import json

def index(request):
    return render(request, "personal_page/home.html")

def smartlist(request):
    return render(request, "personal_page/smartlist.html")

def algo(request):
    return render(request, "personal_page/algo.html")

def barry(request):
    return render(request, "personal_page/barry.html")
