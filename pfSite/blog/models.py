from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d/%H/%M")
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def get_edit_url(self):
        return reverse('blog:post_edit', args=[self.pk])

    def get_delete_url(self):
        return reverse('blog:post_delete', args=[self.pk])


class Comment(models.Model):
    # Post : Comment = 1 : N
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def get_edit_url(self):
        return reverse('blog:comment_edit', args=[self.post.pk, self.pk])

    def get_delete_url(self):
        return reverse('blog:comment_delete', args=[self.post.pk, self.pk])
