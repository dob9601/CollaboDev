from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.http import HttpResponseNotFound
from django.shortcuts import render

from random import choice, randint

def index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('/tasks/')
        return render(request, 'index.html', {})
    return render(request, 'index.html', {})


def logout(request):
    auth_logout(request)
    return redirect('/')

def error404(request, exception):
    draw_pos = str(randint(1,10))
    if draw_pos[-1] == '1':
        draw_pos += 'st'
    elif draw_pos[-1] == '2':
        draw_pos += 'nd'
    elif draw_pos[-1] == '3':
        draw_pos += 'rd'
    else:
        draw_pos += 'th'
    message = choice(['Have you tried looking '+choice(['under the bed', 'in the fridge', 'down the side of the sofa', 'in the car', 'under your desk', 'in that random pot on your desk', 'in the '+draw_pos+' draw down on the left', 'in the reactor core', 'behind the bookshelf', 'on planet Edmunds', 'in Groots room', 'where Holston went']),
                      'Did you leave it '+choice(['in the taxi', 'on the train', 'on the roof of your car', 'in the tray at airport security', 'on the plane', 'at the bar', 'at the cafe', 'at the office', 'at the playground', 'on the internet', 'on a 404 page']),
                      'Did '+choice(['a llama steal it', 'an eagle steal it', 'it get baked into a pastry', 'it get thrown out of the window', 'it run away with your spouse', 'it get sucked into a turbine', 'it get sent into hyperspace', 'decay into muons', 'get turned into a cyborg by the borg', 'you try consulting Deep Thought', 'it get derezzed on the grid', 'it get sucked into Gargantua', 'you try consulting the tree of souls', 'it get chosen as a tribute in the reaping', 'it get sucked into a hydrorig', 'you try reporting it to the Tet'])])

    context = {
            'message': message
    }
    return HttpResponseNotFound(render(request, '404.html', context))
