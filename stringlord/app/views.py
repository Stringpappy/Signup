from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import CustomUser, Client, ServiceProvider
from .serializers import ClientSerializer, ServiceProviderSerializer, CustomUserSerializer

    
class Api_create(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            # Create user
            user = CustomUser.objects.create(
                email=data['email'],
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=make_password(data['password']),
            )

            # Create client profile
            Client.objects.create(user=user, service_needed=data['service_needed'])

            return Response({"message": "Client account created successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Api_createsp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            # Create user
            user = CustomUser.objects.create(
                email=data['email'],
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=make_password(data['password']),
            )

            # Create service provider profile
            ServiceProvider.objects.create(
                user=user,
                working_hour=data['working_hour'],
                professions=data['professions']
            )

            return Response({"message": "Service provider account created successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Api_login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful. Redirecting to profile...",
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)

class Api_profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = CustomUserSerializer(user).data

        # Check if the user is a client or service provider
        try:
            client = Client.objects.get(user=user)
            user_data['role'] = 'Client'
            user_data['service_needed'] = client.service_needed
        except Client.DoesNotExist:
            pass

        try:
            service_provider = ServiceProvider.objects.get(user=user)
            user_data['role'] = 'Service Provider'
            user_data['working_hour'] = service_provider.working_hour
            user_data['professions'] = service_provider.professions
        except ServiceProvider.DoesNotExist:
            pass

        return Response(user_data, status=status.HTTP_200_OK)


#html template 
def login(request):
    return render(request, 'app/login.html')

def cl_signup(request):
    return render(request, 'app/client_reg.html')


def profile(request):
    return render(request, 'app/profile.html')


def sp_reg(request):
    return render(request, 'app/sp_reg.html')


def base(request):
    return render(request, 'app/base.html')
