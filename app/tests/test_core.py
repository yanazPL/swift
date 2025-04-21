from django.urls import reverse
import pytest
from api.models import Code
from api.serializers import HqSerializer, BranchSerializer
from rest_framework.exceptions import ErrorDetail


@pytest.fixture
def code_data():
    return {
        "address": "TESTSTRASSE 1, BERLIN, 10115",
        "bankName": "TEST BANK DEUTSCHLAND",
        "countryName": "GERMANY",
        "countryISO2": "DE",
        "isHeadquarter": True,
        "swiftCode": "DEDEDEDEXXX"
    }


@pytest.mark.django_db
class TestAPI:
    def test_get_hq(self, client, headquarter):
        url = reverse("swift_code_detail", kwargs={"swift_code": headquarter.swift_code})
        response = client.get(url, format="json")
        assert response.status_code == 200
        assert response.data["id"] == headquarter.id
        assert response.data["address"] == "UL.TESTOWA 1, KRAKÓW, 11-111"
        assert response.data["bankName"] == "TEST BANK POLSKA"
        assert response.data["countryName"] == "POLAND"
        assert response.data["countryISO2"] == "PL"
        assert response.data["isHeadquarter"]
        assert response.data["branches"] == []

    def test_delete_branch(self, client, headquarter_with_2_branches):
        deleted_branch = headquarter_with_2_branches.branches.first()
        url = reverse("swift_code_detail", kwargs={"swift_code": deleted_branch.swift_code})
        response = client.delete(url, format="json")
        assert response.status_code == 204
        assert headquarter_with_2_branches.branches.count() == 1

    def test_hq_with_branch(self, client, branch):
        url = reverse("swift_code_detail", kwargs={"swift_code": branch.headquarter.swift_code})
        response = client.get(url, format="json")
        branch_data = response.data["branches"][0]
        assert response.status_code == 200
        assert branch_data["id"] == branch.id
        assert branch_data["swiftCode"] == branch.swift_code
        assert branch_data["address"] == "UL.PĘTLA 1, KRAKÓW, 11-111"
        assert branch_data["bankName"] == "TEST BANK POLSKA"
        assert branch_data["countryName"] == "POLAND"
        assert branch_data["countryISO2"] == "PL"
        assert not branch_data["isHeadquarter"]
        assert not "branches" in branch_data

    def test_post(self, client, code_data):
        response = client.post(reverse("swift_code_create"), data=code_data)
        assert Code.objects.filter(swift_code=code_data["swiftCode"]).exists()
        assert response.status_code == 201

    def test_post_duplicate(self, client, code_data):
        client.post(reverse("swift_code_create"), data=code_data)
        response = client.post(reverse("swift_code_create"), data=code_data)
        assert response.status_code == 400
        assert isinstance(response.data["swiftCode"][0], ErrorDetail)

    def test_post_too_long_code(self, client, code_data):
        data = code_data
        data["swiftCode"] = "A" * 15
        response = client.post(reverse("swift_code_create"), data=data)
        obj_from_data = response.data["swiftCode"][0]
        assert response.status_code == 400
        assert isinstance(obj_from_data, ErrorDetail)
        assert obj_from_data.code == "max_length"

    def test_list_for_country_de(self, client, headquarter_with_2_branches, german_headquarter_with_branch):
        url = reverse("swif_codes_for_country", kwargs={"country_iso_2": "DE"})
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_list_for_country_pl(self, client, headquarter_with_2_branches, german_headquarter_with_branch):
        url = reverse("swif_codes_for_country", kwargs={"country_iso_2": "PL"})
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 3
