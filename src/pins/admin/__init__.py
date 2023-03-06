from django.contrib import admin

from src.pins.admin.pin import PinAdmin
from src.pins.admin.pin_category import PinCategoryAdmin
from src.pins.models import Pin, PinCategory

admin.site.register(Pin, PinAdmin)
admin.site.register(PinCategory, PinCategoryAdmin)

