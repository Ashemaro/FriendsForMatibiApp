from django.views import generic
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from .models import NewsArticles, VisitCounter, NookHubArticles


class News(generic.TemplateView):
 # Optional, specifies the name of a GET field with the URL to redirect to after login

    def get(self, request):
        news_posts = NewsArticles.objects.filter(status=1)

        context = self.get_context_data()
        context.update({'news_posts': news_posts})
        paginator = Paginator(news_posts, 10)  # Show 10 news articles per page
        page_number = request.GET.get('page')  # Get the current page number from the request
        page_obj = paginator.get_page(page_number)  # Get the articles for the current page
        return render(request, 'news.html', context)

class index(generic.TemplateView):
    def get(self, request):
        news_posts = NewsArticles.objects.filter(status=1)

        context = self.get_context_data()
        context.update({'news_posts': news_posts})
        return render(request, "index.html", context)


class NewsDetail(generic.DetailView):
    model = NewsArticles
    template_name = 'news_details.html'

class NookHub(generic.TemplateView):
 # Optional, specifies the name of a GET field with the URL to redirect to after login

    def get(self, request):
        nookHub_posts = NookHubArticles.objects.filter(status=1)

        context = self.get_context_data()
        context.update({'nookHub_posts': nookHub_posts})
        paginator = Paginator(nookHub_posts, 10)  # Show 10 news articles per page
        page_number = request.GET.get('page')  # Get the current page number from the request
        page_obj = paginator.get_page(page_number)  # Get the articles for the current page
        return render(request, 'nookhub.html', context)

class NookHubDetail(generic.DetailView):
    model = NookHubArticles
    template_name = 'nookhub_details.html'


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def runningprojects(request):
    return render(request, 'runningprojects.html')


def projectstofund(request):
    return render(request, 'projectstofund.html')


def completedprojects(request):
    return render(request, 'completedprojects.html')

