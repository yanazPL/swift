from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView
from api.serializers import HqSerializer, BranchSerializer
from api.models import Code

class SwiftRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """
    API view that retrieves or deletes a bank code instance based on swift_code.
    Uses HqSerializer for headquarters and BranchSerializer for branches.
    """
    queryset = Code.objects.all()
    lookup_field = 'swift_code'
    def get_serializer_class(self):
        # Get the object (automatically looked up by swift_code)
        obj = self.get_object()
        return HqSerializer if obj.is_headquarter else BranchSerializer


class SwiftCreateAPIView(CreateAPIView):
    queryset = Code.objects.all()
    serializer_class = BranchSerializer