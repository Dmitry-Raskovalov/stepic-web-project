from django.shortcuts import render
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    id = kwargs.get('id', '')
    resp = 'OK ' + str(id)
    return HttpResponse(resp)

