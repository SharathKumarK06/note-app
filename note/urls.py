from django.urls import path

from . import views

urlpatterns = [
    # Read
    # List all notes
    path("", views.note_list, name="note_list"),
    # Show one note
    path("<int:note_id>/", views.note_item, name="note_item"),
]
