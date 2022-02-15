from codecs import register
import site
from django.contrib import admin
from django.db import models

from silsilah.models import Silsilah


admin.site.register(Silsilah)