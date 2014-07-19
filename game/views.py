from django.shortcuts import render
from django.http import HttpResponse

from game.models import Scene, Option

def index(request):
    context = {}
    return render(request, 'game/index.html', context)

def scene(request, scene_id):
    context = {
        'scene': Scene.objects.get(pk=int(scene_id)),
        'options': Option.objects.filter(scene=int(scene_id))
    }
    return render(request, 'game/scene.html', context)

def option(request, option_id):
        return HttpResponse("This is Option #%s." % option_id)
