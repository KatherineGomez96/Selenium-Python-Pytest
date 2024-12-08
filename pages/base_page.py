from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

#page object model se utiliza para encapsular la lógica de navegación de una página en una clase
#la base page define los métodos que se pueden utilizar en cualquier página
#los métodos de la base page se pueden utilizar en cualquier página que herede de ella
#esto nos permite reutilizar código y mantener la lógica de navegación de cada página
#en una sola clase

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        self.wait_for_element(locator).click()

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, index):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)
    
    def get_select_options(self, locator):
        dropdown = Select(self.wait_for_element(locator))
        return[option.text for option in dropdown.options]


    def select_element(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def unselect_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def reload_page(self):
        self.driver.refresh()


