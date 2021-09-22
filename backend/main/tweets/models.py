from django.db import models

# Create your models here.

class Tweet(models.Model):
    subject = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.subject}'

