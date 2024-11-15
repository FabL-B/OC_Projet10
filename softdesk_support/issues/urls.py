
from django.urls import path, include
from rest_framework import routers
 
from .views import IssueViewSet
 

router = routers.SimpleRouter()
router.register(r'', IssueViewSet, basename='issues')
 
urlpatterns = [
    path('projects/<int:project_pk>/issues/', include(router.urls))
]
