from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from users.models import CustomUser, Recruiter


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""
    photo = Base64ImageField()
    recruiter = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'full_name',
                  'company', 'position', 'photo',
                  'recruiter',)

    def get_recruiter(self, obj):
        recruiter = Recruiter.objects.filter(user_id=obj).all()
        return RecruiterSerializer(recruiter, many=True).data

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'photo',
                  'password')


class RecruiterSerializer(serializers.ModelSerializer):
    """Cериализатор для рекрутеров."""
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )

    class Meta:
        model = Recruiter
        read_only_fields = ('user',)
        fields = ('id', 'top10', 'finished_cases',  'user',
                  'years_of_exp', 'about_me')


# class AchievementsSerializer(serializers.ModelSerializer):
#     """Cериализатор для достижений."""
#     class Meta:
#         model = Achievements
#         fields = '__all__'
#
#
# class SkillsSerializer(serializers.ModelSerializer):
#     """Cериализатор для навыков."""
#     class Meta:
#         model = Skills
#         fields = '__all__'
