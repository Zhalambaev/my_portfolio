from django.db import models

class Blog_project(models.Model):

    title_blog = models.CharField(max_length=200)
    date_blog = models.DateTimeField(auto_now=True)
    description_blog = models.TextField()
    url_blog = models.URLField(blank=True)

    def __str__(self):
        return self.title_blog

