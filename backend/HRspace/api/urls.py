from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet, RecruiterViewSet, SphereViewSet,
                    EmployerViewSet,
                    JobVacancyViewSet, CityViewSet, ScheduleOptionViewSet,
                    WorkFormatViewSet)

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register('customuser', CustomUserViewSet, basename='customuser')
router_v1.register('recruiter', RecruiterViewSet, basename='recruiter')
router_v1.register('employer', EmployerViewSet, basename='employer')

router_v1.register('jobvacancy', JobVacancyViewSet, basename='jobvacancy')
router_v1.register('sphere', SphereViewSet, basename='sphere')
router_v1.register('city', CityViewSet, basename='city')
router_v1.register('scheduleoption', ScheduleOptionViewSet,
                   basename='scheduleoption')
router_v1.register('workformat', WorkFormatViewSet,
                   basename='workformat')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('', include('djoser.urls')),  # чтобы лишние эндпоинты не мешались
    path('auth/', include('djoser.urls.authtoken')),
]
