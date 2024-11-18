from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewset(ModelViewSet):

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
