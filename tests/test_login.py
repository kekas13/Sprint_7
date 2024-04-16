import allure
import pytest
import requests

from Sprint_7.courier_generator import generate_login_pass
from Sprint_7.env import LOGIN_COURIER
from Sprint_7.urls import URL


@allure.title('Проверка возврата "id" при успешной авторизации курьера')
def test_login_courier_success(registered_courier):
    data = registered_courier
    response = requests.post(f'{URL}{LOGIN_COURIER}', data=data)
    assert response.status_code == 200 and "id" in response.text


@allure.title('Проверка ошибки при авторизации с неверным логином или паролем')
@pytest.mark.parametrize('field', ["login", "password"])
def test_login_courier_with_invalid_log_or_pass(registered_courier, field):
    data = registered_courier.copy()
    data[field] += 'invalid'
    response = requests.post(f'{URL}{LOGIN_COURIER}', data=data)
    assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}'


@allure.title('Проверка ошибки при авторизации без поля логина или пароля')
@pytest.mark.parametrize('field, status, text', [("login", 400, '{"code":400,"message":"Недостаточно данных для входа"}'),
                                                 ("password", 504, 'Service unavailable')])
def test_login_courier_no_login_or_no_pass_field(registered_courier, field, status, text):
    data = registered_courier.copy()
    del data[field]
    response = requests.post(f'{URL}{LOGIN_COURIER}', data=data)
    assert response.status_code == status and response.text == text


@allure.title('Проверка ошибки при авторизации под несуществующим пользователем')
def test_login_unregistered_courier():
    login, password, firstname = generate_login_pass()
    data = {
        "login": login,
        "password": password
    }
    response = requests.post(f'{URL}{LOGIN_COURIER}', data=data)
    assert response.status_code == 404 and response.text == '{"code":404,"message":"Учетная запись не найдена"}'
