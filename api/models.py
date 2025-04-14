from django.db import models


class Code(models.Model):
    address = models.CharField(blank=True)
    bank_name = models.CharField()
    country_iso_2 = models.CharField()
    country_name = models.CharField()
    swift_code = models.CharField(unique=True)
    is_headquarter = models.BooleanField()
    headquarter = models.ForeignKey("self", on_delete=models.CASCADE, related_name="branches", null=True)

    def save(self, *args, **kwargs):
        self.country_name = self.country_name.upper()
        self.country_iso_2 = self.country_iso_2.upper()
        super().save(*args, **kwargs)

