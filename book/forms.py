from django.forms import forms, ModelForm

from book.models import Category


class CreateCategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

