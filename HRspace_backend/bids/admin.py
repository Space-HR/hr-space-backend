from django.contrib import admin

from .models import (Bid, City,
                     Country, EducationsOption, EmployeeAddSkill,
                     EmployeeCategory, EmployeeSkill, ExperienceOption,
                     JobVacancy, RecruiterTask, RegisterAsOption,
                     ScheduleOption, Sphere, TariffOption, WorkFormat,
                    #  RecruiterToBid,
                    #  RecruiterToBidAddedResume,
                    #  BidCountry, BidEmployeeAddSkill, BidEmployeeCategory,
                    #  BidEmployeeSkill, BidRecruiterTask, BidRegisterAs,
                     )


class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    empty_value_display = '-пусто-'


class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    empty_value_display = '-пусто-'


class EmployeeAddSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    empty_value_display = '-пусто-'


class TariffOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'payment_for_employee_start_working',
                    'payment_for_employee_after_guarantee',
                    'guarantee_period',
                    'units_of_measurement_warranty_period')
    empty_value_display = '-пусто-'


admin.site.register(JobVacancy, JobVacancyAdmin)
admin.site.register(Sphere)
admin.site.register(City)
admin.site.register(ScheduleOption)
admin.site.register(WorkFormat)
admin.site.register(RegisterAsOption)
admin.site.register(EmployeeCategory)
admin.site.register(ExperienceOption)
admin.site.register(EducationsOption)
admin.site.register(EmployeeSkill, EmployeeSkillAdmin)
admin.site.register(EmployeeAddSkill, EmployeeAddSkillAdmin)
admin.site.register(TariffOption, TariffOptionAdmin)
admin.site.register(Country)
admin.site.register(RecruiterTask)
admin.site.register(Bid)

# admin.site.register(RecruiterToBid)
# admin.site.register(RecruiterToBidAddedResume)
# admin.site.register(BidRegisterAs)
# admin.site.register(BidCountry)
# admin.site.register(BidEmployeeCategory)
# admin.site.register(BidEmployeeSkill)
# admin.site.register(BidEmployeeAddSkill)
# admin.site.register(BidRecruiterTask)
