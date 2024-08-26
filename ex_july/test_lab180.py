import pytest
import allure

@allure.title("test case 1")
@allure.description("This is a smoke test, we are doing this to verify whether 1+1 =2")
@pytest.mark.smoke
def test_add():
    assert 1+1 == 2

@allure.title("test case 2")
@allure.description("This is a smoke test, we are doing this to verify whether 1-1 =0")
@pytest.mark.smoke
def test_sub():
    assert 1-1 == 0


@allure.title("test case 4")
@allure.description("This is a skip test, not working on this moment")
@pytest.mark.skip
def test_add():
    assert 3+3 == 6
