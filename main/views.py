from django.shortcuts import render
from .models import Topic
from .forms import TopicForm


def index(request):
    topics = Topic.objects.order_by('-published')
    context = {'topics': topics}

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()

    form = TopicForm()
    context['form'] = form
    return render(request, 'main/index.html', context)
