from django.shortcuts import render
from django.http import HttpResponse

from game.models import Scene, Option, Item, Session, Inventory

def index(request):
    context = {}
    return render(request, 'game/index.html', context)

def scene(request, scene_id):
    normalized_id = int(scene_id)
    session = str(request.GET.get('session', ""))
    scene = Scene.objects.get(pk=normalized_id)

    if session:
        session = Session.objects.get(uuid=session)
    else:
        # start a new session
        session = Session(scene=scene)
        session.save()

    # select the available options
    options = Option.objects.filter(scene=normalized_id)
    inventory = Inventory.objects.filter(session=session)

    pruned_options = []
    for option in options:
        adding = True
        # if there is a required item, check if the player has it
        if option.required_item:
            if inventory.filter(item=option.required_item):
                adding = True
            else:
                adding = False

        #if there is a prohibited item, check if the player had it
        if option.prohibited_item:
            if inventory.filter(item=option.prohibited_item):
                adding = False

        # add the option if it is ok
        if adding:
            pruned_options.append(option)

    context = {
        'scene': scene,
        'options': pruned_options,
        'session': session.uuid,
    }
    return render(request, 'game/scene.html', context)

def option(request, option_id):
        return HttpResponse("This is Option #%s." % option_id)
