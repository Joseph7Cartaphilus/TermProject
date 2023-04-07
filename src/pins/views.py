from rest_framework import viewsets, permissions
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from pins.models import Pin, PinCategory
from pins.forms import PinForm
from pins.serializers import PinSerializer, PinCategorySerializer


@login_required
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


@login_required
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


class PinViewSet(viewsets.ModelViewSet):
    """GET /pins/ - получить список всех пинов
       POST /pins/ - создать новый пин
       GET /pins/<id>/ - получить пин с указанным идентификатором
       PUT /pins/<id>/ - полностью обновить пин с указанным идентификатором
       PATCH /pins/<id>/ - частично обновить пин с указанным идентификатором
       DELETE /pins/<id>/ - удалить пин с указанным идентификатором"""
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAdminUser]


class PinCategoryViewSet(viewsets.ModelViewSet):
    """
    GET /categories/ - получить список всех категорий пинов
    POST /categories/ - создать новую категорию пинов
    GET /categories/<id>/ - получить категорию пинов с указанным идентификатором
    PUT /categories/<id>/ - полностью обновить категорию пинов с указанным идентификатором
    PATCH /categories/<id>/ - частично обновить категорию пинов с указанным идентификатором
    DELETE /categories/<id>/ - удалить категорию пинов с указанным идентификатором"""
    queryset = PinCategory.objects.all()
    serializer_class = PinCategorySerializer
    permission_classes = [permissions.IsAdminUser]
