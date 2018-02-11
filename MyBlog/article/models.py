from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)  # the title of the blog
    category = models.CharField(max_length = 50, blank = True)  # the main label of the blog
    tag = models.CharField(max_length = 50, blank = True)  # the sub label of the blog
    date_time = models.DateTimeField(auto_now_add = True)  # the publish time of the blog
    content = models.TextField(blank = True, null = True)  # the content of the blog
    page_views = models.IntegerField(default = 0)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://www.hutianyi.tech%s" % path

    def __str__(self):  #python3 use str
        return self.title

    class Meta: # be ordered by time
        ordering = ['-date_time']