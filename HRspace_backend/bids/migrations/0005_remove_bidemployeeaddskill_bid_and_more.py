# Generated by Django 4.2.9 on 2024-03-25 13:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0004_auto_20240324_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidemployeeaddskill',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidemployeeaddskill',
            name='employee_add_skill',
        ),
        migrations.RemoveField(
            model_name='bidemployeecategory',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidemployeecategory',
            name='employee_category',
        ),
        migrations.RemoveField(
            model_name='bidemployeeskill',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidemployeeskill',
            name='employee_skill',
        ),
        migrations.RemoveField(
            model_name='bidrecruitertask',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidrecruitertask',
            name='recruiter_task',
        ),
        migrations.RemoveField(
            model_name='bidregisteras',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidregisteras',
            name='register_as',
        ),
        migrations.RemoveField(
            model_name='bidworkformat',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='bidworkformat',
            name='work_format',
        ),
        migrations.AlterModelOptions(
            name='recruitertobidaddedresume',
            options={'verbose_name': 'Добавленные к заявке кандидаты', 'verbose_name_plural': 'Добавленные к заявке кандидаты'},
        ),
        migrations.AlterField(
            model_name='bid',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.city', verbose_name='ID города'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='closed_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата закрытия'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='employee_add_skills',
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_add_skills',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.employeeaddskill', verbose_name='Дополнительные навыки'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='employee_categories',
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_categories',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.employeecategory', verbose_name='Дополнительные категории граждан'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='employee_education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.educationsoption', verbose_name='ID требования к образованию'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='employee_experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.experienceoption', verbose_name='ID требования к опыту работы'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='employee_skills',
        ),
        migrations.AddField(
            model_name='bid',
            name='employee_skills',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.employeeskill', verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='employee_will_go_to_work_at',
            field=models.DateField(blank=True, null=True, verbose_name='Желаемая дата выхода сотрудника'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='expected_first_cv_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ожидаемая дата получения первых резюме'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='foreign_countries',
        ),
        migrations.AddField(
            model_name='bid',
            name='foreign_countries',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.country', verbose_name='Граждане каких стран принимаются на работу'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='job_vacancy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.jobvacancy', verbose_name='ID вакансии'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='max_salary',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Максимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='min_salary',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Минимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='qty_employees',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Количество сотрудников'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='recruiter_tasks',
        ),
        migrations.AddField(
            model_name='bid',
            name='recruiter_tasks',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.recruitertask', verbose_name='Задачи рекрутера'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='register_as_set',
        ),
        migrations.AddField(
            model_name='bid',
            name='register_as_set',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.registerasoption', verbose_name='Оформление сотрудника'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.scheduleoption', verbose_name='ID опции графика работы'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='schedule_comment',
            field=models.CharField(blank=True, max_length=200, verbose_name='Комментарий к графику работы'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='skills_recruiter',
            field=models.TextField(blank=True, verbose_name='Требования (навыки) к рекрутеру'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='sphere',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.sphere', verbose_name='ID сферы деятельности'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='stop_list',
            field=models.TextField(blank=True, verbose_name='Стоп-лист сотрудников'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='tariff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='bids.tariffoption', verbose_name='ID тарифа'),
        ),
        migrations.RemoveField(
            model_name='bid',
            name='work_formats',
        ),
        migrations.AddField(
            model_name='bid',
            name='work_formats',
            field=models.ManyToManyField(blank=True, related_name='bids', to='bids.workformat', verbose_name='Форматы работы'),
        ),
        migrations.AlterField(
            model_name='recruitertobid',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recruitertobid', to='bids.bid', verbose_name='ID заявки'),
        ),
        migrations.AlterField(
            model_name='recruitertobidaddedresume',
            name='accepted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Кандидат одобрен'),
        ),
        migrations.AlterField(
            model_name='recruitertobidaddedresume',
            name='recruiter_to_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvtorecruiter', to='bids.recruitertobid', verbose_name='ID связи заявки и рекрутера'),
        ),
        migrations.DeleteModel(
            name='BidCountry',
        ),
        migrations.DeleteModel(
            name='BidEmployeeAddSkill',
        ),
        migrations.DeleteModel(
            name='BidEmployeeCategory',
        ),
        migrations.DeleteModel(
            name='BidEmployeeSkill',
        ),
        migrations.DeleteModel(
            name='BidRecruiterTask',
        ),
        migrations.DeleteModel(
            name='BidRegisterAs',
        ),
        migrations.DeleteModel(
            name='BidWorkFormat',
        ),
    ]
