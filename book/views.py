from django.shortcuts import render

from book.models import User


def index(request):
    queryset = User.objects.all()
    context = {'queryset': queryset}
    return render(request, 'index.html', context)