from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from accounts.pagination import CustomPagination
from accounts.serializers import UserSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        page = CustomPagination
        serializer = UserSerializer(queryset, many=True, context=self.get_serializers_context())
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        page = CustomPagination
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context=self.get_serializers_context())
        return Response(serializer.data)

    def get_serializers_context(self):
        return {'request': self.request}

    def get_permissions(self):
        permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# class RegistrationView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')
#         if username is None or email is None or password is None:
#             return Response({'error': 'Please provide username, email and password'},
#                             status=status.HTTP_400_BAD_REQUEST)
#         user = User.objects.create_user(username=username, email=email, password=password)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_200_OK)
#
#
# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class LoginViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#
#         return Response({'token': token.key}, status=status.HTTP_200_OK)

