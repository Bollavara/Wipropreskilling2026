*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/search_keywords.robot

Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Shop Page

*** Test Cases ***
Search With Valid Product
    Search Product    ${VALID_PRODUCT}
    Validate Search Results Visible
    Page Should Contain    ${VALID_PRODUCT}

Search With Invalid Product
    Search Product    ${INVALID_PRODUCT}
    Validate No Search Results

Search With Empty Value
    Search Product    ${EMPTY}
    Validate Search Results Visible
