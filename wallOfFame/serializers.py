from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # never return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    # class Meta:
    #     model = Student
    #     fields = '__all__'
    #     extra_kwargs = {
    #         'password': {'write_only': True}  # don’t expose password in API responses
    #     }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # hashes password
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student