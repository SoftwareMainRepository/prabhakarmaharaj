from django.http import HttpResponse
from django.template import loader

def about(request):
  template = loader.get_template('about.html')
  context = {
    'name': "about",
  }
  return HttpResponse(template.render(context, request));
  

def service_section(request):
  template = loader.get_template('service.html')
  context = {
    'name': "service_section",
  }
  return HttpResponse(template.render(context, request));

  

def havan(request):
  template = loader.get_template('havan.html')
  context = {
    'name': "havan",
  }
  return HttpResponse(template.render(context, request));


def pandit(request):
  template = loader.get_template('pandit.html')
  context = {
    'name': "pandit",
  }
  return HttpResponse(template.render(context, request));



def termandservice(request):
  template = loader.get_template('termandservice.html')
  context = {
    'name': "termandservice",
  }
  return HttpResponse(template.render(context, request));


