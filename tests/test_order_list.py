import allure
import requests

from Sprint_7.env import MAKE_ORDER
from Sprint_7.urls import URL


@allure.title('Проверка возврата списка заказов в тело ответа')
def test_order_list():
    response = requests.get(f'{URL}{MAKE_ORDER}')
    assert "orders" in response.json() and response.json()["orders"] is not None
