from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from . import models
import json


# Create your views here.
def index(request):
    return render(request, 'todo_home.html')


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
