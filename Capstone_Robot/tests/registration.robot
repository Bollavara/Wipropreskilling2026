*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/auth_keywords.robot
Suite Setup    Open Application
Suite Teardown    Close Application

*** Test Cases ***
Login With Valid Credentials
    Go To My Account Page
    Login With Credentials    ${VALID_USERNAME}    ${VALID_PASSWORD}
    Verify Login Success

Login With Invalid Password
    Go To My Account Page
    Login With Credentials    ${VALID_USERNAME}    ${INVALID_PASSWORD}
    Verify Login Failure

Login With Empty Password
    Go To My Account Page
    Login With Credentials    ${VALID_USERNAME}
    Verify Login Failure
