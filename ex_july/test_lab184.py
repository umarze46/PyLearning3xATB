import pytest
import allure
import requests
import json


@allure.title("test_01")
@allure.description("test for checking,the GET bookingID is working or not")
@allure.tag("smoke")
@allure.label("owner", "Umar")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/46"
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200


@allure.title("test_02")
@allure.description("test for failure, the GET bookingID is working or not")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 404
