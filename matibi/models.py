from django.db import models
from django.contrib.auth.models import User

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images.models import Image
from wagtail.admin.panels import FieldPanel

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class NewsArticlePage(Page):
    # Adding Wagtail-specific fields
    article_title = models.CharField(max_length=200, unique=True)
    article_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    content = RichTextField()  # Wagtail's RichTextField to allow rich text formatting
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    # This is the class's meta information for ordering
    class Meta:
        ordering = ['-created_on']

    # For Wagtail to correctly display the page in the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('author'),
        FieldPanel('status'),
        FieldPanel('image'),
        FieldPanel('content'),
    ]

    # Optionally, you can also define settings for your page
    def __str__(self):
        return self.title


class NookHubArticles(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nookhub_articles')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class VisitCounter(models.Model):
    count = models.IntegerField(default=0)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
