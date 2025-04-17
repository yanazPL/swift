import pytest
from api.models import Code


@pytest.fixture
def headquarter():
    return Code.objects.create(
        address="UL.TESTOWA 1, KRAKÓW, 11-111",
        bank_name="TEST BANK POLSKA",
        country_name="POLAND",
        country_iso_2="PL",
        swift_code="ABCDABCDXXX",
        is_headquarter=True,
        headquarter=None
    )


@pytest.fixture
def branch(headquarter):
    return Code.objects.create(
        address="UL.PĘTLA 1, KRAKÓW, 11-111",
        bank_name="TEST BANK POLSKA",
        country_name="POLAND",
        country_iso_2="PL",
        swift_code="ABCDABCD1234",
        is_headquarter=False,
        headquarter=headquarter
    )

@pytest.fixture
def headquarter_with_2_branches(branch):
    Code.objects.create(
        address="UL.GAŁĘZI 1, KRAKÓW, 11-111",
        bank_name="TEST BANK POLSKA",
        country_name="POLAND",
        country_iso_2="PL",
        swift_code="ABCDABCD5678",
        is_headquarter=False,
        headquarter=branch.headquarter
    )
    return branch.headquarter