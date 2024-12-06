import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #condiciones de espera
from selenium.webdriver import ActionChains


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) #espera implicita de 10 segundos, todos los elementos van a estar guiados por esa espera
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


def test_hover_over_enviar(browser):
    # Localizar el botón por su texto usando xpath
    button = WebDriverWait(browser, 10).until( # Espera explicita hasta que el elemento esté disponible
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Enviar')]")
        )
    )

    # Obtenemos el color del botón ANTES de hacer hover
    color_before_hover = button.value_of_css_property("background-color")

    # Usamos ActionChains para simular el hover
    time.sleep(10) #espera explicita de 10 segundos sin importar lo que haga el navegador (es una mala práctica)
    ActionChains(browser).move_to_element(button).perform()

    # Esperamos que cambie el color después de hacer Hover
    WebDriverWait(browser, 10).until(
        lambda d: button.value_of_css_property("background-color") != color_before_hover
    )

    # Obtener el color después del Hover
    color_after_hover = button.value_of_css_property("background-color")

    # Validar con un assertion que efectivamente son distintos valores antes y después del hover
    assert color_before_hover != color_after_hover
