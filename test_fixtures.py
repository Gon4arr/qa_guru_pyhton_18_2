import pytest



@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")

@pytest.fixture
def user():
    print("Юзер!")
    return "username","password"

def test_login (login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
    # assert 1 == 2

def test_logout (login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
