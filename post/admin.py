from django.contrib import admin
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created")


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostModelAdmin)
