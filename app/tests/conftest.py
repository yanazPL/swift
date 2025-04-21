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

@pytest.fixture
def german_headquarter_with_branch():
    """Tworzy centralę z oddziałami w Niemczech"""
    hq = Code.objects.create(
        address="HAUPTSTRASSE 1, MÜNCHEN, 80331",
        bank_name="HAUPTBANK DEUTSCHLAND",
        country_name="GERMANY",
        country_iso_2="DE",
        is_headquarter=True,
        swift_code="HBDEDEMM"
    )

    Code.objects.create(
        address="ZWEIGSTELLE 1, FRANKFURT, 60313",
        bank_name="HAUPTBANK DEUTSCHLAND",
        country_name="GERMANY",
        country_iso_2="DE",
        is_headquarter=False,
        swift_code="HBDEDEFF",
        headquarter=hq
    )
    return hq