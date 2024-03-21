from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from bids.models import (Bid, BidCountry, BidEmployeeAddSkill,
                         BidEmployeeCategory, BidEmployeeSkill,
                         BidRecruiterTask, BidRegisterAs, City, Country,
                         EducationsOption, EmployeeAddSkill, EmployeeCategory,
                         EmployeeSkill, ExperienceOption, JobVacancy,
                         RecruiterTask, RecruiterToBid,
                         RecruiterToBidAddedResume, RegisterAsOption,
                         ScheduleOption, Sphere, TariffOption, WorkFormat)
from users.models import CustomUser, Employer, Recruiter

from .serializers import (BidChangeSerializer, BidCountrySerializer,
                          BidEmployeeAddSkillSerializer,
                          BidEmployeeCategorySerializer,
                          BidEmployeeSkillSerializer, BidGetSerializer,
                          BidRecruiterTaskSerializer, BidRegisterAsSerializer,
                          CitySerializer, CountrySerializer,
                          CustomUserSerializer, EducationsOptionSerializer,
                          EmployeeAddSkillSerializer,
                          EmployeeCategorySerializer, EmployeeSkillSerializer,
                          EmployerSerializer, ExperienceOptionSerializer,
                          JobVacancySerializer, RecruiterSerializer,
                          RecruiterTaskSerializer,
                          RecruiterToBidAddedResumeSerializer,
                          RecruiterToBidSerializer, RegisterAsOptionSerializer,
                          ScheduleOptionSerializer, SphereSerializer,
                          TariffOptionSerializer, WorkFormatSerializer)


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
    filter_backends = (SearchFilter, OrderingFilter)  # ищет не по части слова
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


class ScheduleOptionViewSet(viewsets.ModelViewSet):
    """Графики работы (сменный, 5/2 и пр)."""
    queryset = ScheduleOption.objects.all()
    serializer_class = ScheduleOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class WorkFormatViewSet(viewsets.ModelViewSet):
    """Формат работы (в офисе, удаленно)."""
    queryset = WorkFormat.objects.all()
    serializer_class = WorkFormatSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class RegisterAsOptionViewSet(viewsets.ModelViewSet):
    """Способ оформления."""
    queryset = RegisterAsOption.objects.all()
    serializer_class = RegisterAsOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidRegisterAsViewSet(viewsets.ModelViewSet):
    """Способы оформления, привязанные к заявке."""
    queryset = BidRegisterAs.objects.select_related('bid')
    serializer_class = BidRegisterAsSerializer
    # permission_classes = (isowner,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class CityViewSet(viewsets.ModelViewSet):
    """Города."""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EmployeeCategoryViewSet(viewsets.ModelViewSet):
    """Категория сотрудников."""
    queryset = EmployeeCategory.objects.all()
    serializer_class = EmployeeCategorySerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidEmployeeCategoryViewSet(viewsets.ModelViewSet):
    """Категории, привязанные к заявке."""
    queryset = BidEmployeeCategory.objects.select_related('bid')
    serializer_class = BidEmployeeCategorySerializer
    # permission_classes = (isowner,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class CountryViewSet(viewsets.ModelViewSet):
    """Города."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidCountryViewSet(viewsets.ModelViewSet):
    """Страны, привязанные к заявке."""
    queryset = BidCountry.objects.select_related('bid')
    serializer_class = BidCountrySerializer
    # permission_classes = (isowner,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class ExperienceOptionViewSet(viewsets.ModelViewSet):
    """Опыт работы."""
    queryset = ExperienceOption.objects.all()
    serializer_class = ExperienceOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EducationsOptionViewSet(viewsets.ModelViewSet):
    """Образование."""
    queryset = EducationsOption.objects.all()
    serializer_class = EducationsOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class EmployeeSkillViewSet(viewsets.ModelViewSet):
    """Навыки."""
    queryset = EmployeeSkill.objects.all()
    serializer_class = EmployeeSkillSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidEmployeeSkillViewSet(viewsets.ModelViewSet):
    """навыки в заявке."""
    queryset = BidEmployeeSkill.objects.select_related('bid')
    serializer_class = BidEmployeeSkillSerializer
    # permission_classes = (isowner,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class EmployeeAddSkillViewSet(viewsets.ModelViewSet):
    """Навыки."""
    queryset = EmployeeAddSkill.objects.all()
    serializer_class = EmployeeAddSkillSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidEmployeeAddSkillViewSet(viewsets.ModelViewSet):
    """Страны, привязанные к заявке."""
    queryset = BidEmployeeAddSkill.objects.select_related('bid')
    serializer_class = BidEmployeeAddSkillSerializer
    # permission_classes = (isowner,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class TariffOptionViewSet(viewsets.ModelViewSet):
    """Тариф."""
    queryset = TariffOption.objects.all()
    serializer_class = TariffOptionSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    ordering_fields = ('id',)


class RecruiterTaskViewSet(viewsets.ModelViewSet):
    """Задачи рекрутера."""
    queryset = RecruiterTask.objects.all()
    serializer_class = RecruiterTaskSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get',]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name', 'id',)


class BidRecruiterTaskViewSet(viewsets.ModelViewSet):
    """Привязанные к заявке задачи рекрутера."""
    queryset = BidRecruiterTask.objects.all()
    serializer_class = BidRecruiterTaskSerializer
    # permission_classes = (,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class RecruiterToBidViewSet(viewsets.ModelViewSet):
    """Рекрутеры, связанные с заявкой."""
    queryset = RecruiterToBid.objects.all()
    serializer_class = RecruiterToBidSerializer
    # permission_classes = (,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class RecruiterToBidAddedResumeViewSet(viewsets.ModelViewSet):
    """направленные кандидаты."""
    queryset = RecruiterToBidAddedResume.objects.all()
    serializer_class = RecruiterToBidAddedResumeSerializer
    # permission_classes = (,)
    http_method_names = ['get', 'post', 'patch', 'delete']


class BidViewSet(viewsets.ModelViewSet):
    """Вьюсет для заявки."""

    queryset = (Bid.objects.select_related('employer'))
    # permission_classes = (IsEmployer)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BidGetSerializer
        return BidChangeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
