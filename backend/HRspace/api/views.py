from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import Achievements, CustomUser, Recruiter, Skills

from .serializers import (AchievementsSerializer, CustomUserSerializer,
                          RecruiterSerializer, SkillsSerializer)


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

    def perform_create(self, serializer):
        user = get_object_or_404(CustomUser, id=self.kwargs.get('user_id'))
        serializer.save(user=user)


class SkillsViewSet(viewsets.ModelViewSet):
    """Вьюсет для навыков."""

    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = (AllowAny,)


class AchievementsViewSet(viewsets.ModelViewSet):
    """Вьюсет для достижений."""
    serializer_class = AchievementsSerializer
    queryset = Achievements.objects.all()
    http_method_names = ['get', 'post',]

    def perform_create(self, serializer):
        recruiter = get_object_or_404(Recruiter, id=self.kwargs.get('user_id'))
        serializer.save(recruiter=recruiter)
