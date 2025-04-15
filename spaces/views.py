from django.shortcuts import render, get_object_or_404
from .models import Space

def space_list(request):
    spaces = Space.objects.filter(available=True)
    return render(request, 'spaces/space_list.html', {'spaces': spaces})

def space_detail(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    return render(request, 'spaces/space_detail.html', {'space': space})
