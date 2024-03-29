from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Entry, Topic
from .forms import EntryForm, TopicForm


# Контроллер, выводящий список сообщений
def entry_list_controller(request):
    # Получаем тему, сообщения которой надо вывести
    try:
        selected_topic = Topic.objects.get(pk=request.GET['topic_id'])
    except:
        selected_topic = None

    # Если пришли данные от формы ввода нового сообщения, то проверяем и сохраняем его
    if request.method == 'POST' and selected_topic is not None:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.creator = request.user
            new_entry.topic = selected_topic
            new_entry.save()

    # Получаем список сообщений по теме
    entries = []
    if selected_topic is not None:
        entries = Entry.objects.filter(topic=selected_topic).order_by('-published')
    context = {'entries': entries, 'selected_topic': selected_topic}

    # Если список сообщений запрошен залогинившимся пользователем, то выводим форму для ввода нового сообщения
    if request.user.is_authenticated and selected_topic is not None:
        form = EntryForm()
        context['form'] = form

    return render(request, 'main/entry_list.html', context)


# Контроллер, выводящий список тем
def topic_list_controller(request):
    # Если пришли данные от формы ввода новой темы, то проверяем и сохраняем её
    if request.method == 'POST' and request.user.is_authenticated:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.creator = request.user
            new_topic.save()

    # Получаем список тем и добавляем его в контекст
    topics = Topic.objects.order_by('-published')
    context = {'topics': topics}

    # Получаем количество сообщений по каждой теме и добавляем его в контекст
    entry_counts = {}
    for tc in topics:
        entry_count = Entry.objects.filter(topic=tc).count()
        entry_counts[tc.pk] = entry_count
    context['entry_counts'] = entry_counts

    # Если список тем запрошен залогинившимся пользователем, то выводим форму для ввода новой темы
    if request.user.is_authenticated:
        form = TopicForm()
        context['form'] = form

    return render(request, 'main/topic_list.html', context)


# Контроллер, удаляющий тему
def remove_topic_controller(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('topic_list'))

    # Получаем тему, которую надо удалить. Если это не удалось, то переходим к странице аккаунта
    try:
        selected_topic = Topic.objects.get(pk=request.GET['topic_id'])
    except:
        return HttpResponseRedirect(reverse('account'))

    # Удаляем тему и переходим к странице аккаунта
    selected_topic.delete()
    return HttpResponseRedirect(reverse('account'))


# Контроллер, выводящий информацию о пользователе
def account_controller(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('topic_list'))

    # Получаем список тем, созданных пользователем
    topics = Topic.objects.filter(creator=request.user).order_by('-published')
    topics_count = topics.count()
    context = {'topics': topics, 'topics_count': topics_count}

    # Получаем количество сообщений, оставленных пользователем
    entry_counts = Entry.objects.filter(creator=request.user).count()
    context['entry_counts'] = entry_counts

    return render(request, 'main/account.html', context)


# Контроллер, регистрирующий нового пользователя
def user_register_controller(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('topic_list'))

    if request.method == 'GET':
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'main/register.html', context)


# Контроллер входа на сайт
class LoginController(LoginView):
    template_name = 'main/login.html'


# Контроллер смены пароля
class ChangePasswordController(PasswordChangeView):
    template_name = 'main/change_password.html'
    success_url = reverse_lazy('password_change_done')


# Контроллер, выводящий страницу с уведомлением об успешной смене пароля
class PasswordChangeDoneController(PasswordChangeDoneView):
    template_name = 'main/password_change_done.html'


# Контроллер выхода
class LogoutController(LogoutView):
    next_page = reverse_lazy('topic_list')
