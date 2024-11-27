from django.urls import path, include
from rest_framework import routers

from .views import ProjectListViewSet, ProjectDetailViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectListViewSet, basename='project-list')

urlpatterns = [
    path('', include(router.urls))
]
