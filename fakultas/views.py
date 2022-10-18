from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import  DosenFaperta, StaffFaperta, MahasiswaFaperta, AkreditasiFaperta, HMJFaperta, RuanganFaperta, UKMFaperta, DutaFaperta, MataKuliahFaperta, ProdiFaperta
from . models import  DosenFeb, StaffFeb, MahasiswaFeb, AkreditasiFeb, HMJFeb, RuanganFeb, UKMFeb, DutaFeb, MataKuliahFeb, ProdiFeb  
from . models import  DosenFh, StaffFh, MahasiswaFh, AkreditasiFh, HMJFh, RuanganFh, UKMFh, DutaFh, MataKuliahFh, ProdiFh
from . models import  DosenFisip, StaffFisip, MahasiswaFisip, AkreditasiFisip, HMJFisip, RuanganFisip, UKMFisip, DutaFisip, MataKuliahFisip, ProdiFisip
from . models import  DosenFk, StaffFk, MahasiswaFk, AkreditasiFk, HMJFk, RuanganFk, UKMFk, DutaFk, MataKuliahFk, ProdiFk
from . models import  DosenFkip, StaffFkip, MahasiswaFkip, AkreditasiFkip, HMJFkip, RuanganFkip, UKMFkip, DutaFkip, MataKuliahFkip, ProdiFkip
from . models import  DosenFt, StaffFt, MahasiswaFt, AkreditasiFt, HMJFt, RuanganFt, UKMFt, DutaFt, MataKuliahFt, ProdiFt
from . models import  DosenPascasarjana, StaffPascasarjana, MahasiswaPascasarjana, AkreditasiPascasarjana, HMJPascasarjana, RuanganPascasarjana, UKMPascasarjana, DutaPascasarjana, MataKuliahPascasarjana, ProdiPascasarjana 



# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def faperta(request):
    template = loader.get_template('faperta.html')
    dosen = DosenFaperta.objects.all()
    staff = StaffFaperta.objects.all()
    mahasiswa = MahasiswaFaperta.objects.all() 
    akreditasi = AkreditasiFaperta.objects.all()
    hmj = HMJFaperta.objects.all()
    ruangan = RuanganFaperta.objects.all()
    ukm = UKMFaperta.objects.all()
    duta = DutaFaperta.objects.all()
    matakuliah = MataKuliahFaperta.objects.all()
    prodi = ProdiFaperta.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,  
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,  
    }
    return HttpResponse(template.render())

def feb(request):
    template = loader.get_template('feb.html')
    dosen = DosenFeb.objects.all()
    staff = StaffFeb.objects.all()
    mahasiswa = MahasiswaFeb.objects.all() 
    akreditasi = AkreditasiFeb.objects.all()
    hmj = HMJFeb.objects.all()
    ruangan = RuanganFeb.objects.all()
    ukm = UKMFeb.objects.all()
    duta = DutaFeb.objects.all()
    matakuliah = MataKuliahFeb.objects.all()
    prodi = ProdiFeb.objects.all()   
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,  
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,  
    }
    return HttpResponse(template.render())

def fh(request):
    template = loader.get_template('fh.html')
    dosen = DosenFh.objects.all()
    staff = StaffFh.objects.all()
    mahasiswa = MahasiswaFh.objects.all()  
    akreditasi = AkreditasiFh.objects.all()
    hmj = HMJFh.objects.all()
    ruangan = RuanganFh.objects.all()
    ukm = UKMFh.objects.all()
    duta = DutaFh.objects.all()
    matakuliah = MataKuliahFh.objects.all()
    prodi = ProdiFh.objects.all()  
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,    
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,
    }
    return HttpResponse(template.render())

def fisip(request):
    template = loader.get_template('fisip.html')
    dosen = DosenFisip.objects.all()
    staff = StaffFisip.objects.all()
    mahasiswa = MahasiswaFisip.objects.all() 
    akreditasi = AkreditasiFisip.objects.all()
    hmj = HMJFisip.objects.all()
    ruangan = RuanganFisip.objects.all()
    ukm = UKMFisip.objects.all()
    duta = DutaFisip.objects.all()
    matakuliah = MataKuliahFisip.objects.all()
    prodi = ProdiFisip.objects.all()   
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,  
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,  
    }
    return HttpResponse(template.render())

def fk(request):
    template = loader.get_template('fk.html')
    dosen = DosenFk.objects.all()
    staff = StaffFk.objects.all()
    mahasiswa = MahasiswaFk.objects.all() 
    akreditasi = AkreditasiFk.objects.all()
    hmj = HMJFk.objects.all()
    ruangan = RuanganFk.objects.all()
    ukm = UKMFk.objects.all()
    duta = DutaFk.objects.all()
    matakuliah = MataKuliahFk.objects.all()
    prodi = ProdiFk.objects.all()   
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,  
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,  
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
    prodi = ProdiFkip.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,
    }
    return HttpResponse(template.render(context))

def ft(request):
    template = loader.get_template('ft.html')
    dosen = DosenFt.objects.all()
    staff = StaffFt.objects.all()
    mahasiswa = MahasiswaFt.objects.all()
    akreditasi = AkreditasiFt.objects.all()
    hmj = HMJFt.objects.all()
    ruangan = RuanganFt.objects.all()
    ukm = UKMFt.objects.all()
    duta = DutaFt.objects.all()
    matakuliah = MataKuliahFt.objects.all()
    prodi = ProdiFt.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,
         
    }
    return HttpResponse(template.render())

def pascasarjana(request):
    template = loader.get_template('pascasarjana.html')
    dosen = DosenPascasarjana.objects.all()
    staff = StaffPascasarjana.objects.all()
    mahasiswa = MahasiswaPascasarjana.objects.all()
    akreditasi = AkreditasiPascasarjana.objects.all()
    hmj = HMJPascasarjana.objects.all()
    ruangan = RuanganPascasarjana.objects.all()
    ukm = UKMPascasarjana.objects.all()
    duta = DutaPascasarjana.objects.all()
    matakuliah = MataKuliahPascasarjana.objects.all()
    prodi = ProdiPascasarjana.objects.all()
    context = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
        'dataAkreditasi': akreditasi,
        'dataHMJ': hmj,
        'dataRuangan': ruangan,
        'dataUKM': ukm,
        'dataDuta': duta,
        'dataMataKuliah': matakuliah,
        'dataProdi': prodi,
         
    }
    return HttpResponse(template.render())

def visidanmisi(request):
    template = loader.get_template('visidanmisi.html')
    return HttpResponse(template.render())