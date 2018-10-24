from django.db import models

# All the data is being handeled here. being divided by its varius properties,
# each with its uniqe trait.

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)

    slug = models.SlugField() # a slug field is being used in order to specify each thread in the blog later on
    body = models.TextField() # the body of the thread that is being posted
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",blank=True)
    # add in author later

    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] +'...'  # a limitaion of 50 letters that are being shown from each thread
        #later on, thumbnail and author
