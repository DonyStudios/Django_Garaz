from django.http import HttpResponse
from django.template import loader
from .models import Ridic, Vozidlo, Motor, Brzdy, Pneu, Odpruzeni
from django.shortcuts import render

def garaz1(request):
  mymembers = Vozidlo.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def vozidlo(request, id):
  vozidlo = Vozidlo.objects.get(id=id)
  return render(request, 'vozidlo.html', {'vozidlo': vozidlo})


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def list_ridici(request):
    ridici = Ridic.objects.all()
    return render(request, 'list_ridici.html', {'ridici': ridici})

def ridic(request, id):
  ridici = Ridic.objects.get(id=id)
  return render(request, 'ridic.html', {'ridici': ridici})

def list_soucastky(request):
    motory = Motor.objects.all()
    brzdy = Brzdy.objects.all()
    pneu = Pneu.objects.all()
    odpruzeni = Odpruzeni.objects.all()
    return render(request, 'list_soucastky.html', {'motory': motory,'brzdy': brzdy,'pneu': pneu,'odpruzeni': odpruzeni})

def motor(request, id):
  motory = Motor.objects.get(id=id)
  return render(request, 'motor.html', {'motory': motory})

def brzdy(request, id):
  brzda = Brzdy.objects.get(id=id)
  return render(request, 'brzda.html', {'brzda': brzda})

def pneu(request, id):
  pnei = Pneu.objects.get(id=id)
  return render(request, 'pneu.html', {'pnei': pnei})

def odpruzeni(request, id):
  pruzina = Odpruzeni.objects.get(id=id)
  return render(request, 'odpruzeni.html', {'pruzina': pruzina})