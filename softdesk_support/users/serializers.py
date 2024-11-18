from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'date_of_birth',
                  'can_be_contacted',
                  'can_data_be_shared'
                  ]
