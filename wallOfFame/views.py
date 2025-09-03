from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Buddies! Welcome to the wall of fame app.")


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@api_view(['POST'])
def signup(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=user.username, password=password)
    if user:
        return Response({"message": "Login successful"})
    else:
        return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
