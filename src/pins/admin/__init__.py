from django.contrib import admin

from pins.admin.pin import PinAdmin
from pins.admin.pin_category import PinCategoryAdmin
from pins.models import Pin, PinCategory

admin.site.register(Pin, PinAdmin)  # Регистрация модели Pin в админке
admin.site.register(PinCategory, PinCategoryAdmin)  # Регистрация модели Pin artist в админке
