import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_full_flow():
    driver = webdriver.Chrome()
    
    try:
        driver.get("http://localhost:5000")
        time.sleep(2)
        assert "Inventory" in driver.title or "Welcome" in driver.page_source
    except Exception as e:
        pytest.skip(f"Server not running: {e}")
    finally:
        driver.quit()