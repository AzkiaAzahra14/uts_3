from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import  Persegi
from . models import  PersegiPanjang
from . models import  JajarGenjang
from . models import  Segitiga
from . models import  Lingkaran


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def persegi(request):
    template = loader.get_template('faperta.html')
    persegi = DataPersegi.objects.all()
    context = {
        'dataPersegi': persegi, 
    }
    return HttpResponse(template.render())

def persegipanjang(request):
    template = loader.get_template('feb.html')
    persegipanjang = DataPersegiPanjang.objects.all()   
    context = {
        'dataPersegiPanjang': persegipanjang,
    }
    return HttpResponse(template.render())

def jajargenjnag(request):
    template = loader.get_template('fh.html')
    jajargenjang = DataJajarGenjang.objects.all()
    context = {
        'dataJajarGenjang': jajargenjang,
    }
    return HttpResponse(template.render())

def segitiga(request):
    template = loader.get_template('fisip.html')
    segitiga = DataSegitiga.objects.all()   
    context = {
        'dataSegitiga': segitiga, 
    }
    return HttpResponse(template.render())

def lingkaran(request):
    template = loader.get_template('fk.html')
    lingkaran = DataLingkaran.objects.all()   
    context = {
        'dataLingkaran': lingkaran, 
    }
    return HttpResponse(template.render())
