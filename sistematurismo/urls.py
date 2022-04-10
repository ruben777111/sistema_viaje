from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('cliente/contenidocliente',views.cliente,name='contenido'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

