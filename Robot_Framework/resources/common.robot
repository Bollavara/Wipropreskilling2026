*** Settings ***
Library    SeleniumLibrary    screenshot_root_directory=reports/screenshots
Variables  ../variables/config.py

*** Keywords ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    10s

Close Application
    Close Browser
