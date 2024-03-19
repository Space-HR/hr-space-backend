from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

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
    """График работы."""
    name = models.CharField('График работы', max_length=250)

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'

    def __str__(self):
        return self.name


class WorkFormat(models.Model):
    """Формат работы."""
    name = models.CharField('Форматы работы', max_length=250)

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
    """Дополнительные навыки соискателя."""
    name = models.CharField('Дополнительный навык соискателя', max_length=150)

    class Meta:
        verbose_name = 'Дополнительный навык соискателя'
        verbose_name_plural = 'Дополнительные навыки соискателя'

    def __str__(self):
        return self.name


class TariffOption(models.Model):
    """Модель тарифа."""
    UNIT = (
    )
    name = models.CharField('Название тарифа', max_length=150)
    payment_for_employee_start_working = models.PositiveSmallIntegerField(
        verbose_name='Процент оплаты за выход сотрудника'
    )
    payment_for_employee_after_guarantee = models.PositiveSmallIntegerField(
        verbose_name='Процент оплаты после гарантийного периода'
    )
    guarantee_period = models.PositiveSmallIntegerField()
    units_of_measurement_warranty_period = models.CharField(max_length=16, choices=UNIT, default='')

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
    STATUS =()

    employer = models.ForeignKey(
        User,
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
        related_name='job_vacancy',
        verbose_name='ID вакансии',
    )
    sphere = models.ForeignKey(
        Sphere,
        on_delete=CASCADE,
        related_name='sphere',
        verbose_name='ID сферы деятельности',
    )
    city = models.ForeignKey(
        City,
        on_delete=CASCADE,
        related_name='city',
        verbose_name='ID города',
    )
    min_salary = models.PositiveIntegerField(
        verbose_name='Минимальная зарплата',
    )
    max_salary = models.PositiveIntegerField(
        verbose_name='Минимальная зарплата',   # Добавить валидацию: min_salary < max_salary
    )
    schedule = models.ForeignKey(
        ScheduleOption,
        on_delete=CASCADE,
        related_name='schedule',
        verbose_name='ID опции графика работы',
    )
    schedule_comment = models.CharField(
        max_length=200,
        verbose_name='Комментарий к графику работы',
    )
    work_formats = models.ManyToManyField (
        WorkFormat,
        through='BidWorkFormat',
        through_fields=('bid', 'work_format'),
        blank=False,
        verbose_name='Форматы работы',
    )
    register_as_set = models.ManyToManyField(
        RegisterAsOption,
        through='BidRegisterAs',
        through_fields=('bid', 'work_format'),
        blank=False,
        verbose_name='Форматы работы',
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
        through='BidCountry',
        through_fields=('bid', 'country'),
        blank=False,
        verbose_name='Граждане каких стран принимаются на работу',
    )
    employee_categories = models.ManyToManyField(
        EmployeeCategory,
        through='BidEmployeeCategory',
        through_fields=('bid', 'employee_category'),
        blank=False,
        verbose_name='Дополнительные категории граждан',
    )
    working_conditions = models.TextField(
        verbose_name='Описание дополнительных условий работы',
    )
    employee_experience = models.ForeignKey(
        ExperienceOption,
        on_delete=CASCADE,
        related_name='employee_experience',
        verbose_name='ID требования к опыту работы',
    )
    employee_education = models.ForeignKey(
        EducationsOption,
        on_delete=CASCADE,
        related_name='employee_education',
        verbose_name='ID требования к образованию',
    )
    employee_skills = models.ManyToManyField(
        EmployeeSkill,
        through='BidEmployeeSkill',
        through_fields=('bid', 'employee_skill'),
        blank=False,
        verbose_name='Навыки',
    )
    employee_add_skills = models.ManyToManyField(
        EmployeeAddSkill,
        through='BidEmployeeAddSkill',
        through_fields=('bid', 'employee_add_skill'),
        blank=False,
        verbose_name='Дополнительные навыки',
    )
    responsibilities_employee = models.TextField(
        verbose_name='Описание обязонностей сотрудника',
    )
    qty_employees = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(QTY_EMPLOYEES_MIN),
            MaxValueValidator(QTY_EMPLOYEES_MAX),
        ],
        verbose_name='Количество сотрудников',
    )

    payment_for_employee = models.PositiveIntegerField(
        verbose_name='Вознаграждение за сотрудника',
    )
    tariff = models.ForeignKey(
        TariffOption,
        on_delete=CASCADE,
        related_name='tariff',
        verbose_name='ID тарифа',
    )

    qty_recruiters = models.PositiveSmallIntegerField(
        verbose_name='Допустипое количество рекрутеров',
    )
    employee_will_go_to_work_at = models.DateTimeField(
        verbose_name='Желаемая дата выхода сотрудника',
    )

    recruiter_tasks = models.ManyToManyField(
        RecruiterTask,
        through='BidRecruiterTask',
        through_fields=('bid', 'employee_add_skill'),
        blank=False,
        verbose_name='Задачи рекрутера',
    )
    skills_recruiter = models.TextField(
        verbose_name='Требования к рекрутеру',
    )
    stop_list = models.TextField(
        verbose_name='Стоп-лист сотрудников',
    )

    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    closed_at = models.DateTimeField(
        verbose_name='Дата закрытия',
    )
    status_id = models.CharField(max_length=16, choices=STATUS, default='')


class BidWorkFormat(models.Model):
    """Модель связи заявки и формата работы."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    work_format = models.ForeignKey(
        WorkFormat,
        on_delete=CASCADE,
        verbose_name='ID формата работы',
    )

    class Meta:
        verbose_name = 'Связь заявки и формата работы'
        verbose_name_plural = 'Связи заявки и формата работы'

    def __str__(self):
        return f'{self.bid} -> {self.work_format}'


class BidRegisterAs(models.Model):
    """Модель связи заявки и способа оформления сотрудника."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    register_as = models.ForeignKey(
        RegisterAsOption,
        on_delete=CASCADE,
        verbose_name='ID способа оформления сотрудника',
    )

    class Meta:
        verbose_name = 'Связь заявки и способа оформления сотрудника'
        verbose_name_plural = 'Связи заявки и способа оформления сотрудника'

    def __str__(self):
        return f'{self.bid} -> {self.register_as}'


class BidCountry(models.Model):
    """Модель связи заявки и разрешенной страны гражданства сотрудника."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    country = models.ForeignKey(
        Country,
        on_delete=CASCADE,
        verbose_name='ID страны',
    )

    class Meta:
        verbose_name = 'Связь заявки и разрешенной страны гражданства сотрудника'
        verbose_name_plural = 'Связи заявки и разрешенной страны гражданства сотрудника'

    def __str__(self):
        return f'{self.bid} -> {self.country}'


class BidEmployeeCategory(models.Model):
    """Модель связи заявки и дополнительной категории граждан."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    employee_category = models.ForeignKey(
        EmployeeCategory,
        on_delete=CASCADE,
        verbose_name='ID категории граждан',
    )

    class Meta:
        verbose_name = 'Связь заявки и разрешенной страны гражданства сотрудника'
        verbose_name_plural = 'Связи заявки и разрешенной страны гражданства сотрудника'

    def __str__(self):
        return f'{self.bid} -> {self.employee_category}'


class BidEmployeeSkill(models.Model):
    """Модель связи заявки и навыка соискателя."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    employee_skill = models.ForeignKey(
        EmployeeSkill,
        on_delete=CASCADE,
        verbose_name='ID навыка',
    )

    class Meta:
        verbose_name = 'Связь заявки и навыка соискателя'
        verbose_name_plural = 'Связи заявки и навыка соискателя'

    def __str__(self):
        return f'{self.bid} -> {self.employee_skill}'


class BidEmployeeAddSkill(models.Model):
    """Модель связи заявки и дополнительного навыка соискателя."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    employee_add_skill = models.ForeignKey(
        EmployeeAddSkill,
        on_delete=CASCADE,
        verbose_name='ID дополнительного навыка',
    )

    class Meta:
        verbose_name = 'Связь заявки и дополнительного навыка соискателя'
        verbose_name_plural = 'Связи заявки и дополнительного навыка соискателя'

    def __str__(self):
        return f'{self.bid} -> {self.employee_add_skill}'


class BidRecruiterTask(models.Model):
    """Модель связи заявки и задачи рекрутера."""

    bid = models.ForeignKey(
        Bid,
        on_delete=CASCADE,
        verbose_name='ID заявки',
    )
    recruiter_task = models.ForeignKey(
        EmployeeAddSkill,
        on_delete=CASCADE,
        verbose_name='ID задачи рекрутера',
    )

    class Meta:
        verbose_name = 'Связь заявки и задачи рекрутера'
        verbose_name_plural = 'Связи заявки и задачи рекрутера'

    def __str__(self):
        return f'{self.bid} -> {self.recruiter_task}'