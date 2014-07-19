from django.shortcuts import render
from django.http import HttpResponse

from game.models import Scene, Option, Item, Session, Inventory

def index(request):
    context = {}
    return render(request, 'game/index.html', context)

def scene(request, scene_id):
    normalized_id = int(scene_id)
    session = ""

    if normalized_id == 1:
        # start a new session
        session = "new"



    context = {
        'scene': Scene.objects.get(pk=normalized_id),
        'options': Option.objects.filter(scene=normalized_id),
        'session': session_id,
    }
    return render(request, 'game/scene.html', context)

def option(request, option_id):
        return HttpResponse("This is Option #%s." % option_id)
