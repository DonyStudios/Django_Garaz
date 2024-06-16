from django.http import HttpResponse
from django.template import loader
from .models import Ridic, Vozidlo
from django.shortcuts import render

def garaz1(request):
  mymembers = Vozidlo.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Vozidlo.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def list_ridici(request):
    ridici = Ridic.objects.all()
    return render(request, 'list_ridici.html', {'ridici': ridici})

def ridic(request, id):
  ridici = Ridic.objects.get(id=id)
  return render(request, 'ridic.html', {'ridici': ridici})