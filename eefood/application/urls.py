from django.urls import path

from .views import IndexView, Review

urlpatterns = [
    path('', IndexView.as_view()),
    path('review/', Review.as_view()),
]