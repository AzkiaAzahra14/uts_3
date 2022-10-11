from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import DosenFaperta, DutaFkip,  StaffFaperta, MahasiswaFaperta
from . models import  DosenFeb, StaffFeb, MahasiswaFeb
from . models import  DosenFh, StaffFh, MahasiswaFh
from . models import  DosenFisip, StaffFisip, MahasiswaFisip
from . models import  DosenFk, StaffFk, MahasiswaFk    
from . models import  DosenFkip, StaffFkip, MahasiswaFkip, AkreditasiFkip, HMJFkip, RuanganFkip, UKMFkip, DutaFkip, MataKuliahFkip
from . models import  DosenFt, StaffFt, MahasiswaFt
from . models import  DosenPascasarjana, StaffPascasarjana, MahasiswaPascasarjana   



# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def faperta(request):
    template = loader.get_template('faperta.html')
    dosen = DosenFaperta.objects.all()
    staff = StaffFaperta.objects.all()
    mahasiswa = MahasiswaFaperta.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def feb(request):
    template = loader.get_template('feb.html')
    dosen = DosenFeb.objects.all()
    staff = StaffFeb.objects.all()
    mahasiswa = MahasiswaFeb.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fh(request):
    template = loader.get_template('fh.html')
    dosen = DosenFh.objects.all()
    staff = StaffFh.objects.all()
    mahasiswa = MahasiswaFh.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fisip(request):
    template = loader.get_template('fisip.html')
    dosen = DosenFisip.objects.all()
    staff = StaffFisip.objects.all()
    mahasiswa = MahasiswaFisip.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fk(request):
    template = loader.get_template('fk.html')
    dosen = DosenFk.objects.all()
    staff = StaffFk.objects.all()
    mahasiswa = MahasiswaFk.objects.all()    
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
    }
    return HttpResponse(template.render())

def fkip(request):
    template = loader.get_template('fkip.html')
    dosen = DosenFkip.objects.all()
    staff = StaffFkip.objects.all()
    mahasiswa = MahasiswaFkip.objects.all()
    akreditasi = AkreditasiFkip.objects.all()
    hmj = HMJFkip.objects.all()
    ruangan = RuanganFkip.objects.all()
    ukm = UKMFkip.objects.all()
    duta = DutaFkip.objects.all()
    matakuliah = MataKuliahFkip.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah
    }
    return HttpResponse(template.render(context))

def ft(request):
    template = loader.get_template('ft.html')
    dosen = DosenFt.objects.all()
    staff = StaffFt.objects.all()
    mahasiswa = MahasiswaFt.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
         
    }
    return HttpResponse(template.render())

def pascasarjana(request):
    template = loader.get_template('pascasarjana.html')
    dosen = DosenPascasarjana.objects.all()
    staff = StaffPascasarjana.objects.all()
    mahasiswa = MahasiswaPascasarjana.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
         
    }
    return HttpResponse(template.render())

def visidanmisi(request):
    template = loader.get_template('visidanmisi.html')
    return HttpResponse(template.render())