from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Entry, Topic
from .forms import EntryForm


# Контроллер, выводящий список сообщений
def entry_list_controller(request):
    # Получаем тему, сообщения которой надо вывести
    try:
        selected_topic = Topic.objects.get(pk=request.GET['topic_id'])
        entries = Entry.objects.filter(topic=selected_topic).order_by('-published')
    except:
        # Если тему получить не удалось, то список сообщений делаем пустым
        entries = []
    context = {'entries': entries}

    # Если пришли данные от формы ввода нового сообщения, то проверяем и сохраняем его
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.creator = request.user
            new_topic.save()

    # Если список сообщений запрошен залогинившимся пользователем, то выводим форму для ввода нового сообщения
    if request.user.is_authenticated:
        form = EntryForm()
        context['form'] = form

    return render(request, 'main/entry_list.html', context)


# Контроллер, выводящий список тем
def topic_list_controller(request):
    # Получаем список тем
    topics = Topic.objects.order_by('-published')
    context = {'topics': topics}

    # Получаем количество сообщений по каждой теме
    entry_counts = {}
    for tc in topics:
        entry_count = Entry.objects.filter(topic=tc).count()
        entry_counts[tc.pk] = entry_count
    context['entry_counts'] = entry_counts

    return render(request, 'main/topic_list.html', context)


# Контроллер, регистрирующий нового пользователя
def user_register_controller(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('entry_list'))

    if request.method == 'GET':
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'main/register.html', context)


# Контроллер входа на сайт
class LoginController(LoginView):
    template_name = 'main/login.html'


# Контроллер выхода
class LogoutController(LogoutView):
    next_page = 'entry_list'
