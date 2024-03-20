from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

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


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""
    photo = Base64ImageField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'full_name', 'photo',
                  'role', 'created_at')

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'photo',
                  'password')


class RecruiterSerializer(serializers.ModelSerializer):
    """Cериализатор для рекрутеров."""
    class Meta:
        model = Recruiter
        fields = ('id', 'user', 'top10', 'finished_cases',
                  'years_of_exp', 'about_me')


class EmployerSerializer(serializers.ModelSerializer):
    """Cериализатор для работодателей."""

    class Meta:
        model = Employer
        fields = ('id', 'user', 'company', 'position')


class JobVacancySerializer(serializers.ModelSerializer):
    """Cериализатор для списка должностей."""
    class Meta:
        fields = ('id', 'name')
        model = JobVacancy


class SphereSerializer(serializers.ModelSerializer):
    """Cериализатор для сферы деятельности."""
    class Meta:
        fields = ('id', 'name')
        model = JobVacancy


class CitySerializer(serializers.ModelSerializer):
    """Cериализатор для списка городов."""
    class Meta:
        fields = ('id', 'name')
        model = JobVacancy


class ScheduleOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для графиков работы."""
    class Meta:
        fields = ('id', 'name')
        model = JobVacancy


class WorkFormatSerializer(serializers.ModelSerializer):
    """Cериализатор для формата работы."""
    class Meta:
        fields = ('id', 'name')
        model = WorkFormat
