from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Typesofpuja


def festive_service(request):
  festival_puja = Typesofpuja.objects.all().values()
  template = loader.get_template('typesofpuja/festival_puja_services.html')
  context = {
    'festival_puja': festival_puja,
  }
  return HttpResponse(template.render(context, request))


  
def details(request, id):
  festival_puja_d = Typesofpuja.objects.get(id=id)
  template = loader.get_template('typesofpuja/festive_puja_details.html')
  context = {
    'festival_puja_d': festival_puja_d,
  }
  return HttpResponse(template.render(context, request))
  
def mainservices(request):
  template = loader.get_template('service.html')
  context = {
    'name': "all_services",
  }
  return HttpResponse(template.render(context, request))                 