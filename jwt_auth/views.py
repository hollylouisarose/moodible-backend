from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from .serializers import UserProfileSerializer, UserRegisterSerializer
User = get_user_model()

class RegisterView(APIView):
    '''Register User View CREATE'''
    def post(self, request):
        user_to_create = UserRegisterSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response(
                {'message': 'Registration Successful'},
                status=status.HTTP_201_CREATED
            )
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):
    ''' Login User View POST'''
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)           
        except User.DoesNotExist:
            raise PermissionDenied(detail='Unauthorized')

        if not user_to_login.check_password(password):
            raise PermissionDenied(detail='Unauthorized')

        expiry_time = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            { 'sub': user_to_login.id, 'exp': int(expiry_time.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        print('token check🍓', token)

        return Response({
            'token': token,
            'message': f'Hi there {username}'
        }, status=status.HTTP_200_OK)

class ProfileView(APIView):
    '''User Profile View GET'''
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serialized_user = UserProfileSerializer(request.user)
        print('the data', serialized_user.data)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

# todo: add ability to edit user profile
    # def put(self, request):
    #     user_to_edit = UserProfileSerializer(request.user)
    #     print('the data', user_to_edit.data)
    #     return Response({'hello': 'world'})
