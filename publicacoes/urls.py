from django.urls import path
from .views import all_news

urlpatterns = [
    path('all/', all_news),
]
