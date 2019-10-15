from django.shortcuts import render
from .models import Topic


def index(request):
    topics = Topic.objects.order_by('-published')
    context = {'topics': topics}
    return render(request, 'main/index.html', context)
