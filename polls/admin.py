from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Choice, Question, Book

'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
'''


class BookResource(resources.ModelResource):

    class Meta:
        model = Book


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Book, BookAdmin)

