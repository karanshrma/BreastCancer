from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('allusers/', views.allusers, name="allusers"),
    path('allpatients/', views.allpatients, name="allpatients"),
    path('about/', views.about, name="about"),
            path('signup/', views.signup_view, name="signup"),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
