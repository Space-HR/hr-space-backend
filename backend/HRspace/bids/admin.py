from django.contrib import admin

from .models import (JobVacancy, Sphere, City, ScheduleOption, WorkFormat,
                     RegisterAsOption, Country, EmployeeCategory,
                     ExperienceOption,
                     EducationsOption, EmployeeSkill, EmployeeAddSkill,
                     TariffOption, Bid, RecruiterToBid,
                     RecruiterToBidAddedResume,
                    #  BidWorkFormat, BidRegisterAs,  # &
                    #  BidCountry, BidEmployeeCategory, BidEmployeeSkill,
                    #  BidEmployeeAddSkill, BidRecruiterTask,
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
admin.site.register(TariffOption)
admin.site.register(Country)
admin.site.register(Bid)
admin.site.register(RecruiterToBid)
admin.site.register(RecruiterToBidAddedResume)

# admin.site.register(BidWorkFormat)
# admin.site.register(BidRegisterAs)
# admin.site.register(BidCountry)
# admin.site.register(BidEmployeeCategory)
# admin.site.register(BidEmployeeSkill)
# admin.site.register(BidEmployeeAddSkill)
# admin.site.register(BidRecruiterTask)
