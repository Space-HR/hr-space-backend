from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from users.models import CustomUser, Employer, Recruiter
from bids.models import (JobVacancy, Sphere, City, ScheduleOption, WorkFormat,
                     RegisterAsOption, Country, EmployeeCategory,
                     ExperienceOption,
                     EducationsOption, EmployeeSkill, EmployeeAddSkill,
                     TariffOption, Bid, RecruiterToBid,
                     RecruiterToBidAddedResume,
                    #  BidWorkFormat, BidRegisterAs,  # &
                    #  BidCountry, BidEmployeeCategory, BidEmployeeSkill,
                    #  BidEmployeeAddSkill, BidRecruiterTask,
                     )


from .serializers import (CustomUserSerializer, EmployerSerializer,
                          RecruiterSerializer, JobVacancySerializer,
                          SphereSerializer, CitySerializer, ScheduleOptionSerializer,
                          WorkFormatSerializer)

from bids.models import (JobVacancy, Sphere, City, ScheduleOption, WorkFormat,
                     RegisterAsOption, Country, EmployeeCategory,
                     ExperienceOption,
                     EducationsOption, EmployeeSkill, EmployeeAddSkill,
                     TariffOption, Bid, RecruiterToBid,
                     RecruiterToBidAddedResume,
                    #  BidWorkFormat, BidRegisterAs,  # &
                    #  BidCountry, BidEmployeeCategory, BidEmployeeSkill,
                    #  BidEmployeeAddSkill, BidRecruiterTask,
                     )


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


class JobVacancyViewSet(viewsets.ModelViewSet):
    """Должность."""
    queryset = JobVacancy.objects.all()
    serializer_class = JobVacancySerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)  # ищет по точному совпадению, не по части слова
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class SphereViewSet(viewsets.ModelViewSet):
    """Сфера деятельности."""
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter) 
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class CityViewSet(viewsets.ModelViewSet):
    """Города."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter) 
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class ScheduleOptionViewSet(viewsets.ModelViewSet):
    """Виды графиков."""
    queryset = ScheduleOption.objects.all()
    serializer_class = ScheduleOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter) 
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class WorkFormatViewSet(viewsets.ModelViewSet):
    """Формат работы."""
    queryset = WorkFormat.objects.all()
    serializer_class = WorkFormatSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter) 
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)
