from rest_framework.viewsets import ModelViewSet
 
from users.models import CustomUser
from users.serializers import CustomUserSerializer
 
class CustomUserViewset(ModelViewSet):
 
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
