
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import UserRegistrationForm, LoginForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import auth


def home(request):
    """Отображение главное страницы"""
    try:
        return render(request, "country/home.html")
    except:
        return HttpResponseNotFound



def show_cities(request, region_id):
    """Отображение списка городов по областям"""
    try:
        region = Region.objects.get(pk=region_id)
        cities = region.cities_set.all()
        context = {
            'cities': cities,
        }
        return render(request, "country/show_cities.html", context=context)
    except:
        return HttpResponseNotFound("Page not found")


def show_routers(request):
    """список маршрутов"""
    try:
        routers = Routers.objects.all()
        context = {'routers':routers}
        return render(request, "country/routers.html", context=context)
    except:
        return HttpResponseNotFound("Page not found")


def events_list(request):
    """список событий"""
    try:
        event = Events.objects.all()
        context = {'events':event}
        return render(request, "country/events_list.html", context=context)
    except:
        return HttpResponseNotFound("Page not found")


def show_photos(request):
    """списко рубрики фото"""
    try:
        posts = Photos.objects.all()
        context = {'posts':posts}
        return render(request, 'country/photos.html', context)
    except:
        return HttpResponseNotFound("Page not found")


def show_city_info(request, city_id):
    """вывод инфы о каждом городе"""
    try:
        city_info = Cities.objects.all()
        city = Cities.objects.get(pk=city_id)
        comm = city.comments.all()
        transport = city.transport_set.all()
        hotels = city.hotels_set.all()
        culturalobjects = city.culturalobjects_set.all()
        food = city.food_set.all()
        shopping = city.shopping_set.all()
        context = {
                    'city': city,
                    'transport': transport,
                    'hotel': hotels,
                    'cultural_objects': culturalobjects,
                    'food': food, 
                    'shopping': shopping,
                    'city_info': city_info,
                    'commetns': comm

                }
        return render(request, 'country/content_city.html', context)
    except:
        return HttpResponseNotFound("Page not found")


def show_route(request, route_id):
    """Вывод инфы о каждом маршруте"""
    try:
        route_desc = Routers.objects.get(pk=route_id)
        route = Routers.objects.get(pk=route_id)
        router = route.routers.all()
        context = {
            'route':router,
            'desc': route_desc
        }
        return render(request, 'country/route_info.html', context=context)
    except:
        return HttpResponseNotFound("Page not found")


def show_event(request, event_id):
    """Вывод инфы о каждом событии"""
    try:
        events = Events.objects.get(pk=event_id)
        event = events.events.all()
        context = {
            'event':event,
        
        }
        return render(request, 'country/event_info.html', context=context)
    except:
        return HttpResponseNotFound("Page not found")


def show_photos_info(request, photo_id):
    """Вывод Фотографий"""
    try:
        photos = Photos.objects.get(pk=photo_id)
        photo = photos.photos.all()

        context = {
            'photo': photo,
        
        }
        return render(request, 'country/photos_info.html', context=context)
    except:
        return HttpResponseNotFound("Page not found")


def register(request):
    """Регистрация пользователей"""
    context = {}
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return render(request, 'country/register.html', {'new_user': new_user})
    else: 
        form = UserRegistrationForm()
        context['form'] = form
    return render(request, 'country/register.html', context)


def user_login(request):
    """Авторизация пользователей"""
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Неверный логин или пароль')        
    else:
        forms = LoginForm()
    return render(request, 'country/login.html', {'form': forms})

def logout_user(request):
    logout(request)
    return redirect('home')


def add_comments(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comments = comment_form.save(commit=False)
            post_id = request.POST.get('post_id')
            post = Cities.objects.get(id=post_id)
            new_comments.post = post
            new_comments.save()
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'country/comments.html', {'comments_form':comment_form})

