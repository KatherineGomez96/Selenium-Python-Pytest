from selenium.webdriver.common.by import By
from .base_page2 import BasePage


class SandboxPage(BasePage):
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")

    def navigate_sandbox(self):
        self.navigate_to(
            "https://thefreerangetester.github.io/sandbox-automation-testing/"
        )

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)
