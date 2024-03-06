from django.contrib import admin

from .models import CustomUser, Recruiter, Skills, Achievements


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'full_name'
                    'company', 'position', 'photo')
    list_filter = ('username',)
    search_fields = ('username', )
    empty_value_display = '-пусто-'


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('username', 'top10', 'finished_cases',
                    'years_of_exp', 'achievements', 'about_me')
    empty_value_display = '-пусто-'


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill')
    empty_value_display = '-пусто-'


class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'achievement')
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Achievements, AchievementsAdmin)
