from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser, Employer, Recruiter

from .serializers_users import (CustomUserSerializer, 
                                CustomUserCreateSerializer,
                                EmployerSerializer,
                                RecruiterGetSerializer, RecruiterSerializer)


class CustomUserViewSet(UserViewSet):
    """Управление пользователями."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializer
        return CustomUserCreateSerializer

    @action(
        detail=False,
        methods=['get'],
        url_path='me',
        permission_classes=[IsAuthenticated,])
    def profile(self, request):
        """Просмотр информации о себе."""
        serializer = CustomUserSerializer(
            self.request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecruiterViewSet(viewsets.ModelViewSet):
    """Рекрутеры."""
    queryset = Recruiter.objects.all()
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', 'post',]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecruiterGetSerializer
        return RecruiterSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    """Работодатели."""
    queryset = Employer.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = EmployerSerializer
    http_method_names = ['get', 'post',]
