import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # для опций

@pytest.fixture(scope='function', autouse=True)
def driver (request):
    """Создаёт изолированный WebDriver для каждого теста, настраивает опции
    (инкогнито, без кэша), закрывает после теста для чистоты окружения."""
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox') # не песочница, а реальный проект
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options) # Создаёт новый экземпляр Chrome для изоляции тестов
    request.cls.driver = driver # Создает драйвер внутри тестов
    yield driver
    driver.quit() # Закрывает браузер после теста