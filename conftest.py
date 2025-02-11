import pytest

@pytest.fixture
def browser(scope="session"):
    print("Браузер!")
    yield

    print("Закрываем браузер!")

