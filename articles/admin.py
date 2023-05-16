from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_main = []
        for form in self.forms:
            if form in self.deleted_forms or self._should_delete_form(form):
                continue
            if form.cleaned_data.get('is_main'):
                list_main.append(form.cleaned_data['is_main'])
        if len(list_main) > 1:
            raise ValidationError('Основным может быть только один раздел')
        if len(list_main) == 0:
            raise ValidationError('Укажите основной раздел')

        return super().clean()



class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

