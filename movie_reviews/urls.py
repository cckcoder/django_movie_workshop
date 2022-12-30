from django.contrib import admin
from django.urls import path
from movie import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home),
    path('about/', movie_views.about, name="about"),
    path('signup/', movie_views.signup, name="signup"),
]
