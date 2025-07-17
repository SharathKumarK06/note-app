from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32, default="uncategorized", unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.CharField(max_length=256, blank=True, null=True)
    tags = models.ManyToManyField(Tag, through="Note_Tag")
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["modification_time"]

    def __str__(self):
        return self.title

class Note_Tag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.ForeignKey(
            Tag, on_delete=models.CASCADE,
            blank=True, null=True
            )
