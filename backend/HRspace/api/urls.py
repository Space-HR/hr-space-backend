from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, RecruiterViewSet

app_name = "api"
router_v1 = DefaultRouter()

router_v1.register('customuser', CustomUserViewSet, basename='customuser')
router_v1.register('recruiter', RecruiterViewSet, basename='recruiter')
router_v1.register('employer', RecruiterViewSet, basename='employer')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('', include('djoser.urls')),  # чтобы лишние эндпоинты не мешались
    path('auth/', include('djoser.urls.authtoken')),
]
