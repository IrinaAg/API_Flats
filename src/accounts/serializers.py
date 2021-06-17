from rest_framework.serializers import (CharField, EmailField, DateField, FloatField, BooleanField,
                                        TimeField, Serializer, ModelSerializer)
from accounts.models import CustomUser


class CustomUserSelializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
