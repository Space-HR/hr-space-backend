from rest_framework import serializers

from bids.models import (
    RecruiterToBid, Bid,
    RecruiterToBidAddedResume,
    EmployeeAddSkill,
    )

from .serializers_users import RecruiterSerializer, EmployerSerializer
from .serializers_bid_data import EmployeeAddSkillSerializer


class RecruiterToBidAddedResumeSerializer(serializers.ModelSerializer):
    """Просмотр кандидатов, прикрепленных к заявке."""

    recruiter_to_bid = serializers.IntegerField(source='recruiter_to_bid.id')

    class Meta:
        fields = ('id', 'recruiter_to_bid',
                  'file', 'comment', 'accepted_at', 'status',)
        model = RecruiterToBidAddedResume


class RecruiterToBidAddedResumeSerializer(serializers.ModelSerializer):
    """Прикрепление рекрутера к заявке."""

    class Meta:
        fields = ('id', 'recruiter_to_bid',
                  'file', 'comment', 'accepted_at', 'status',)
        model = RecruiterToBidAddedResume


class RecruiterToBidSerializer(serializers.ModelSerializer):
    """Просмотр рекрутеров, связанных с заявкой."""

    recruiter = RecruiterSerializer()
    bid = serializers.SlugRelatedField(
        read_only=True, slug_field='title')
    candidates = RecruiterToBidAddedResumeSerializer(
        many=True,
        read_only=True,
        source='cvtorecruiter')

    class Meta:
        fields = ('id', 'recruiter', 'bid',
                  'status', 'candidates')
        model = RecruiterToBid


class RecruiterToBidCreateSerializer(serializers.ModelSerializer):
    """Присоединение рекрутера к заявке."""
    recruiter = serializers.IntegerField(source='recruiter.id')
    bid = serializers.SlugRelatedField(
        read_only=True, slug_field='title')

    class Meta:
        fields = ('id', 'recruiter', 'bid',
                  'status', )
        model = RecruiterToBid


class BidGetSerializer(serializers.ModelSerializer):
    """Cериализатор для просмотра заявок. Получение
    полной информации по всем полям(вместе с рекрутерами
    и направленными на рассмотрение кандидатами)."""

    employer = EmployerSerializer()
    job_vacancy = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    sphere = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    schedule = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    work_formats = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    register_as_set = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    city = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    employee_categories = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    foreign_countries = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    employee_experience = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    employee_education = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    employee_skills = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    employee_add_skills = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    tariff = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    recruiter_tasks = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many=True
    )
    recruiters = RecruiterToBidSerializer(many=True,
                                          read_only=True,
                                          source='recruitertobid')

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
                  'recruiters',
                  )


class BidChangeSerializer(serializers.ModelSerializer):
    """Cериализатор для создания и редактирования заявок."""

    # employee_add_skills = EmployeeAddSkillSerializer(many=True)

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
