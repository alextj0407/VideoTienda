from django.contrib import admin
from .models import *

admin.site.register(Actor)
admin.site.register(Listado)
admin.site.register(Cliente)
admin.site.register(Director)
admin.site.register(Formato)
admin.site.register(Genero)
admin.site.register(Video)
admin.site.register(VideoHasGenero)
admin.site.register(ActorHasVideo)
admin.site.register(Alquiler)
# Register your models here.
