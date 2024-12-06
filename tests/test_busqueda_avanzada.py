import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://thefreerangetester.github.io/sandbox-automation-testing/")
    yield driver
    driver.quit()


def test_checkbox(browser):
    # Ubicar el elemento contenedor de los checkboxes
    contenedor_checkboxes = browser.find_element(By.CLASS_NAME, "mt-3")

    # Dentro del contenedor, buscar el checkbox para "Hamburguesa" por su ID
    checkbox_hamburguesa = contenedor_checkboxes.find_element(By.ID, "checkbox-1")

    # Interacción con el checkbox (le hace click si no está seleccionado)
    if not checkbox_hamburguesa.is_selected():
        checkbox_hamburguesa.click()

    # Validación de que el checkbox está seleccionado
    assert checkbox_hamburguesa.is_selected()
