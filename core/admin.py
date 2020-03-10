from django.contrib import admin

from .models import Snippet, Tag, Library, Language

admin.site.register(Snippet)
admin.site.register(Tag)
admin.site.register(Library)
admin.site.register(Language)