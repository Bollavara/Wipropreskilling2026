*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/login_keywords.robot

Test Setup       Open Application
Test Teardown    Run Keywords    Run Keyword If Test Failed    Capture Page Screenshot    AND    Close Application

*** Test Cases ***
Login With Valid Credentials
    Login User    ${VALID_LOGIN_EMAIL}    ${VALID_LOGIN_PASSWORD}
    Verify Login Successful

Login With Invalid Password
    Login User    ${VALID_LOGIN_EMAIL}    ${INVALID_PASSWORD}
    Verify Login Failed

Login With Invalid Email
    Login User    ${INVALID_EMAIL}    ${INVALID_PASSWORD}
    Verify Login Failed


Login With Empty Fields
    Login User    ${EMPTY}    ${EMPTY}
    Verify Login Failed
