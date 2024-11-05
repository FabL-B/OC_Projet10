from django.urls import path, include
from rest_framework import routers
 
from users.views import CustomUserViewset
 

router = routers.SimpleRouter()

router.register(r'', CustomUserViewset, basename='user')
 
urlpatterns = [
    path('', include(router.urls))
]