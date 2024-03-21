from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views_bid import (BidViewSet, RecruiterToBidAddedResumeViewSet,
                        RecruiterToBidViewSet)
from .views_bid_data import (CityViewSet, CountryViewSet,
                             EducationsOptionViewSet, EmployeeAddSkillViewSet,
                             EmployeeCategoryViewSet, EmployeeSkillViewSet,
                             ExperienceOptionViewSet, JobVacancyViewSet,
                             RecruiterTaskViewSet, RegisterAsOptionViewSet,
                             ScheduleOptionViewSet, SphereViewSet,
                             TariffOptionViewSet, WorkFormatViewSet)
from .views_users import CustomUserViewSet, EmployerViewSet, RecruiterViewSet

app_name = "api"
router_v1 = DefaultRouter()

# эндпоинты пользователей
router_v1.register('customuser', CustomUserViewSet, basename='customuser')
router_v1.register('recruiter', RecruiterViewSet, basename='recruiter')
router_v1.register('employer', EmployerViewSet, basename='employer')

# эндпоинты справочников
router_v1.register('jobvacancy', JobVacancyViewSet, basename='jobvacancy')
router_v1.register('sphere', SphereViewSet, basename='sphere')
router_v1.register('city', CityViewSet, basename='city')
router_v1.register('scheduleoption', ScheduleOptionViewSet,
                   basename='scheduleoption')
router_v1.register('workformat', WorkFormatViewSet,
                   basename='workformat')
router_v1.register('registerasoption', RegisterAsOptionViewSet,
                   basename='registerasoption')
router_v1.register('country', CountryViewSet, basename='country')
router_v1.register('employeecategory', EmployeeCategoryViewSet,
                   basename='employeecategory')
router_v1.register('experienceoption', ExperienceOptionViewSet,
                   basename='experienceoption')
router_v1.register('educationsoption', EducationsOptionViewSet,
                   basename='educationsoption')
router_v1.register('employeeskill', EmployeeSkillViewSet,
                   basename='employeeskill')
router_v1.register('employeeaddskill', EmployeeAddSkillViewSet,
                   basename='employeeaddskill')
router_v1.register('recruitertask', RecruiterTaskViewSet,
                   basename='recruitertask')
router_v1.register('tariffoption', TariffOptionViewSet,
                   basename='tariffoption')

# эндпоинты заявки
router_v1.register('bid', BidViewSet, basename='bid')
router_v1.register(r'bid/(?P<bid_id>\d+)/recruitertobid',
                   RecruiterToBidViewSet,
                   basename='recruitertobid')
router_v1.register(r'bid/(?P<bid_id>\d+)/recruitertobid/(?P<recruitertobid_id>\d+)/recruitertobidaddedresume',
                   RecruiterToBidAddedResumeViewSet,
                   basename='recruitertobidaddedresume')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('', include('djoser.urls')),  # чтобы лишние эндпоинты не мешались
    path('auth/', include('djoser.urls.authtoken')),
]
