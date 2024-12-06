from selenium.webdriver.common.by import By
from .base_page import BasePage


class SandboxPage(BasePage): 
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]") 
    
    def click_enviar(self):
        enviar_button = self.wait_for_element(self.ENVIAR_BUTTON)
        enviar_button.click()

