from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest

from pins.models import Pin, PinCategory
from pins.forms import PinForm


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


def add_pin(request: HttpRequest) -> HttpResponse:
    """Функция создания пина"""
    if request.method == 'POST':
        form = PinForm(request.POST, request.FILES)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.user = request.user
            pin.save()
            return redirect('gallery')
    else:
        form = PinForm()
    return render(request, 'add_pin.html', {'form': form})
