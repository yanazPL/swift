from django.urls import reverse
import pytest
from api.serializers import HqSerializer, BranchSerializer


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
