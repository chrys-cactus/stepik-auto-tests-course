import pytest

def test_succeed():
    assert True
    import slow_module
    if slow_module.slow_function():
        pytest.xfail("slow_module taking too long")


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
