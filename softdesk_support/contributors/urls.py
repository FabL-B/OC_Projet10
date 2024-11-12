from django.urls import path, include
from rest_framework import routers
 
from .views import ContributorViewSet
 

router = routers.SimpleRouter()
router.register(r'contributors', ContributorViewSet, basename='contributors')
 
urlpatterns = [
    path('', include(router.urls))
]
