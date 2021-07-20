from django.db import models

# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
