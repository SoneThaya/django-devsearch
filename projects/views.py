from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('here are our projects')

def project(request, pk):
    return HttpResponse('single project' + ' ' + str(pk))
