import allure
import pytest
import requests

from Sprint_7.courier_generator import generate_login_pass
from Sprint_7.urls import URL
from Sprint_7.env import CREATE_COURIER


@allure.title('Проверка успешного создания курьера')
def test_create_courier_is_ok(unregistered_courier):
    data = unregistered_courier
    response = requests.post(f'{URL}{CREATE_COURIER}', data=data)
    assert response.status_code == 201 and response.text == '{"ok":true}'


@allure.title('Проверка, что нельза создать 2 одинаковых')
def test_same_courier_not_ok(unregistered_courier):
    data = unregistered_courier
    requests.post(f'{URL}{CREATE_COURIER}', data=data)
    response = requests.post(f'{URL}{CREATE_COURIER}', data=data)
    assert response.status_code == 409 and response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'


@allure.title('Проверка успешного создания курьера при заполнении только обязательных полей')
def test_create_courier_no_name_field(unregistered_courier):
    data = unregistered_courier
    data["firstName"] = None
    response = requests.post(f'{URL}{CREATE_COURIER}', data=data)
    assert response.status_code == 201 and response.text == '{"ok":true}'


@allure.title('Проверка ошибки при создании курьера без обязательного поля')
@pytest.mark.parametrize('field', ["login", "password"])
def test_create_courier_no_login_or_no_pass_field(field):
    login, password, firstname = generate_login_pass()
    data = {
        "login": login,
        "password": password,
        "firstName": firstname
    }
    del data[field]
    response = requests.post(f'{URL}{CREATE_COURIER}', data=data)
    assert (response.status_code == 400 and
            response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}')
