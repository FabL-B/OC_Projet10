from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    """
    Serializer for the CustomUser model.

    Serializes the user's ID, username, date of birth, and consent
    preferences (contact and data sharing).
    """
    class Meta:
        model = CustomUser
        fields = ['id',
                  'username',
                  'date_of_birth',
                  'can_be_contacted',
                  'can_data_be_shared'
                  ]
