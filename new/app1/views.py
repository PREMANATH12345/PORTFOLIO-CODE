from django.shortcuts import render,loader
from django.http import HttpResponse

# Create your views here.
def aa(request):
    tem=loader.get_template('aa.html')
    return HttpResponse(tem.render())
def about(request):
    tem=loader.get_template('about.html')
    return HttpResponse(tem.render())
def pro(request):
    tem=loader.get_template('pro.html')
    return HttpResponse(tem.render())
def qua(request):
    tem=loader.get_template('qua.html')
    return HttpResponse(tem.render())
def skills(request):
    tem=loader.get_template('skills.html')
    return HttpResponse(tem.render())