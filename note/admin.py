from django.contrib import admin

from .models import Note, Tag, Note_Tag

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(Note_Tag)
