from django.urls import path, include
from rest_framework import routers
 
from .views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet
 

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'contributors', ContributorViewSet, basename='contributors')
router.register(r'issues', IssueViewSet, basename='issues')
router.register(r'comments', CommentViewSet, basename='comments')
 
urlpatterns = [
    path('', include(router.urls))
]