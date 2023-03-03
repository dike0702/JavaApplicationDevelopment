from . import views
from django.urls import path
from application import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name ='top'),
    #path('', views.ReviewView.as_view(), name ='top'),
    #path('', views.ReviewView.as_view(), name ='top'),
    path('restaurant/<name>', views.ItemDetailView.as_view(), name='restaurant'),
    # path('restaurant/<name>', views.ReviewView.as_view()),
    # path('review/', views.Review.as_view(), name = 'review'),
    # path('home/', views.HomeView.as_view(), name = 'home'),
    # path('login/', views.LoginView.as_view(), name = 'login'),
    # path('logout/', views.LogoutView.as_view(), name = 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)