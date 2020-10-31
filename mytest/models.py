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
class IP(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    idc = models.CharField(max_length=30, null=True, blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20, default='linux', verbose_name='Operating System')

    def __unicode__(self):
        return self.hostname
