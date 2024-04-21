import pytest
from courier_generator import register_new_courier_and_return_login_password, generate_login_pass


@pytest.fixture
def registered_courier():
    login, password, firstname = register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password
    }
    yield payload


@pytest.fixture
def unregistered_courier():
    login, password, firstname = generate_login_pass()
    payload = {
        "login": login,
        "password": password,
        "firstName": firstname
    }

    yield payload
