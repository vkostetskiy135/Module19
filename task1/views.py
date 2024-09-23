from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def main_page(request):
    return render(request, 'platform.html')


def games_page(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context=context)


def cart_page(request):
    return render(request, 'cart.html')


def sign_up(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')
            if password != repeat_password:
                info['password_error'] = 'Пароли не совпадают'

            for user in Buyer.objects.all():
                if user.name == username:
                    info['user_exists_error'] = 'Пользователь уже существует'

            if info:
                return render(request, 'registration_page.html', {'form': form, 'info': info})
            else:
                Buyer.objects.create(name=username, password=password, age=age)
                return HttpResponse(f'Приветствуем, {username}!')

        if form.errors.as_data()['age']:
            info['age_error'] = form.errors.as_data()['age'][0].message
            return render(request, 'registration_page.html', {'form': form, 'info': info})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})