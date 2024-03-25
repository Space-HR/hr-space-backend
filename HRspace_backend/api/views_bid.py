from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from bids.models import Bid, RecruiterToBid, RecruiterToBidAddedResume

from .serializers_bid import (BidChangeSerializer, BidGetSerializer,
                              RecruiterToBidAddedResumeSerializer,
                              RecruiterToBidSerializer,
                              RecruiterToBidCreateSerializer
                              )


class RecruiterToBidViewSet(viewsets.ModelViewSet):
    """Рекрутеры, связанные с заявкой."""
    queryset = RecruiterToBid.objects.all()
    http_method_names = ['get', 'post', 'patch',]  

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecruiterToBidSerializer
        return RecruiterToBidCreateSerializer

    def perform_create(self, serializer):
        bid = get_object_or_404(Bid, id=self.kwargs.get('bid_id'))
        if self.request.user.role == 'recruiter':
            status = 'response'
        else:
            status = 'invite'
        serializer.save(bid=bid, status=status)


class RecruiterToBidAddedResumeViewSet(viewsets.ModelViewSet):
    """направленные кандидаты."""
    queryset = RecruiterToBidAddedResume.objects.all()
    serializer_class = RecruiterToBidAddedResumeSerializer
    http_method_names = ['get', 'post', 'patch',]

    def perform_create(self, serializer):
        recruiter_to_bid = get_object_or_404(
            RecruiterToBid, id=self.kwargs.get('recruiter_to_bid_id'))

        serializer.save(recruiter_to_bid=recruiter_to_bid,
                        status='new')


class BidViewSet(viewsets.ModelViewSet):
    """Вьюсет для заявки."""

    queryset = (Bid.objects.select_related('employer'))
    http_method_names = ['get', 'post', 'patch',]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BidGetSerializer
        return BidChangeSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
