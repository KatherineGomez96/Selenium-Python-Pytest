import pytest
from pages.sandbox_page2 import SandboxPage


def test_click_en_enviar(sandbox_page):
    sandbox_page.navigate_sandbox()
    sandbox_page.click_enviar()
