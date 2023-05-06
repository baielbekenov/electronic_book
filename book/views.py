from http.client import HTTPResponse

import generics as generics
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from book.forms import CreateCategoryForm
from book.models import User


def index(request):
    queryset = User.objects.all()
    context = {'queryset': queryset}
    return render(request, 'index.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, 'create_category.html', context)
    return HttpResponse('error')
