from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from main.models import Street


# Create your views here.
def index(request):
    return render(request, 'main/index.html', locals())


def about(request):
    return render(request, 'main/about.html', locals())


# @login_required
def street(request):
    streets = Street.objects.all()
    if request.method == 'POST':
        streetname = request.POST['Street']
        street = Street()
        street.StreetName= streetname
        street.save()

    return render(request, 'main/street.html', locals())



def login(request):
    if request.method == "POST":
        login = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=login, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect("/test")
        else:
            print("authentication failed")

    return render(request, 'main/login.html', locals())


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


def register(request):
    if request.method == "POST":
        login = request.POST['login']
        password = request.POST['password']
        user = auth.models.User.objects.create_user(username=login, password=password)
        user = auth.authenticate(username=login, password=password)
        if user:
            auth.login(request, user)
        else:
            print("authentication failed")
        return HttpResponseRedirect("/test")

    return render(request, 'main/register.html', locals())


@login_required
def test(request):
    return render(request, 'main/test.html', locals())


def service(request):
    return render(request, 'main/service.html', locals())


def fitter(request):
    return render(request, 'main/fitter.html', locals())


def amenities(request):
    return render(request, 'main/amenities.html', locals())


def errors(request):
    return render(request, 'main/errors.html', locals())


def DIREPAIR(request):
    return render(request, 'main/DIREPAIR.html', locals())


def CTREET(request):
    return render(request, 'main/CTREET.html', locals())


def SERVICE1(request):
    return render(request, 'main/SERVICE1.html', locals())


def abonent(request):
    return render(request, 'main/abonent.html', locals())


def executor(request):
    return render(request, 'main/executor.html', locals())


def nachislsumm(request):
    return render(request, 'main/nachislsumma.html', locals())


def paysumm(request):
    return render(request, 'main/paysumma.html', locals())


def request(request):
    return render(request, 'main/request.html', locals())

def full(request):
    return render(request, 'main/full-width.html', locals())

def side(request):
    return render(request, 'main/sidebar.html', locals())

def four(request):
    return render(request, 'main/404.html', locals())

def faq(request):
    return render(request, 'main/faq.html', locals())

def price(request):
    return render(request, 'main/price.html', locals())

def pri(request):
    return render(request, 'main/pri.html', locals())

def recep(request):
    return render(request, 'main/recep.html', locals())
