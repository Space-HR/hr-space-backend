from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny

from bids.models import (City, Country, EducationsOption, EmployeeAddSkill,
                         EmployeeCategory, EmployeeSkill, ExperienceOption,
                         JobVacancy, RecruiterTask, RegisterAsOption,
                         ScheduleOption, Sphere, TariffOption, WorkFormat)

from .serializers_bid_data import (CitySerializer, CountrySerializer,
                                   EducationsOptionSerializer,
                                   EmployeeAddSkillSerializer,
                                   EmployeeCategorySerializer,
                                   EmployeeSkillSerializer,
                                   ExperienceOptionSerializer,
                                   JobVacancySerializer,
                                   RecruiterTaskSerializer,
                                   RegisterAsOptionSerializer,
                                   ScheduleOptionSerializer, SphereSerializer,
                                   TariffOptionSerializer,
                                   WorkFormatSerializer)


class JobVacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """Должность."""
    queryset = JobVacancy.objects.all()
    serializer_class = JobVacancySerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class SphereViewSet(viewsets.ReadOnlyModelViewSet):
    """Сфера деятельности."""
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class ScheduleOptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Графики работы (сменный, 5/2 и пр)."""
    queryset = ScheduleOption.objects.all()
    serializer_class = ScheduleOptionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class WorkFormatViewSet(viewsets.ReadOnlyModelViewSet):
    """Формат работы (в офисе, удаленно)."""
    queryset = WorkFormat.objects.all()
    serializer_class = WorkFormatSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class RegisterAsOptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Способ оформления."""
    queryset = RegisterAsOption.objects.all()
    serializer_class = RegisterAsOptionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    """Города."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EmployeeCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Категория сотрудников."""
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """Города."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class ExperienceOptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Опыт работы."""
    queryset = ExperienceOption.objects.all()
    serializer_class = ExperienceOptionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EducationsOptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Образование."""
    queryset = EducationsOption.objects.all()
    serializer_class = EducationsOptionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EmployeeSkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Навыки."""
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EmployeeAddSkillViewSet(viewsets.ModelViewSet):
    """Навыки."""
    queryset = EmployeeAddSkill.objects.all()
    serializer_class = EmployeeAddSkillSerializer
    http_method_names = ['get', 'post']
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class TariffOptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Тариф."""
    queryset = TariffOption.objects.all()
    serializer_class = TariffOptionSerializer
    permission_classes = (AllowAny,)
    ordering_fields = ('id',)


class RecruiterTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """Задачи рекрутера."""
    queryset = RecruiterTask.objects.all()
    serializer_class = RecruiterTaskSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)
