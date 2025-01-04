from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Enter the title for your blog post')
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    body = models.TextField(help_text='Enter the content for your blog post')

    def __str__(self):
        return self.title