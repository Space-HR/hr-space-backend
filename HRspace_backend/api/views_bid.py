from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from bids.models import Bid, RecruiterToBid, RecruiterToBidAddedResume
from users.models import Recruiter  # CustomUser, Employer,

from .serializers_bid import (BidChangeSerializer, BidGetSerializer,
                              RecruiterToBidAddedResumeSerializer,
                              RecruiterToBidSerializer)

# from .serializers_users import (CustomUserSerializer,
#                                 EmployerSerializer, RecruiterSerializer,
#                                 RecruiterGetSerializer,)

# from .serializers_bid_data import (
#                           CitySerializer, CountrySerializer,
#                           EducationsOptionSerializer,
#                           EmployeeAddSkillSerializer,
#                           EmployeeCategorySerializer,
#                           EmployeeSkillSerializer,
#                           ExperienceOptionSerializer,
#                           JobVacancySerializer,
#                           RecruiterTaskSerializer,
#                           RegisterAsOptionSerializer,
#                           ScheduleOptionSerializer, SphereSerializer,
#                           TariffOptionSerializer, WorkFormatSerializer,
#                         )



class RecruiterToBidViewSet(viewsets.ModelViewSet):
    """Рекрутеры, связанные с заявкой."""
    queryset = RecruiterToBid.objects.all()
    serializer_class = RecruiterToBidSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        bid = get_object_or_404(Bid, id=self.kwargs.get('bid_id'))
        recruiter = get_object_or_404(Recruiter,
                                      id=self.kwargs.get('recruiter_id'))
        serializer.save(bid=bid, recruiter=recruiter)


class RecruiterToBidAddedResumeViewSet(viewsets.ModelViewSet):
    """направленные кандидаты."""
    queryset = RecruiterToBidAddedResume.objects.all()
    serializer_class = RecruiterToBidAddedResumeSerializer
    # permission_classes = (,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        recruiter_to_bid = get_object_or_404(
            RecruiterToBid, id=self.kwargs.get('recruiter_to_bid_id'))

        serializer.save(recruiter_to_bid=recruiter_to_bid)


class BidViewSet(viewsets.ModelViewSet):
    """Вьюсет для заявки."""

    queryset = (Bid.objects.select_related('employer'))
    # permission_classes = (IsEmployer)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BidGetSerializer
        return BidChangeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
