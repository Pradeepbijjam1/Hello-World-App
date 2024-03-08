from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template import loader

def hello_world_json(request):
    data = {'Message': 'Hello World!'}
    return JsonResponse(data)

def hello_world_html(request):
    template = loader.get_template('hello/hello_world.html')
    context = {'message': 'Hello World!'}
    return HttpResponse(template.render(context, request))
