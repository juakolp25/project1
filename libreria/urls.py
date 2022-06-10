from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inico'),
    path('inicio', views.inicio, name='principal'),
    path('diseno', views.diseno, name='diseno'),
    path('tatuajes', views.tatuajes, name='tatuajes'),
    path('formulario', views.contacto, name='formulario'),
    path('ayuda', views.ayuda, name='ayuda'),
    path('about', views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)