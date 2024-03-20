from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .constants import (MAX_ABOUT_ME_LENGTH, MAX_CHAR_LENGTH,
                        MAX_COMPANY_LENGTH, MAX_POSITION_LENGTH)


class CustomUser(AbstractUser):
    """Модель пользователя."""
    EMPLOYER = 'employer'
    RECRUITER = 'recruiter'
    ADMIN = 'administrator'
    ROLES = (
        (EMPLOYER, 'employer'),
        (RECRUITER, 'recruiter'),
        (ADMIN, 'administrator'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    username = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        unique=True,
        verbose_name='Логин',
        validators=([RegexValidator(
            regex=r'^(?!me$).*$',
            message='Неподходящий логин. "me" использовать запрещено.')]))
    first_name = models.CharField('Имя', max_length=MAX_CHAR_LENGTH)
    last_name = models.CharField('Фамилия', max_length=MAX_CHAR_LENGTH)
    password = models.CharField(max_length=MAX_CHAR_LENGTH,
                                verbose_name='пароль', )
    photo = models.ImageField('Фото', upload_to='photo',
                              blank=True, null=True, )
    role = models.CharField(max_length=16, choices=ROLES, default=EMPLOYER)
    created_at = models.DateTimeField(verbose_name='Дата публикации',
                                      auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username


class Recruiter(models.Model):
    """Рекрутер"""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recruiter',
        verbose_name='рекрутер', )
    about_me = models.CharField('О себе', max_length=MAX_ABOUT_ME_LENGTH)
    top10 = models.BooleanField(default=False, )
    finished_cases = models.PositiveIntegerField(
        'Количество закрытых вакансий', )
    years_of_exp = models.PositiveIntegerField('Количество лет опыта', )

    class Meta:
        verbose_name = 'Рекрутер'
        verbose_name_plural = 'Рекрутеры'

    def __str__(self):
        return self.about_me


class Employer(models.Model):
    """Работодатель"""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='employer',
        verbose_name='работодатель', )
    company = models.CharField('Компания',
                               max_length=MAX_COMPANY_LENGTH)
    position = models.CharField('Должность',
                                max_length=MAX_POSITION_LENGTH)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    def __str__(self):
        return self.company
