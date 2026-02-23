*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Verify Page Title And Screenshot
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    Title Should Be    Google
    Capture Page Screenshot
    Close Browser
