*** Settings ***
Library    SeleniumLibrary
#Resource   ../keywords/logout_keywords.robot
#Resource    ../keywords/registration_keywords.robot
#Suite Setup    Open Browser And Login
#Suite Teardown    Close Browser

*** Variables ***
${URL}     https://practice.automationtesting.in/
${USERNAME}    testuser999@gmail.com
${PASSWORD}    Harika@3703

*** Test Cases ***
Logout From Shop
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    Wait Until Element Is Visible    xpath=//a[text()='My Account']    10s
    Click Element    xpath=//a[text()='My Account']
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    name=login
    Wait Until Element Is Visible    xpath=//a[contains(text(),'Logout')]    10s
    Click Element    xpath=//a[contains(text(),'Logout')]
    Page Should Contain Element    xpath=//a[contains(@href,'my-account')]

    Close Browser
