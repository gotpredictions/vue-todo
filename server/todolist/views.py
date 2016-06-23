from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, HttpResponseNotFound,\
    HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from . import models
import json


# Create your views here.
def index(request):
    return HttpResponseRedirect('/static/todolist/todo_home.html')


def get_list(request):
    return HttpResponse(json.dumps([[x.id, x.name, x.is_done] for x in models.Task.objects.all()]))


def details(request, task_id=None):
    try:
        task_details = models.Task.objects.get(['id', task_id])
        return HttpResponse(json.dumps({
            'name': task_details.name,
            'description': task_details.description,
            'is_done': task_details.is_done
        }))
    except ObjectDoesNotExist:
        return HttpResponseNotFound()

def create(request):

    if request.method == 'GET':
        return HttpResponseBadRequest('GET not allowed')

    try:
        data_in = request.read()
        print data_in
        data = json.loads(data_in)
        t = models.Task()
        t.name = data['name']
        t.is_done = False
        t.description = ''
        t.save()
        return HttpResponse(json.dumps({"id":t.id}))
    except Exception as ex:
        return HttpResponseBadRequest(ex.message)

def update(request, task_id=None):

    if request.method == 'GET':
        return HttpResponseBadRequest('GET not allowed')

    try:
        task_details = models.Task.objects.get(['id', task_id])
        data = json.load(request)
        if 'is_done' in data:
            task_details.is_done = data['is_done']
        if 'name' in data:
            task_details.name = data['name']
        if 'description' in data:
            task_details.description = data['description']
        task_details.save()
        return HttpResponse(json.dumps({
            'name': task_details.name,
            'description': task_details.description,
            'is_done': task_details.is_done
        }))
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
