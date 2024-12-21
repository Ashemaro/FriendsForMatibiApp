from django.contrib import admin
from .models import NewsArticlePage


# Register your models here.
#admin.site.register(models.NewsArticlePage)
#admin.site.register(models.NookHubArticles)
#admin.site.register(models.ContactMessage)
#admin.site.register(models.VisitCounter)

@admin.register(NewsArticlePage)
class NewsArticlePageAdmin(admin.ModelAdmin):
    exclude = ('created_on', 'updated_on')
