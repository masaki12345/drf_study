
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSets,ProfessionViewSets

router = DefaultRouter()
router.register(r'person', PersonViewSets)
router.register(r'profession', ProfessionViewSets)
urlpatterns = [
    path("", include(router.urls)),
]
