from django.shortcuts import render
from .models import Topic
from .forms import TopicForm


def index(request):
    topics = Topic.objects.order_by('-published')
    form = TopicForm()
    context = {'topics': topics, 'form': form}
    if request.method == 'GET':
        return render(request, 'main/index.html', context)
