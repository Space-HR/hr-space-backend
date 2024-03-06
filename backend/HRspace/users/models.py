from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.constants import (MAX_CHAR_LENGTH,
                             MAX_ABOUT_ME_LENGTH,
                             MAX_SKILL_LENGTH, MAX_ACHIEVEMENT_LENGTH)


class CustomUser(AbstractUser):
    """Модель пользователя."""
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'company', 'position',]
    username = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        unique=True,
        verbose_name='Логин',
        validators=([RegexValidator(
            regex=r'^(?!me$).*$',
            message='Неподходящий логин. "me" использовать запрещено.')]))
    first_name = models.CharField('Имя', max_length=MAX_CHAR_LENGTH)
    last_name = models.CharField('Фамилия', max_length=MAX_CHAR_LENGTH)
    company = models.CharField('Компания', max_length=MAX_CHAR_LENGTH)
    position = models.CharField('Должность', max_length=MAX_CHAR_LENGTH)
    password = models.CharField(max_length=MAX_CHAR_LENGTH,
                                verbose_name='пароль',)
    photo = models.ImageField('Фото', upload_to='photo',
                              blank=True, null=True,)

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.position}'

    def get_full_name(self):
        """ Функция возвращает имя и фамилию с пробелом между ними."""
        return f"{self.first_name} {self.last_name}"


class Skills(models.Model):
    """Избранное"""

    skill = models.CharField('Навык', max_length=MAX_SKILL_LENGTH)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        default_related_name = 'skills'


class Recruiter(models.Model):
    """Рекрутер"""
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recruiter',
        verbose_name='рекрутер',)
    about_me = models.CharField('О себе', max_length=MAX_ABOUT_ME_LENGTH)
    top10 = models.BooleanField(default=False,)
    finished_cases = models.PositiveIntegerField(
        'Количество закрытых вакансий', )
    years_of_exp = models.PositiveIntegerField('Количество лет опыта', )
    skills = models.ManyToManyField(
        Skills,
        related_name='recruiter'
    )

    class Meta:
        verbose_name = 'Рекрутер'
        verbose_name_plural = 'Рекрутеры'

    def __str__(self):
        return self.user


class Achievements(models.Model):
    """Достижения."""

    recruiter = models.ForeignKey(
        Recruiter,
        on_delete=models.CASCADE,
    )
    achievement = models.CharField('Достижение',
                                   max_length=MAX_ACHIEVEMENT_LENGTH)

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        default_related_name = 'achievements'

    def __str__(self):
        return self.achievement
