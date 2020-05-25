
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewSets

router = DefaultRouter()
router.register(r'post', PostViewSets)
urlpatterns = [
    path("", include(router.urls)),
]