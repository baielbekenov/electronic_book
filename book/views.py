from http.client import HTTPResponse

import generics as generics
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView

from book.forms import CreateCategoryForm, CreateLessonForm
from book.models import User, Category, Lesson


def base(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'base.html', context)


def index(request, pk):
    lessons = Lesson.objects.all().filter(category_id=pk)
    context = {'lessons': lessons}
    return render(request, 'index.html', context)


def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    context = {'lesson': lesson}
    return render(request, 'lesson_detail.html', context)


def create_category(request):
    form = CreateCategoryForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'create_category.html', context)


def create_lesson(request):
    form = CreateLessonForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'create_lesson.html', context)


class Search(ListView):
    paginated_by = 3
    template_name = 'lesson_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Lesson.objects.filter(Q(name__icontains=query))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


