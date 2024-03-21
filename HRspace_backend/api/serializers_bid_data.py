from rest_framework import serializers

from bids.models import (BidRegisterAs, City, Country, EducationsOption,
                         EmployeeAddSkill, EmployeeCategory, EmployeeSkill,
                         ExperienceOption, JobVacancy, RecruiterTask,
                         RegisterAsOption, ScheduleOption, Sphere,
                         TariffOption, WorkFormat)


class JobVacancySerializer(serializers.ModelSerializer):
    """Cериализатор для списка должностей."""
    class Meta:
        fields = ('id', 'name')
        model = JobVacancy


class SphereSerializer(serializers.ModelSerializer):
    """Cериализатор для сферы деятельности."""
    class Meta:
        fields = ('id', 'name')
        model = Sphere


class ScheduleOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для графиков работы."""
    class Meta:
        fields = ('id', 'name')
        model = ScheduleOption


class WorkFormatSerializer(serializers.ModelSerializer):
    """Cериализатор для формата работы."""
    class Meta:
        fields = ('id', 'name')
        model = WorkFormat


class RegisterAsOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для типа занятости."""
    class Meta:
        fields = ('id', 'name')
        model = RegisterAsOption


class CitySerializer(serializers.ModelSerializer):
    """Cериализатор для списка городов."""
    class Meta:
        fields = ('id', 'name')
        model = City


class EmployeeCategorySerializer(serializers.ModelSerializer):
    """Cериализатор для категорий сотрудников."""
    class Meta:
        fields = ('id', 'name')
        model = EmployeeCategory


class CountrySerializer(serializers.ModelSerializer):
    """Cериализатор для типа стран."""
    class Meta:
        fields = ('id', 'name')
        model = Country


class ExperienceOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для требований к опыту работы."""
    class Meta:
        fields = ('id', 'name')
        model = ExperienceOption


class EducationsOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для требований к опыту образованию."""
    class Meta:
        fields = ('id', 'name')
        model = EducationsOption


class EmployeeSkillSerializer(serializers.ModelSerializer):
    """Cериализатор для требований."""
    class Meta:
        fields = ('id', 'name')
        model = EmployeeSkill


class EmployeeAddSkillSerializer(serializers.ModelSerializer):
    """Cериализатор для обязанностей."""
    class Meta:
        fields = ('id', 'name')
        model = EmployeeAddSkill


class TariffOptionSerializer(serializers.ModelSerializer):
    """Cериализатор для тарифов."""
    class Meta:
        fields = ('id', 'name', 'payment_for_employee_start_working',
                  'payment_for_employee_after_guarantee',
                  'guarantee_period',
                  'units_of_measurement_warranty_period')
        model = TariffOption


class RecruiterTaskSerializer(serializers.ModelSerializer):
    """Cериализатор для задач рекрутера."""
    class Meta:
        fields = ('id', 'name')
        model = RecruiterTask


class BidRegisterAsSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления способов оформления в заявку."""

    class Meta:
        model = BidRegisterAs
        fields = ('id', 'bid', 'register_as')
