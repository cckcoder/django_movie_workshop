from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from movie import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name="home"),
    path('about/', movie_views.about, name="about"),
    path('signup/', movie_views.signup, name="signup"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
