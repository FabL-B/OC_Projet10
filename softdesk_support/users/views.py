from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewset(ModelViewSet):
    """
    ViewSet for managing CustomUser instances.

    Provides functionality to list, retrieve, create, update, and delete users.
    """
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
