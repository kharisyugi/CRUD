from django.contrib import admin
from django.urls import path
from silsilah import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getall),
    path('<id>/delete/', views.delete),
    path('<id>/update/', views.update),
]
