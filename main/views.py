from django.shortcuts import render
from .models import Topic
from .forms import TopicForm


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
