from django.db import models

# Create your models here.

class Persegi(models.Model):
    nomor = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    rumus = models.CharField(max_length=50)
    foto = models.CharField(max_length=300, null=True)
    pengertian = models.CharField(max_length=100)

    def str(self):
        return "{}".format(self.nama)

class PersegiPanjang(models.Model):
    nomor = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    rumus = models.CharField(max_length=50)
    foto = models.CharField(max_length=300, null=True)
    pengertian = models.CharField(max_length=100)

    def str(self):
        return "{}".format(self.nama)

class JajarGenjang(models.Model):
    nomor = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    rumus = models.CharField(max_length=50)
    foto = models.CharField(max_length=300, null=True)
    pengertian = models.CharField(max_length=100)

    def str(self):
        return "{}".format(self.nama)

class Segitiga(models.Model):
    nomor = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    rumus = models.CharField(max_length=50)
    foto = models.CharField(max_length=300, null=True)
    pengertian = models.CharField(max_length=100)

    def str(self):
        return "{}".format(self.nama)

class Lingkaran(models.Model):
    nomor = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    rumus = models.CharField(max_length=50)
    foto = models.CharField(max_length=300, null=True)
    pengertian = models.CharField(max_length=100)

    def str(self):
        return "{}".format(self.nama)
