from django.contrib import admin

from core.models import Carro, Marca

admin.site.register(Carro) # registra o modelo Carro no admin
admin.site.register(Marca) # registra o modelo Marca no admin