from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=15)
    caption = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title
