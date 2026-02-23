*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/filter_keywords.robot

Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To Shop Page

*** Test Cases ***
Default Sorting Validation
    Select Default Sorting
    Validate Products Visible

Sort By Price Low To High Validation
    Select Sort By Price Low To High
    Validate Products Visible

Filter By Price Validation
    ${before}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${after}=     Get Price Range Text
    Should Not Be Equal    ${before}    ${after}

Price Change Filter Validation
    ${initial}=    Get Price Range Text
    Move Price Slider And Apply Filter
    ${changed}=    Get Price Range Text
    Log    Initial Price Range: ${initial}
    Log    Changed Price Range: ${changed}
    Should Not Be Equal    ${initial}    ${changed}
