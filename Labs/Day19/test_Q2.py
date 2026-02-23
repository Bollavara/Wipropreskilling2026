from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRID_URL = "http://localhost:4444"

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        continue

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.get("https://www.google.com")

    # Verify page title
    assert "Google" in driver.title

    # Get browser and platform details
    capabilities = driver.capabilities
    browser_name = capabilities.get("browserName")
    platform_name = capabilities.get("platformName")

    print(f"Browser: {browser_name} | Platform: {platform_name}")

    driver.quit()
