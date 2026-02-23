*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=../variables/registration_users.csv    delimiter=;
Resource          ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
# ADDED: This runs after every single row in your CSV
Test Teardown     Run Keyword If Test Failed    Capture Failed Screenshot
Test Template     Register User

*** Test Cases ***
User Registration    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

*** Keywords ***
*** Keywords ***
Register User
    [Arguments]    ${EMAIL}    ${PASSWORD}    ${FIRSTNAME}    ${LASTNAME}    ${PHONE}    ${CITY}    ${POSTCODE}    ${EXPECTED}

    IF    '${EXPECTED}' != 'PASS'
        Skip    Not registration user
    END

    Go To    https://practice.automationtesting.in/my-account/

    # NEW: Run your ad-handling keyword before interacting
    Handle Ads Popup

    Wait Until Page Contains Element    id=reg_email

    Input Text    id=reg_email        ${EMAIL}
    Textfield Value Should Be         id=reg_email    ${EMAIL}

    Input Text    id=reg_password     ${PASSWORD}
    Element Should Be Visible         id=reg_password

    # --- FIX APPLIED HERE ---
    # Instead of Click Button, we use JS to bypass the intercepting iframe
    Execute Javascript    document.querySelector('input[name="register"]').click()
    # -------------------------

    Wait Until Keyword Succeeds    15s    2s    Check Registration Result
Check Registration Result
    ${logout}=    Run Keyword And Return Status
    ...    Page Should Contain    Logout

    ${exists}=    Run Keyword And Return Status
    ...    Page Should Contain    already registered

    #assertions
    IF    ${logout} or ${exists}
        Log    Registration successful (new user or already registered)
    ELSE
        Fail    Registration failed - no expected result found
    END