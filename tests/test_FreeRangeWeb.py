import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.mark.regresion #los 'Marks' son tags que nos ayuda a organizar las pruebas
def test_navegacion_free_range_web():
    driver.get("https://www.freerangetesters.com")
    driver.find_element(By.XPATH, "//a[normalize-space()='Cursos' and @href]").click()

#con la nomenclatura: 'pytest -m ...' levanta todas las pruebas con ese mark
#si se escribe: 'pytest --markers' se puede visualizar todos los markes configurados o registrados


'''
Locators y el Find Element en Python: Extra
Creamos una nueva clase: test_FreeRangeWeb.py! 

test_FreeRangeWeb

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
 
def test_navegacion_free_range_web():
    driver.get("https://www.freerangetesters.com")
    driver.find_element(By.XPATH, "//a[normalize-space()='Cursos' and @href]").click()
----------------------------------------------------------------------------------------
Crear XPaths efectivos es fundamental para la automatización de pruebas web con Selenium. Aquí hay algunos ejemplos de estrategias para crear XPaths, siguiendo la línea de lo que vimos en clase y evitando esos horribles xpath absolutos:

Búsqueda por tipo y texto: Para encontrar un botón con el texto "Enviar":

//button[normalize-space()='Enviar']
Búsqueda por atributo: Para localizar un elemento por su clase, como un div con la clase 'header':

//div[@class='header']
Uso de contains: Útil cuando el valor del atributo contiene una palabra específica. Por ejemplo, para encontrar un elemento cuyo ID contiene 'submit':

//*[@id[contains(., 'submit')]]
Búsqueda de elementos hijo: Para encontrar un enlace dentro de un div específico:

//div[@class='navigation']//a[normalize-space()='Inicio']
Búsqueda por posición: Para seleccionar el segundo elemento de una lista:

(//ul[@id='lista-items']/li)[2]
Uso de starts-with: Si quieres encontrar elementos cuyo atributo comienza con un texto específico, como un ID que comienza con 'menu':

//*[@id[starts-with(., 'menu')]]
Combinando múltiples condiciones: Puedes buscar un elemento que cumpla con varias condiciones. Por ejemplo, un botón con texto "Enviar" y clase "btn-activo":

//button[normalize-space()='Enviar' and @class='btn-activo']
Búsqueda por hermanos (following-sibling / preceding-sibling): Para seleccionar el primer elemento hermano que sigue a un h3 con texto específico:

//h3[normalize-space()='Título Sección']/following-sibling::*[1]
Búsqueda por ancestros (ancestor): Para encontrar un div que es ancestro de un elemento específico:

//*[@id='elemento-especifico']/ancestor::div
Búsqueda por descendientes (descendant): Para encontrar todos los elementos 'a' que son descendientes de un div específico:

//div[@class='contenedor']/descendant::a

'''