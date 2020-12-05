# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Partidas, Productos, Salida_productos, Stock

admin.site.register(Partidas)
admin.site.register(Productos)
admin.site.register(Salida_productos)
admin.site.register(Stock)

