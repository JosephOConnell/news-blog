from django.contrib import admin
from .models import News
from django_summernote.admin import SummernoteModelAdmin


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)