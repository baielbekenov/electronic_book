from django.forms import forms, ModelForm

from book.models import Category, Lesson


class CreateCategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'image']


class CreateLessonForm(ModelForm):

    class Meta:
        model = Lesson
        fields = ['name', 'category_id', 'file', 'description']

