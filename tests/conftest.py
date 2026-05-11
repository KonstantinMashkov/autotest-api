import pytest


# Фикстура, которая будет автоматически вызываться для каждого теста
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")


# Фикстура для инициализации настроек автотестов на уровне сессии
@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Инициализируем настройки автотестов")


# Фикстура для создания данных пользователя, которая будет выполняться один раз на класс тестов
@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


# Фикстура для инициализации API клиента, выполняющаяся для каждого теста
@pytest.fixture(scope='function')
def users_client():
    print("[FUNCTION] Создаем API клиент на каждый автотест")