from django.urls import path, include
from rest_framework import routers
 
from .views import ContributorViewSet
 

router = routers.SimpleRouter()
router.register(r'', ContributorViewSet, basename='contributors')
 
urlpatterns = [
    path('projects/<int:project_pk>/contributors/', include(router.urls))
]
