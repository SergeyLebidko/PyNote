from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Topic
from .forms import TopicForm


# Контроллер, выводящий главную страницу
def index(request):
    topics = Topic.objects.order_by('-published')
    context = {'topics': topics}

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.creator = request.user
            new_topic.save()

    if request.user.is_authenticated:
        form = TopicForm()
        context['form'] = form

    return render(request, 'main/index.html', context)


# Контроллер, регистрирующий нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))

    if request.method == 'GET':
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'main/register.html', context)


# Контроллер входа на сайт
class LoginController(LoginView):
    template_name = 'main/login.html'


# Контроллер выхода
class LogoutController(LogoutView):
    next_page = 'index'
