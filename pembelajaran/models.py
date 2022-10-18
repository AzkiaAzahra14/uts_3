from django.db import models

# Create your models here.

class DosenFaperta(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFaperta(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFaperta(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFaperta(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFaperta(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFaperta(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFaperta(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFaperta(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFaperta(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFaperta(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DosenFeb(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFeb(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFeb(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFeb(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFeb(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFeb(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFeb(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFeb(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFeb(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFeb(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)



class DosenFh(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFh(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFh(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFh(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFh(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFh(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFh(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFh(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFh(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFh(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)


class DosenFisip(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFisip(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFisip(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFisip(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFisip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFisip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFisip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFisip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFisip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFisip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DosenFk(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFk(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFk(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFk(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFk(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFk(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFk(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFk(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFk(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFk(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)


class DosenFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFkip(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFkip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFkip(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFkip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFkip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFkip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFkip(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)


class DosenFt(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffFt(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaFt(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiFt(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJFt(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganFt(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMFt(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaFt(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahFt(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiFt(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DosenPascasarjana(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class StaffPascasarjana(models.Model):
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class MahasiswaPascasarjana(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=300)
    foto = models.CharField(max_length=300, null=True)


    def str(self):
        return "{}".format(self.nama)

class AkreditasiPascasarjana(models.Model):
    nilai = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class HMJPascasarjana(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class RuanganPascasarjana(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class UKMPascasarjana(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class DutaPascasarjana(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class MataKuliahPascasarjana(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)

class ProdiPascasarjana(models.Model):
    nama = models.CharField(max_length=50)

    def str(self):
        return "{}".format(self.nama)