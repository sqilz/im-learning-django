from django.contrib import admin
from rangoapp.models import Category, Page
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Page, PageAdmin)
admin.site.register(Category)
