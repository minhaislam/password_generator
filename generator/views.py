from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, 'generator/index.html')


def view(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length'))
    thepassword = ''
    
    for x in range(length):
        thepassword +=  random.choice(characters)

    return render(request, 'generator/view.html', {'password': thepassword})