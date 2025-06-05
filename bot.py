from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    options=options
)

driver.get("https://example.com")
print("Página cargada.")
driver.quit()
