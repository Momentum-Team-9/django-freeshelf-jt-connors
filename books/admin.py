from django.contrib import admin
from .models import Book, User, Category

# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
