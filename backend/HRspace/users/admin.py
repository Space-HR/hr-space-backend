from django.contrib import admin

from .models import CustomUser, Recruiter


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'photo')
    list_filter = ('username',)
    search_fields = ('username', )
    empty_value_display = '-пусто-'


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('user', 'about_me', 'top10', 'finished_cases',
                    'years_of_exp',)
    empty_value_display = '-пусто-'


# class SkillsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'skill')
#     empty_value_display = '-пусто-'
#
#
# class AchievementsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'achievement')
#     empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
# admin.site.register(Skills, SkillsAdmin)
# admin.site.register(Achievements, AchievementsAdmin)
