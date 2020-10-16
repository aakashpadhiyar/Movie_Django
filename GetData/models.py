from django.db import models

# Create your models here.
class MoviesList(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Video = models.URLField(max_length=200, blank=False)
    Description = models.TextField(blank=False)
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return self.Title[50]