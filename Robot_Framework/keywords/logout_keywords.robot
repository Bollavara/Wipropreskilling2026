*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/common.robot

*** Keywords ***
Login User
    [Arguments]    ${username}    ${password}
    Go To    https://practice.automationtesting.in/my-account/
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    name=login
    Wait Until Page Contains Element    css=a.logout

Logout User
    Wait Until Element Is Visible    css=a.logout
    Click Link    css=a.logout
    Wait Until Page Contains Element    id=username   # login field visible again
