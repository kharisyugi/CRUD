from pyexpat import model
from django.forms import ModelForm
from .models import *

class SilsilahForms(ModelForm):
    class Meta:
        model = Silsilah
        exclude = []