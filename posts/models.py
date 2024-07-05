from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="標題")
    content = models.TextField(verbose_name="內文")
    slug = models.SlugField(blank=True, unique=True, verbose_name="網址別名")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
