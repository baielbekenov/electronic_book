from django.contrib import admin
from .models import User, Category, Lesson

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Lesson)