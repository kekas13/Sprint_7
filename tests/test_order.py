import allure
import pytest
import requests

from env import MAKE_ORDER
from urls import URL


@allure.title('Проверка успешного создания заказа при разном заполнении поля "цвет"')
@pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
def test_create_order(color):
    data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
    response = requests.post(f'{URL}{MAKE_ORDER}', params=data)
    assert response.status_code == 201 and "track" in response.text
