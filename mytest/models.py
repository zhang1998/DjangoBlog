from django.db import models
from django.utils import timezone
# Create your models here.
class BlogArticles(models.Model):
    title=models.CharField(max_length=300)
    publish=models.DateTimeField(default=timezone.now)


    class Meta:
        ordering=("-publish",)
    def __str__(self):
        return self.title


class Test(models.Model):
    name = models.CharField(max_length=20)
