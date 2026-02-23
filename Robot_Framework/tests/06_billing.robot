*** Settings ***
Resource    ../keywords/billing_keywords.robot

*** Test Cases ***
Verify User Can Complete Billing And Place Order
    [Documentation]    End-to-end checkout flow with assertions.
    Open Browser To Website
    Add Product To Cart
    Proceed To Checkout
    Fill Billing Details
    Place The Order
    [Teardown]    Close Browser