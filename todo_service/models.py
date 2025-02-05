from django.db import models

class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    class Meta:
        ordering = ["is_done", "datetime"]

    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
