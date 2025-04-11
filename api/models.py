from django.db import models

class Code(models.Model):
    """
    "address": string,
    "bankName": string,
    "countryISO2": string,
    "countryName": string,
    “isHeadquarter”: bool,
    "swiftCode": string,

    """
    address = models.CharField(blank=True)
    bank_name = models.CharField()
    country_iso_2 = models.CharField()
    country_name = models.CharField
    swift_code = models.CharField()
    is_headquarter = models.BooleanField()
    headquarter = models.ForeignKey("self", on_delete=models.CASCADE, related_name="branch", null=True)