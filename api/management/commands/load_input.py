from django.core.management.base import BaseCommand, CommandError
from api.models import Code
import csv

FILENAME = 'Interns_2025_SWIFT_CODES - Sheet1.csv'

class Command(BaseCommand):
    help = "Reads SWIFT codes from csv."

    def handle(self, *args, **options):
        with open(FILENAME, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            hqs = {}
            branches = []
            for row in csv_reader:
                iso2, code, _, name, address, _, country, *_ = row
                address = address.lstrip()

                code_object = Code(
                    swift_code=code,
                    address=address,
                    bank_name=name,
                    country_iso_2=iso2,
                    country_name=country
                )
                if code.endswith("XXX"):
                    code_object.is_headquarter = True
                    hqs[code[:8]] = code_object
                else:
                    code_object.is_headquarter = False
                    branches.append(code_object)
                code_object.save()

        for branch in branches:
            try:
                branch.headquarter = hqs[branch.swift_code[:8]]
                branch.save()
            except KeyError:
                continue
