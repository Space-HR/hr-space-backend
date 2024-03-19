from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser, Employer, Recruiter

from .serializers import (CustomUserSerializer, EmployerSerializer,
                          RecruiterSerializer)


class CustomUserViewSet(UserViewSet):
    """Управление пользователями."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = CustomUserSerializer
    http_method_names = ['get',]

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
    serializer_class = RecruiterSerializer
    http_method_names = ['get', 'post',]


class EmployerViewSet(viewsets.ModelViewSet):
    """Рекрутеры."""
    queryset = Employer.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = EmployerSerializer
    http_method_names = ['get', 'post',]
