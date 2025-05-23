from django.shortcuts import render, get_object_or_404
from fighters.models import Fighter 

def index(request):
    characters = Fighter.objects.all()
    return render(request, 'fighters/index.html',{"cards": characters})

def page_figher(request, foto_id):
    character = get_object_or_404(Fighter, pk=foto_id)
    return render(request, 'fighters/page_figher.html',{"character": character})