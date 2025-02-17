from django.shortcuts import render, redirect
from .forms import *
from .forms import UserForm
from .models import *
import random
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    films = Kino.objects.all()
    artists = Artist.objects.all()
    print(films)
    print(artists)
    randomFilm=random.choice(films)
    data = {'randomFilm':randomFilm,'films':films,'artists':artists}
    return render(request, 'index.html',data)

from django.views import generic
class kinoList(generic.ListView):
    model = Kino
    # paginate_by = 6 #количество фильмов на странице

class artistList(generic.ListView):
    model = Artist

class kinoDetail(generic.DetailView):
    model = Kino


def registration(request):
    if request.POST:
        print(1)
        form = UserForm(request.POST)
        if form.is_valid():
            print(2)
            k1 = form.cleaned_data.get('username')
            k2 = form.cleaned_data.get('email')
            k3 = form.cleaned_data.get('password1')
            k4 = form.cleaned_data.get('first_name')
            k5 = form.cleaned_data.get('last_name')
            User.objects.create_user(username=k1,email=k2, password=k3)
            # user1 =  authenticate(username=k1, password=k2)
            myuser = User.objects.get(username=k1)  # находим пользователя
            # заполняем данные
            myuser.last_name = k5
            myuser.first_name = k4
            myuser.save()
            Profile.objects.create(user=myuser)# сохраняем
            login(request, myuser)  # вход пользователя на сайт
            return redirect('index')  # на главную
    else:
        form = UserForm()
    data = {'form':form}
    return render(request,'registration/reg.html',data)

def profile(request):
    return render(request, 'kabinet.html')

def profileChange(request):
    form= ProfileForm()
    data = {'form':form}
    if request.POST:
        k1= request.POST['newpodpiska']
        user = User.objects.get(id=request.user.id)
        user.profile.podpiska_id = k1
        user.profile.save()
        return redirect('kabinet')
    return render(request, 'kabinet.html',data)