from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db import models
from django.forms import forms
from silsilah.forms import SilsilahForms

from silsilah.models import Silsilah


def getall(request):
    data = Silsilah.objects.all()
    form_silsilah = SilsilahForms()
    if request.method == 'POST':
        barang = SilsilahForms(request.POST)
        if barang.is_valid():
            barang.save()
            return redirect('/')
    return render(request,'home.html',{'data':data,'form':form_silsilah})
def update(req, id):
    if req.POST:
        task = Silsilah.objects.filter(pk=id).update(nama=req.POST['nama'], jk=req.POST['jk'])
        return redirect('/')

    task = Silsilah.objects.filter(pk=id).first()
    return render(req, 'update.html', {
        'data': task,
    })
def delete(req, id):
    Silsilah.objects.filter(pk=id).delete()
    return redirect('/')

