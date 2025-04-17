from rest_framework import serializers
from .models import Code


class BranchSerializer(serializers.ModelSerializer):
    address = serializers.CharField()
    bankName = serializers.CharField(source='bank_name')
    countryISO2 = serializers.CharField(source='country_iso_2')
    countryName = serializers.CharField(source='country_name')
    isHeadquarter = serializers.BooleanField(source='is_headquarter')
    swiftCode = serializers.CharField(source='swift_code')

    class Meta:
        model = Code
        fields = [
            "id",
            'address',
            'bankName',
            'countryISO2',
            'countryName',
            'isHeadquarter',
            'swiftCode',
        ]


class HqSerializer(BranchSerializer):
    class Meta:
        model = Code
        fields = [
            "id",
            'branches',
            'address',
            'bankName',
            'countryISO2',
            'countryName',
            'isHeadquarter',
            'swiftCode',
        ]
    branches = BranchSerializer(many=True, read_only=True)