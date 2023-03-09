from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest

from pins.models import Pin, PinCategory


def gallery(request: HttpRequest, category_id=None) -> HttpResponse:
    """Функция для отображения всех пинов | категорий"""
    context = {
        'pins': Pin.objects.all(),
        'categories': PinCategory.objects.all(),
    }
    if category_id:
        context.update({'pins': Pin.objects.filter(category_id=category_id)})
    else:
        context.update({'pins': Pin.objects.all()})
    return render(request, 'gallery.html', context)
