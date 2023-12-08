from django.shortcuts import render,loader
from django.http import HttpResponse

# Create your views here.
def htm(request):
    tem=loader.get_template('aa.html')
    return HttpResponse(tem.render())