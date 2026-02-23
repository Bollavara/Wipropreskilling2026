*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/registration_keywords.robot

#Suite Setup       Open Application
#Suite Teardown    Close Application
Test Setup        Open Application
Test Teardown     Close Application

Test Teardown     Run Keyword If Test Failed    Capture Page Screenshot

*** Test Cases ***
Register With Valid Data
    Register User    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Registration Successful

Register With Existing Email
    Register User    ${EXISTING_EMAIL}    ${VALID_PASSWORD}
    Verify Registration Failed

Register With Empty Fields
    Register User    ${EMPTY}    ${EMPTY}
    Verify Registration Failed
