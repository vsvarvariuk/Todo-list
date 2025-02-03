from django.db import models

from django.db import models

class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

class Tag(models.Model):
    name = models.CharField(max_length=255)
