from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet


router = routers.SimpleRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path(
        'projects/<int:project_pk>/issues/<int:issue_pk>/',
        include(router.urls)
    )
]
