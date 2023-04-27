from django.contrib import admin
from .models import Contact, News, Company, Tag, Category, Author


class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'message', 'date')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'date', 'author')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')


class CatogoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CatogoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
