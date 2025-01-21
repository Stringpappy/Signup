from rest_framework import serializers
from .models import CustomUser, Client, ServiceProvider

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Hash the password before saving the user
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'service_needed']
        read_only_fields = ['user']


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id', 'user', 'working_hour', 'professions']
        read_only_fields = ['user']
