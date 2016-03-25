from django.db import models

# Create your models here.
from django.utils import timezone


class Review(models.Model):
    reviewer = models.ForeignKey('auth.User')
    bid = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200, default='')
    subtitle = models.CharField(max_length=200, null=True)
    authors = models.CharField(max_length=200, default='')
    score = models.IntegerField(default=0)
    comment = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)
    '''
    def update(self):
        self.updated_date = timezone.now()
        self.save()
    '''
    def __str__(self):
        return ( self.title + ' :: ' + self.comment[:100])
