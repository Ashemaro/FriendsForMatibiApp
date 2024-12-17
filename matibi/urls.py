from . import views
from .views import News, NookHub, index
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'matibi'

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('runningprojects/', views.runningprojects, name='runningprojects'),
    path('projectstofund/', views.projectstofund, name='projectstofund'),
    path('completedprojects/', views.completedprojects, name='completedprojects'),
    path('news/', News.as_view(), name='news'),
    path('nookhubactivities/', NookHub.as_view(), name='nookhubactivities'),
]