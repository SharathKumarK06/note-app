from django.core.management.base import BaseCommand, CommandError
from note.models import Note, Tag, Note_Tag

notes = [
    {
        "title": "Note 1",
        "content": "This is note 1.",
    },
    {
        "title": "Note 2",
        "content": "This is note 2.",
    },
    {
        "title": "Note 3",
        "content": "This is note 3.",
    },
]
notes_list = []

tags = [
    {
        "name": "tag1",
        "description": "This is tag 1.",
    },
    {
        "name": "tag2",
        "description": "This is tag 2.",
    },
]
tags_list = []

notes_tags = [
    [0, 1],
    [0],
    [],
]

notes_tags_list = []

class Command(BaseCommand):
    help = "Fill database entry for testing"

    def add_notes(self, notes):
        for note in notes:
            n = Note.objects.create(**note)
            n.save()
            notes_list.append(n)
            n = None
        self.stdout.write("Notes added successfully")

    def add_tags(self, tags):
        for tag in tags:
            t = Tag.objects.create(**tag)
            t.save()
            tags_list.append(t)
        self.stdout.write("Tags added successfully")

    def add_notes_tags(self, notes_tags, notes_list, tags_list):
        for i in range(len(notes_tags)):
            note = i
            tag = notes_tags[i]
            notes_tags_list = list(
                map(
                    lambda tag: Note_Tag.objects.create(
                        note=notes_list[note],
                        tag=tags_list[tag]
                    ).save(),
                    tag
                )
            )
        self.stdout.write("Notes_Tags added successfully")

    def handle(self, *args, **options):
        # Create notes
        self.add_notes(notes)
        # Create tags
        self.add_tags(tags)
        # Add tags to notes
        self.add_notes_tags(notes_tags, notes_list, tags_list)
