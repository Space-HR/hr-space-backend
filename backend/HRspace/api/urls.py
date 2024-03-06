from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet, AchievementsViewSet, SkillsViewSet,
                    RecruiterViewSet)

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register('customuser', CustomUserViewSet, basename='customuser')
router_v1.register('recruiter', RecruiterViewSet, basename='recruiter')
router_v1.register('skills', SkillsViewSet, basename='skills')
router_v1.register(r'recruiter/(?P<recruiter_id>\d+)/achievements',
                   AchievementsViewSet, basename='achievements')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('', include('djoser.urls')),  # закоменчено, чтобы в сваггере не мешались
    path('auth/', include('djoser.urls.authtoken')),
]
