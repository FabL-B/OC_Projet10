
from django.urls import path, include
from rest_framework import routers
 
from .views import IssueViewSet
 

router = routers.SimpleRouter()
router.register(r'issues', IssueViewSet, basename='issues')
 
urlpatterns = [
    path('projects/<int:project_pk>/', include(router.urls))
]
