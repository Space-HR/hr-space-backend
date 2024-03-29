# Generated by Django 4.2.9 on 2024-03-20 22:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название заявки')),
                ('min_salary', models.PositiveIntegerField(blank=True, verbose_name='Минимальная зарплата')),
                ('max_salary', models.PositiveIntegerField(default=0, verbose_name='Минимальная зарплата')),
                ('schedule_comment', models.CharField(max_length=200, verbose_name='Комментарий к графику работы')),
                ('vhl', models.BooleanField(default=False, verbose_name='Добровольное медицинское страхование')),
                ('foreign_citizen', models.BooleanField(default=False, verbose_name='Иностранные граждане')),
                ('working_conditions', models.TextField(blank=True, verbose_name='Описание дополнительных условий работы')),
                ('responsibilities_employee', models.TextField(blank=True, verbose_name='Описание обязонностей сотрудника')),
                ('qty_employees', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Количество сотрудников')),
                ('payment_for_employee', models.PositiveIntegerField(default=0, verbose_name='Вознаграждение за сотрудника')),
                ('qty_recruiters', models.PositiveSmallIntegerField(default=1, verbose_name='Допустипое количество рекрутеров')),
                ('employee_will_go_to_work_at', models.DateTimeField(verbose_name='Желаемая дата выхода сотрудника')),
                ('expected_first_cv_date', models.DateTimeField(verbose_name='Ожидаемая дата получения первых резюме')),
                ('resume_after_interview', models.BooleanField(default=False, verbose_name='Предоставлять резюме после собеседования с соискателем')),
                ('not_private_person', models.BooleanField(default=True, verbose_name='Только юр. лица, ИП, самозанятые')),
                ('skills_recruiter', models.TextField(verbose_name='Требования (навыки) к рекрутеру')),
                ('stop_list', models.TextField(verbose_name='Стоп-лист сотрудников')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('closed_at', models.DateTimeField(verbose_name='Дата закрытия')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('moderation', 'moderation'), ('published', 'published'), ('at_work', 'at_work'), ('closed', 'closed'), ('canceled', 'canceled')], default='draft', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='EducationsOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Требование к образованию')),
            ],
            options={
                'verbose_name': 'Требование к образованию',
                'verbose_name_plural': 'Требования к образованию',
            },
        ),
        migrations.CreateModel(
            name='EmployeeAddSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Дополнительный навык соискателя')),
            ],
            options={
                'verbose_name': 'Дополнительный навык соискателя',
                'verbose_name_plural': 'Дополнительные навыки соискателя',
            },
        ),
        migrations.CreateModel(
            name='EmployeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название категории граждан')),
            ],
            options={
                'verbose_name': 'Категория граждан',
                'verbose_name_plural': 'Категории граждан',
            },
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Навык соискателя')),
            ],
            options={
                'verbose_name': 'Навык соискателя',
                'verbose_name_plural': 'Навыки соискателя',
            },
        ),
        migrations.CreateModel(
            name='ExperienceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Требование к опыту работы')),
            ],
            options={
                'verbose_name': 'Требование к опыту работы',
                'verbose_name_plural': 'Требования к опыту работы',
            },
        ),
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название вакансии')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='RecruiterTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Задача рекрутера')),
            ],
            options={
                'verbose_name': 'Задача рекрутера',
                'verbose_name_plural': 'Задачи рекрутера',
            },
        ),
        migrations.CreateModel(
            name='RecruiterToBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('invite', 'invite'), ('response', 'response'), ('accepted', 'accepted'), ('refused', 'refused')], default='response', max_length=16)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.recruiter', verbose_name='ID рекрутера')),
            ],
            options={
                'verbose_name': 'Связь заявки и рекрутера',
                'verbose_name_plural': 'Связи заявки и рекрутера',
            },
        ),
        migrations.CreateModel(
            name='RegisterAsOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Способ оформления сотрудника')),
            ],
            options={
                'verbose_name': 'Способ оформления сотрудника',
                'verbose_name_plural': 'Способы оформления сотрудника',
            },
        ),
        migrations.CreateModel(
            name='ScheduleOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Вид графика работы')),
            ],
            options={
                'verbose_name': 'Вид графика работы',
                'verbose_name_plural': 'Виды графика работы',
            },
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название сферы деятельности')),
            ],
            options={
                'verbose_name': 'Сфера деятельности',
                'verbose_name_plural': 'Сферы деятельности',
            },
        ),
        migrations.CreateModel(
            name='TariffOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название тарифа')),
                ('payment_for_employee_start_working', models.PositiveSmallIntegerField(verbose_name='Процент оплаты за выход сотрудника')),
                ('payment_for_employee_after_guarantee', models.PositiveSmallIntegerField(verbose_name='Процент оплаты после гарантийного периода')),
                ('guarantee_period', models.PositiveSmallIntegerField()),
                ('units_of_measurement_warranty_period', models.CharField(choices=[('day', 'day'), ('month', 'month'), ('year', 'year')], default='day', max_length=16)),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='WorkFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Формата работы')),
            ],
            options={
                'verbose_name': 'Формат работы',
                'verbose_name_plural': 'Форматы работы',
            },
        ),
        migrations.CreateModel(
            name='RecruiterToBidAddedResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='Загрузите резюме', upload_to='uploads/resumes/', verbose_name='Файл с резюме')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий к резюме')),
                ('accepted_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('new', 'new'), ('to_interview', 'to_interview'), ('accepted', 'accepted'), ('canceled', 'canceled')], default='new', max_length=16)),
                ('recruiter_to_bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.recruitertobid', verbose_name='ID связи заявки и рекрутера')),
            ],
            options={
                'verbose_name': 'Связь заявки и рекрутера',
                'verbose_name_plural': 'Связи заявки и рекрутера',
            },
        ),
        migrations.CreateModel(
            name='BidRegisterAs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('register_as', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.registerasoption', verbose_name='ID способа оформления сотрудника')),
            ],
            options={
                'verbose_name': 'Связь заявки и способа оформления сотрудника',
                'verbose_name_plural': 'Связи заявки и способа оформления сотрудника',
            },
        ),
        migrations.CreateModel(
            name='BidRecruiterTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('recruiter_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.recruitertask', verbose_name='ID задачи рекрутера')),
            ],
            options={
                'verbose_name': 'Связь заявки и задачи рекрутера',
                'verbose_name_plural': 'Связи заявки и задачи рекрутера',
            },
        ),
        migrations.CreateModel(
            name='BidEmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('employee_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.employeeskill', verbose_name='ID навыка')),
            ],
            options={
                'verbose_name': 'Связь заявки и навыка соискателя',
                'verbose_name_plural': 'Связи заявки и навыка соискателя',
            },
        ),
        migrations.CreateModel(
            name='BidEmployeeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('employee_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.employeecategory', verbose_name='ID категории граждан')),
            ],
            options={
                'verbose_name': 'Связь заявки и разрешенной страны гражданства сотрудника',
                'verbose_name_plural': 'Связи заявки и разрешенной страны гражданства сотрудника',
            },
        ),
        migrations.CreateModel(
            name='BidEmployeeAddSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('employee_add_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.employeeaddskill', verbose_name='ID дополнительного навыка')),
            ],
            options={
                'verbose_name': 'Связь заявки и дополнительного навыка соискателя',
                'verbose_name_plural': 'Связи заявки и дополнительного навыка соискателя',
            },
        ),
        migrations.CreateModel(
            name='BidCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.bid', verbose_name='ID заявки')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bids.country', verbose_name='ID страны')),
            ],
            options={
                'verbose_name': 'Связь заявки и разрешенной страны гражданства сотрудника',
                'verbose_name_plural': 'Связи заявки и разрешенной страны гражданства сотрудника',
            },
        ),
        migrations.AddField(
            model_name='bid',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.city', verbose_name='ID города'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_add_skills',
            field=models.ManyToManyField(blank=True, through='bids.BidEmployeeAddSkill', to='bids.employeeaddskill', verbose_name='Дополнительные навыки'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_categories',
            field=models.ManyToManyField(blank=True, through='bids.BidEmployeeCategory', to='bids.employeecategory', verbose_name='Дополнительные категории граждан'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.educationsoption', verbose_name='ID требования к образованию'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.experienceoption', verbose_name='ID требования к опыту работы'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_skills',
            field=models.ManyToManyField(through='bids.BidEmployeeSkill', to='bids.employeeskill', verbose_name='Навыки'),
        ),
        migrations.AddField(
            model_name='bid',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='users.employer', verbose_name='Автор заявки'),
        ),
        migrations.AddField(
            model_name='bid',
            name='foreign_countries',
            field=models.ManyToManyField(blank=True, through='bids.BidCountry', to='bids.country', verbose_name='Граждане каких стран принимаются на работу'),
        ),
        migrations.AddField(
            model_name='bid',
            name='job_vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.jobvacancy', verbose_name='ID вакансии'),
        ),
        migrations.AddField(
            model_name='bid',
            name='recruiter_tasks',
            field=models.ManyToManyField(through='bids.BidRecruiterTask', to='bids.recruitertask', verbose_name='Задачи рекрутера'),
        ),
        migrations.AddField(
            model_name='bid',
            name='register_as_set',
            field=models.ManyToManyField(through='bids.BidRegisterAs', to='bids.registerasoption', verbose_name='Оформление сотрудника'),
        ),
        migrations.AddField(
            model_name='bid',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.scheduleoption', verbose_name='ID опции графика работы'),
        ),
        migrations.AddField(
            model_name='bid',
            name='sphere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.sphere', verbose_name='ID сферы деятельности'),
        ),
        migrations.AddField(
            model_name='bid',
            name='tariff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.tariffoption', verbose_name='ID тарифа'),
        ),
        migrations.AddField(
            model_name='bid',
            name='work_format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.workformat', verbose_name='Форматы работы'),
        ),
        migrations.AddConstraint(
            model_name='recruitertobid',
            constraint=models.UniqueConstraint(fields=('recruiter', 'bid'), name='recruiter_bid'),
        ),
        migrations.AddConstraint(
            model_name='bidregisteras',
            constraint=models.UniqueConstraint(fields=('bid', 'register_as'), name='bid_register_as'),
        ),
        migrations.AddConstraint(
            model_name='bidrecruitertask',
            constraint=models.UniqueConstraint(fields=('bid', 'recruiter_task'), name='bid_recruiter_task'),
        ),
        migrations.AddConstraint(
            model_name='bidemployeeskill',
            constraint=models.UniqueConstraint(fields=('bid', 'employee_skill'), name='bid_employee_skill'),
        ),
        migrations.AddConstraint(
            model_name='bidemployeecategory',
            constraint=models.UniqueConstraint(fields=('bid', 'employee_category'), name='bid_employee_category'),
        ),
        migrations.AddConstraint(
            model_name='bidemployeeaddskill',
            constraint=models.UniqueConstraint(fields=('bid', 'employee_add_skill'), name='bid_employee_add_skill'),
        ),
        migrations.AddConstraint(
            model_name='bidcountry',
            constraint=models.UniqueConstraint(fields=('bid', 'country'), name='bid_country'),
        ),
    ]
