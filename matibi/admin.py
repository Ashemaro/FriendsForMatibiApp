from django.contrib import admin
from matibi import models

# Register your models here.
admin.site.register(models.NewsArticles)
admin.site.register(models.NookHubArticles)
admin.site.register(models.ContactMessage)
admin.site.register(models.VisitCounter)