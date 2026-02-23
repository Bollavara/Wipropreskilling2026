from selenium import webdriver

def get_driver(browser_name):

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception("Browser not supported! Use chrome / firefox / edge")

    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver

#chrome-->pytest -v --html=reports/report_2026-02-24.html --self-contained-html
#firefox--->pytest -v --browser firefox --html=reports/firefox_report.html --self-contained-html
#edge--->pytest -v --browser edge --html=reports/edge_report.html --self-contained-html

