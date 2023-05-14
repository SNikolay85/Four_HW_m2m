from django.contrib import admin

from .models import Article, Tag, Scope


class ScopeInLine(admin.TabularInline):
    model = Scope
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag', 'is_main']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    #list_display = ['id', 'is_main']
    inlines = [ScopeInLine]
