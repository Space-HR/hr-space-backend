from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

from users.models import Employer, Recruiter

User = get_user_model()


class JobVacancy(models.Model):
    """Справочник вакансий."""
    name = models.CharField('Название вакансии', max_length=250)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class Sphere(models.Model):
    """Справочник сфер деятельности."""
    name = models.CharField('Название сферы деятельности', max_length=250)

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

    def __str__(self):
        return self.name


class City(models.Model):
    """Справочник городов."""
    name = models.CharField('Название города', max_length=250)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class ScheduleOption(models.Model):
    """Виды графика работы."""
    name = models.CharField('Вид графика работы', max_length=250)

    class Meta:
        verbose_name = 'Вид графика работы'
        verbose_name_plural = 'Виды графика работы'

    def __str__(self):
        return self.name


class WorkFormat(models.Model):
    """Виды формата работы."""
    name = models.CharField('Формата работы', max_length=250)

    class Meta:
        verbose_name = 'Формат работы'
        verbose_name_plural = 'Форматы работы'

    def __str__(self):
        return self.name


class RegisterAsOption(models.Model):
    """Способ оформления сотрудника."""
    name = models.CharField('Способ оформления сотрудника', max_length=250)

    class Meta:
        verbose_name = 'Способ оформления сотрудника'
        verbose_name_plural = 'Способы оформления сотрудника'

    def __str__(self):
        return self.name


class Country(models.Model):
    """Справочник стран."""
    name = models.CharField('Название страны', max_length=250)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class EmployeeCategory(models.Model):
    """Справочник особых категорий граждан."""
    name = models.CharField('Название категории граждан', max_length=250)

    class Meta:
        verbose_name = 'Категория граждан'
        verbose_name_plural = 'Категории граждан'

    def __str__(self):
        return self.name


class ExperienceOption(models.Model):
    """Модель требования к опыту работы."""
    name = models.CharField('Требование к опыту работы', max_length=150)

    class Meta:
        verbose_name = 'Требование к опыту работы'
        verbose_name_plural = 'Требования к опыту работы'

    def __str__(self):
        return self.name


class EducationsOption(models.Model):
    """Модель требования к образованию."""
    name = models.CharField('Требование к образованию', max_length=150)

    class Meta:
        verbose_name = 'Требование к образованию'
        verbose_name_plural = 'Требования к образованию'

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    """Справочник навыков соискателя"""
    name = models.CharField('Навык соискателя', max_length=150)

    class Meta:
        verbose_name = 'Навык соискателя'
        verbose_name_plural = 'Навыки соискателя'

    def __str__(self):
        return self.name


class EmployeeAddSkill(models.Model):
    """Добавленные навыки соискателя(неотредактированные)."""
    name = models.CharField('Дополнительный навык соискателя', max_length=150)

    class Meta:
        verbose_name = 'Дополнительный навык соискателя'
        verbose_name_plural = 'Дополнительные навыки соискателя'

    def __str__(self):
        return self.name


class TariffOption(models.Model):
    """Модель тарифа."""
    DAY = 'day'
    MONTH = 'month'
    YEAR = 'year'
    UNIT = (
        (DAY, 'day'),
        (MONTH, 'month'),
        (YEAR, 'year'),
    )

    name = models.CharField('Название тарифа', max_length=150)
    description = models.CharField('Описание тарифа', max_length=250)
    payment_for_employee_start_working = models.PositiveSmallIntegerField(
        verbose_name='Процент оплаты за выход сотрудника'
    )
    payment_for_employee_after_guarantee = models.PositiveSmallIntegerField(
        verbose_name='Процент оплаты после гарантийного периода'
    )
    guarantee_period = models.PositiveSmallIntegerField()
    units_of_measurement_warranty_period = models.CharField(
        max_length=16, choices=UNIT, default=DAY)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class RecruiterTask(models.Model):
    """Модель задачи рекрутера."""
    name = models.CharField('Задача рекрутера', max_length=150)

    class Meta:
        verbose_name = 'Задача рекрутера'
        verbose_name_plural = 'Задачи рекрутера'

    def __str__(self):
        return self.name


class Bid(models.Model):
    """Модель заявки."""
    QTY_EMPLOYEES_MIN = 1
    QTY_EMPLOYEES_MAX = 10
    DRAFT = 'draft'
    MODERATION = 'moderation'
    PUBLISHED = 'published'
    AT_WORK = 'at_work'
    CLOSED = 'closed'
    CANCELED = 'canceled'
    STATUS_BID = (
        (DRAFT, 'draft'),
        (MODERATION, 'moderation'),
        (PUBLISHED, 'published'),
        (AT_WORK, 'at_work'),
        (CLOSED, 'closed'),
        (CANCELED, 'canceled'),
    )

    employer = models.ForeignKey(
        Employer,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='Автор заявки',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название заявки',
    )
    job_vacancy = models.ForeignKey(
        JobVacancy,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='ID вакансии',
        default=1
    )
    sphere = models.ForeignKey(
        Sphere,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='ID сферы деятельности',
        default=1
    )
    min_salary = models.PositiveIntegerField(
        verbose_name='Минимальная зарплата',
        null=True, blank=True,
    )
    max_salary = models.PositiveIntegerField(
        verbose_name='Максимальная зарплата',   # Добавить валидацию: min_salary < max_salary
        null=True, blank=True,
    )
    schedule = models.ForeignKey(
        ScheduleOption,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='ID опции графика работы',
        null=True, blank=True,
    )
    schedule_comment = models.CharField(
        max_length=200,
        verbose_name='Комментарий к графику работы',
        blank=True
    )
    work_formats = models.ManyToManyField(
        WorkFormat,
        related_name='bids',
        blank=True,
        verbose_name='Форматы работы',
    )
    register_as_set = models.ManyToManyField(  # Если поле обязательное, то надо определить default
        RegisterAsOption,
        related_name='bids',
        blank=True,
        verbose_name='Оформление сотрудника',
    )
    city = models.ForeignKey(
        City,
        on_delete=CASCADE,
        related_name='bids',
        null=True, blank=True,
        verbose_name='ID города',
    )
    vhl = models.BooleanField(
        default=False,
        verbose_name='Добровольное медицинское страхование'
    )
    foreign_citizen = models.BooleanField(
        default=False,
        verbose_name='Иностранные граждане'
    )
    foreign_countries = models.ManyToManyField(
        Country,
        related_name='bids',
        blank=True,
        verbose_name='Граждане каких стран принимаются на работу',
    )
    employee_categories = models.ManyToManyField(
        EmployeeCategory,
        related_name='bids',
        blank=True,
        verbose_name='Дополнительные категории граждан',
    )
    working_conditions = models.TextField(
        verbose_name='Описание дополнительных условий работы',
        blank=True,
    )
    employee_experience = models.ForeignKey(
        ExperienceOption,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='ID требования к опыту работы',
        null=True, blank=True,
    )
    employee_education = models.ForeignKey(
        EducationsOption,
        on_delete=CASCADE,
        related_name='bids',
        null=True, blank=True,
        verbose_name='ID требования к образованию',
    )
    employee_skills = models.ManyToManyField(  # то, что увидел в подсказках в поле требования
        EmployeeSkill,
        related_name='bids',
        blank=True,
        verbose_name='Навыки',
    )
    employee_add_skills = models.ManyToManyField(  # то, что дописал руками в поле требования
        EmployeeAddSkill,
        related_name='bids',
        blank=True,
        verbose_name='Дополнительные навыки',
    )
    responsibilities_employee = models.TextField(
        verbose_name='Описание обязонностей сотрудника',
        blank=True,
    )
    qty_employees = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(QTY_EMPLOYEES_MIN),
            MaxValueValidator(QTY_EMPLOYEES_MAX),
        ],
        verbose_name='Количество сотрудников',
        default=1,
    )
    payment_for_employee = models.PositiveIntegerField(
        verbose_name='Вознаграждение за сотрудника',
        default=0
    )
    tariff = models.ForeignKey(
        TariffOption,
        on_delete=CASCADE,
        related_name='bids',
        verbose_name='ID тарифа',
        default=1
    )
    qty_recruiters = models.PositiveSmallIntegerField(
        verbose_name='Допустипое количество рекрутеров',
        default=1
    )
    employee_will_go_to_work_at = models.DateField(
        verbose_name='Желаемая дата выхода сотрудника',
        null=True, blank=True,
    )
    expected_first_cv_date = models.DateField(
        verbose_name='Ожидаемая дата получения первых резюме',
        null=True, blank=True,
    )
    recruiter_tasks = models.ManyToManyField(
        RecruiterTask,
        related_name='bids',
        blank=True,
        verbose_name='Задачи рекрутера',
    )
    resume_after_interview = models.BooleanField(
        default=False,
        verbose_name='Предоставлять резюме после собеседования с соискателем'
    )
    not_private_person = models.BooleanField(
        default=True,
        verbose_name='Только юр. лица, ИП, самозанятые'
    )
    skills_recruiter = models.TextField(
        verbose_name='Требования (навыки) к рекрутеру',
        blank=True,
    )
    stop_list = models.TextField(
        verbose_name='Стоп-лист сотрудников',
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    closed_at = models.DateField(
        verbose_name='Дата закрытия',
        null=True, blank=True,
    )
    status = models.CharField(max_length=16, choices=STATUS_BID, default=DRAFT)


class RecruiterToBid(models.Model):
    """Модель связи заявки и рекрутера."""
    INVITE = 'invite'
    RESPONSE = 'response'
    ACCEPTED = 'accepted'
    REFUSED = 'refused'
    STATUS_RECRUITER = (
        (INVITE, 'invite'),
        (RESPONSE, 'response'),
        (ACCEPTED, 'accepted'),
        (REFUSED, 'refused'),
    )

    recruiter = models.ForeignKey(
        Recruiter,
        on_delete=CASCADE,
        verbose_name='ID рекрутера',
    )
    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
        related_name='recruitertobid',
    )
    status = models.CharField(max_length=16,
                              choices=STATUS_RECRUITER,
                              default=RESPONSE)  # default зависит кто создал

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recruiter', 'bid'],
                name='recruiter_bid'
            )
        ]
        verbose_name = 'Связь заявки и рекрутера'
        verbose_name_plural = 'Связи заявки и рекрутера'

    def __str__(self):
        return f'заявка {self.bid} -> рекрутер {self.recruiter}'


class RecruiterToBidAddedResume(models.Model):
    """Модель связи рекрутера по конкретной заявке и резюме."""
    NEW = 'new'
    TO_INTERVIEW = 'to_interview'
    ACCEPTED = 'accepted'
    CANCELED = 'canceled'
    STATUS_RESUME = (
        (NEW, 'new'),
        (TO_INTERVIEW, 'to_interview'),
        (ACCEPTED, 'accepted'),
        (CANCELED, 'canceled'),
    )
    recruiter_to_bid = models.ForeignKey(
        RecruiterToBid,
        on_delete=CASCADE,
        related_name='cvtorecruiter',
        verbose_name='ID связи заявки и рекрутера',
    )
    file = models.FileField(
        upload_to='uploads/resumes/',
        blank=False,
        help_text='Загрузите резюме',
        verbose_name='Файл с резюме',
    )
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий к резюме'
    )
    accepted_at = models.DateTimeField(
        verbose_name='Кандидат одобрен',
        null=True, blank=True,)
    status = models.CharField(max_length=16,
                              choices=STATUS_RESUME,
                              default=NEW)

    class Meta:
        verbose_name = 'Добавленные к заявке кандидаты'
        verbose_name_plural = 'Добавленные к заявке кандидаты'

    def __str__(self):
        return f'резюме к {self.recruiter_to_bid}'
