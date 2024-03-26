from django.contrib import admin

from .models import CustomUser, Employer, Recruiter


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'photo')
    list_filter = ('username',)
    search_fields = ('username', )
    empty_value_display = '-пусто-'


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'about_me', 'top10', 'finished_cases',
                    'years_of_exp',)
    empty_value_display = '-пусто-'


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company', 'position')
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(Employer, EmployerAdmin)
