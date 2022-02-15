from django.db import models

class Silsilah(models.Model):
    # jenis_kelamin = {
    #     'lk': 'laki-laki',
    #     'pr': 'Perempuan',
    # }
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    jk= models.CharField(max_length=100)