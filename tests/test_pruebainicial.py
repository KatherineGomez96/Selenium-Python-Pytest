import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())


driver = webdriver.Chrome(service=service)

def test_Prueba():
    driver.get("https://www.freerangetesters.com/")
    titulo = driver.title
    assert titulo == "Free Range Testers"
