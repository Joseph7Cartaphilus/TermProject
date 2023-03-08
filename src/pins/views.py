from django.shortcuts import render, get_object_or_404, redirect

from pins.models import Pin


# def gallery(request, category_id=None):
#     context = {
#         'pins': Pin.objects.all(),
#         'categories': PinCategory.objects.all(),
#     }
#     if category_id:
#         context.update({'pins': Pin.objects.filter(category_id=category_id)})
#     else:
#         context.update({'pins': Pin.objects.all()})
#     return render(request, 'gallery.html', context)
def gallery(request):
    return render(request, 'gallery.html')


def show_one_pin_by_slug_id(request, slug_pin: str, id: int):
    pin = get_object_or_404(Pin, slug=slug_pin, id=id)
    return render(request, 'one_pin.html', {
        'pin': pin,
        'id': pin.id,
        'slug': pin.slug
    })


def delete_pin(request, slug_pin: str):
    Pin.objects.get(slug=slug_pin).delete()
    return redirect('workshop')


def create_or_edit_pin(request, id_pin=None, slug_pin=None):
    form = EditForm()

    pin = None
    if id_pin is not None:
        pin = get_object_or_404(Pin, id=id_pin, slug=slug_pin, user=request.user)
        form = EditForm(instance=pin)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=pin, files=request.FILES, initial={'user': request.user})
        if form.is_valid():
            pin = form.save()
            return redirect('edit_pin', pin.slug, pin.id)

    return render(request, 'add_edit_pin.html', {
        'form': form,
        'id': id_pin,
        'slug': slug_pin,
    })
