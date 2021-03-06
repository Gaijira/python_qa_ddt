import pytest


@pytest.fixture(params=[4, 5, 6], ids=["four", "five", "six"])
def param_fixture(request):
    return request.param
