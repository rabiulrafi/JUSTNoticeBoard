from django.contrib import admin
from .models import *
# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'publish', 'pdf',)
    search_fields = ['title', 'department']
    ordering = ['-publish']


admin.site.register(Notice,NoticeAdmin)
