# from django.contrib.auth import get_user_model
from rest_framework import serializers

from bids.models import (  # City, Country,; EducationsOption, EmployeeAddSkill,; EmployeeCategory,; EmployeeSkill, ExperienceOption, JobVacancy,; RecruiterTask, RegisterAsOption,; ScheduleOption, Sphere, TariffOption, WorkFormat,; BidWorkFormat,
    Bid, BidCountry, BidEmployeeAddSkill, BidEmployeeCategory,
    BidEmployeeSkill, BidRecruiterTask, BidRegisterAs, RecruiterToBid,
    RecruiterToBidAddedResume)

from .serializers_users import \
    RecruiterSerializer  # CustomUserSerializer,; CustomUserCreateSerializer,; EmployerSerializer,; RecruiterGetSerializer,

# from users.models import CustomUser, Employer, Recruiter


# from .serializers_bid_data import (
#                           CitySerializer, CountrySerializer,
#                           EducationsOptionSerializer,
#                           EmployeeAddSkillSerializer,
#                           EmployeeCategorySerializer,
#                           EmployeeSkillSerializer,
#                           ExperienceOptionSerializer,
#                           JobVacancySerializer,
#                           RecruiterTaskSerializer,
#                           RegisterAsOptionSerializer,
#                           ScheduleOptionSerializer, SphereSerializer,
#                           TariffOptionSerializer, WorkFormatSerializer,
#                         )
# User = get_user_model()

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


class RecruiterToBidAddedResumeSerializer(serializers.ModelSerializer):
    """Кандидаты, направленные рекрутером."""

    recruiter_to_bid = serializers.SlugRelatedField(
        read_only=True, slug_field='id')

    class Meta:
        fields = ('id', 'recruiter_to_bid',
                  'file', 'comment', 'accepted_at', 'status',)
        model = RecruiterToBidAddedResume


class RecruiterToBidSerializer(serializers.ModelSerializer):
    """Рекрутеры, связанные с заявкой."""
    recruiter = RecruiterSerializer()
    bid = serializers.SlugRelatedField(
        read_only=True, slug_field='title')

    class Meta:
        fields = ('id', 'recruiter', 'bid', 'status',)
        model = RecruiterToBid


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
                  'schedule_comment', 'work_formats',
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
                  'schedule_comment', 'work_formats',
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
