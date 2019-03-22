from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound 
def test(request, *args, **kwargs):
    id = kwargs.get('id', '')
    resp = 'OK ' + str(id)
    return HttpResponse(resp) 

def not_found(request):
    return HttpResponseNotFound("Not Found!")
