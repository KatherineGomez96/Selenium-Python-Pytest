from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10): # timeout in seconds
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    ## Vamos a ir agregando métodos como el Click, Select, SendKeys y demás interacciones

#page object model se utiliza para encapsular la lógica de navegación de una página en una clase
#la base page define los métodos que se pueden utilizar en cualquier página
#los métodos de la base page se pueden utilizar en cualquier página que herede de ella
#esto nos permite reutilizar código y mantener la lógica de navegación de cada página
#en una sola clase