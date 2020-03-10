from django.contrib import admin

from .models import Snippet, Tag, Library

admin.sire.register(Snippet)
admin.site.register(Tag)
admin.site.register(Library)