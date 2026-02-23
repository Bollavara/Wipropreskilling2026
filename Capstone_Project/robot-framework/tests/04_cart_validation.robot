*** Settings ***
Resource    ../resources/common.resource
Suite Setup       Open Application
Suite Teardown    Close Browser
Test Setup        Go To Shop Page
# --- ADDED TEST TEARDOWN HERE ---
Test Teardown     Run Keyword If Test Failed    Capture Failed Screenshot

*** Keywords ***
Go To Shop Page
    Go To    https://practice.automationtesting.in/shop/
    #assertions
    Wait Until Page Contains Element    id=content


Add First Product By URL
    Go To    https://practice.automationtesting.in/shop/?add-to-cart=169
    #assertions
    Wait Until Page Contains Element    xpath=//a[contains(text(),'View Basket')]
    #assertions
    Page Should Contain    View Basket


Add Second Product By URL
    Go To    https://practice.automationtesting.in/shop/?add-to-cart=181
    #assertions
    Wait Until Page Contains Element    xpath=//a[contains(text(),'View Basket')]
    #assertions
    Page Should Contain    View Basket


Open Cart
    Wait Until Element Is Visible    xpath=//a[contains(text(),'View Basket')]
    # FIX: Use JS to click the button underneath the Ad
    Execute Javascript    document.querySelector('a.wc-forward').click()
    #Click Element    xpath=//a[contains(text(),'View Basket')]

    #assertions
    Wait Until Page Contains Element    css=table.shop_table

    #assertions
    Element Should Be Visible    css=table.shop_table


Remove One Product
    Wait Until Element Is Visible    css=a.remove
    # FIX: Use JS to click the remove 'X' button
    Execute Javascript    document.querySelector('a.remove').click()
    #Scroll Element Into View    css=a.remove
    #Click Element               css=a.remove

    #assertions
    Wait Until Element Is Visible    css=.woocommerce-message
    #assertions
    Element Should Contain      css=.woocommerce-message    removed


Proceed To Checkout
    # Stable navigation (avoids overlay issues)
    Go To    https://practice.automationtesting.in/checkout/

    #assertions
    Wait Until Page Contains Element    id=customer_details

    #assertions
    Element Should Be Visible           id=customer_details


*** Test Cases ***
Add Multiple Products In Cart
    Add First Product By URL
    Add Second Product By URL
    Open Cart

    ${count}=    Get Element Count    css=table.shop_table tbody tr
    #assertions
    Should Be True    ${count} >= 2
    #assertions
    Element Should Be Visible    css=.cart_totals


Remove One Product From Cart
    Add First Product By URL
    Add Second Product By URL
    Open Cart

    ${before}=    Get Element Count    css=table.shop_table tbody tr
    Remove One Product
    ${after}=    Get Element Count    css=table.shop_table tbody tr
    #assertions
    Should Be True    ${after} < ${before}
    #assertions
    Element Should Be Visible    css=table.shop_table


Proceed To Checkout Product
    Add First Product By URL
    Open Cart
    Proceed To Checkout

    #assertions
    Page Should Contain Element    id=customer_details

    #assertions
    Page Should Contain Element    id=billing_first_name

    #assertions
    Page Should Contain Element    id=billing_last_name

    #assertions
    Page Should Contain Element    id=place_order

