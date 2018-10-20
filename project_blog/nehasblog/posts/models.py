from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date_published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def date_pretty(self):
        return self.date_published.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]