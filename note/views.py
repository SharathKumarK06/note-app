from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Note, Note_Tag, Tag
from .forms import NoteForm

# Read
def note_list(request):
    notes_list = Note.objects.all()
    context = { "notes_list": notes_list }
    return render(request, "note/list.html", context)

# Read note with 'note_id'
def note_item(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    tags_ids = list(Note_Tag.objects.filter(note_id=note_id)
            .values_list('tag_id', flat=True))
    tags = Tag.objects.filter(id__in=tags_ids)
    context = { "note": note, "tags": tags }
    return render(request, "note/note.html", context)


