from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from bids.models import (Bid, BidCountry, BidEmployeeAddSkill,
                         BidEmployeeCategory, BidEmployeeSkill,
                         BidRecruiterTask, BidRegisterAs, City, Country,
                         EducationsOption, EmployeeAddSkill, EmployeeCategory,
                         EmployeeSkill, ExperienceOption, JobVacancy,
                         RecruiterTask, RecruiterToBid,
                         RecruiterToBidAddedResume, RegisterAsOption,
                         ScheduleOption, Sphere, TariffOption, WorkFormat)
from users.models import CustomUser, Employer, Recruiter


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
        fields = '__all__'


class BidEmployeeCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для добавления в заявку категорий людей
    (студенты, инвалиды и пр)."""

    class Meta:
        model = BidEmployeeCategory
        fields = '__all__'


class BidCountrySerializer(serializers.ModelSerializer):
    """Сериализатор для добавления стран в заявку."""

    class Meta:
        model = BidCountry
        fields = '__all__'


class BidEmployeeSkillSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления требований в заявку."""

    class Meta:
        model = BidEmployeeSkill
        fields = '__all__'


class BidEmployeeAddSkillSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления обязанностей в заявку."""

    class Meta:
        model = BidEmployeeAddSkill
        fields = '__all__'


class RecruiterToBidSerializer(serializers.ModelSerializer):
    """Рекрутеры, связанные с заявкой."""
    recruiter = RecruiterSerializer()
    bid = serializers.SlugRelatedField(
        read_only=True, slug_field='title')

    class Meta:
        fields = ('id', 'recruiter', 'bid', 'status')
        model = RecruiterToBid


class RecruiterToBidAddedResumeSerializer(serializers.ModelSerializer):
    """Кандидаты, направленные рекрутером."""

    class Meta:
        fields = ('id', 'recruiter_to_bid',
                  'file', 'comment', 'accepted_at', 'status',)
        model = RecruiterToBidAddedResume


class BidRecruiterTaskSerializer(serializers.ModelSerializer):
    """Привязанные к заявке задачи рекрутера."""

    class Meta:
        fields = ('id', 'bid', 'recruiter_task',)
        model = BidRecruiterTask


class BidGetSerializer(serializers.ModelSerializer):
    """Cериализатор для просмотра заявок."""

    class Meta:
        model = Bid
        fields = ('id', 'employer', 'title',
                  'job_vacancy', 'sphere',
                  'min_salary', 'max_salary', 'schedule',
                  'schedule_comment', 'work_format',
                  'register_as_set', 'city',
                  'vhl', 'working_conditions', 'employee_categories',
                  'foreign_citizen', 'foreign_countries',
                  'employee_experience',
                  'employee_education', 'employee_skills',
                  'employee_add_skills', 'responsibilities_employee',
                  'qty_employees', 'payment_for_employee',
                  'tariff', 'qty_recruiters', 'employee_will_go_to_work_at',
                  'expected_first_cv_date',
                  'recruiter_tasks', 'resume_after_interview',
                  'not_private_person', 'skills_recruiter', 'stop_list',
                  'created_at', 'closed_at', 'status',
                  )


class BidChangeSerializer(serializers.ModelSerializer):
    """Cериализатор для создания и редактирования заявок."""
    class Meta:
        model = Bid
        fields = ('id', 'employer', 'title',
                  'job_vacancy', 'sphere',
                  'min_salary', 'max_salary', 'schedule',
                  'schedule_comment', 'work_format',
                  'register_as_set', 'city',
                  'vhl', 'working_conditions', 'employee_categories',
                  'foreign_citizen', 'foreign_countries',
                  'employee_experience',
                  'employee_education', 'employee_skills',
                  'employee_add_skills', 'responsibilities_employee',
                  'qty_employees', 'payment_for_employee',
                  'tariff', 'qty_recruiters', 'employee_will_go_to_work_at',
                  'expected_first_cv_date',
                  'recruiter_tasks', 'resume_after_interview',
                  'not_private_person', 'skills_recruiter', 'stop_list',
                  'created_at', 'closed_at', 'status',
                  )
