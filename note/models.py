from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, default="Uncategorized")


class Note(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="notes")

    class Meta:
        ordering = ['-last_modified']

    def __str__(self):
        return f"{self.title}\n{self.content}"
