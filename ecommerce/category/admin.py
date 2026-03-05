from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.Model):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('categoery_name', 'slug')

admin.site.register(Category, CategoryAdmin)