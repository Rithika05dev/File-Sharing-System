from django.contrib import admin
from .models import File, FileShare

admin.site.register(File)
admin.site.register(FileShare)