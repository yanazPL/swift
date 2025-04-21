from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, ListAPIView
from api.serializers import HqSerializer, BranchSerializer
from api.models import Code


class SwiftRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Code.objects.all()
    lookup_field = 'swift_code'
    def get_serializer_class(self):
        # Get the object (automatically looked up by swift_code)
        obj = self.get_object()
        return HqSerializer if obj.is_headquarter else BranchSerializer


class SwiftCreateAPIView(CreateAPIView):
    queryset = Code.objects.all()
    serializer_class = BranchSerializer


class SwiftCodesListForCountryAPIView(ListAPIView):
    queryset = Code.objects.all().prefetch_related('branches')
    serializer_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Split into headquarters and branches
        country_iso_2 = kwargs.get("country_iso_2")
        headquarters = queryset.filter(is_headquarter=True, country_iso_2=country_iso_2)
        branches = queryset.filter(is_headquarter=False, country_iso_2=country_iso_2)

        # Serialize separately
        hq_data = HqSerializer(headquarters, many=True, context={'request': request}).data
        branch_data = BranchSerializer(branches, many=True, context={'request': request}).data

        # Combine results
        return Response(hq_data + branch_data)