import allure
import requests

from env import MAKE_ORDER
from urls import URL


@allure.title('Проверка возврата списка заказов в тело ответа')
def test_order_list():
    response = requests.get(f'{URL}{MAKE_ORDER}')
    assert "orders" in response.json() and response.json()["orders"] is not None
