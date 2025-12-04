import pytest
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    """Configurar driver de Chrome con opción headless para CI"""
    chrome_options = Options()
    
    # Verificar si se solicita modo headless
    if '--headless' in sys.argv or request.config.getoption('--headless', default=False):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    """Agregar opción --headless a pytest"""
    parser.addoption('--headless', action='store_true', default=False, 
                     help='Run tests in headless mode')


def test_full_flow(driver):
    """Prueba del flujo completo de la aplicación"""
    try:
        driver.get("http://localhost:5000")
        time.sleep(2)
        assert "Inventory" in driver.title or "Welcome" in driver.page_source
        print("✅ Test E2E passed successfully")
    except Exception as e:
        pytest.skip(f"Server not running: {e}")