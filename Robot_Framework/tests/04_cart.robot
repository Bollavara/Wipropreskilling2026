*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/cart_keywords.robot

Test Setup       Open Application
Test Teardown    Run Keywords    Run Keyword If Test Failed    Capture Page Screenshot    AND    Close Application

*** Test Cases ***
Add Product To Cart
    Add First Product To Cart
    Go To Cart Page
    Verify Product Added To Cart

Update Product Quantity
    Add First Product To Cart
    Go To Cart Page
    Update Product Quantity
    Verify Quantity Updated

Remove Product From Cart
    Add First Product To Cart
    Go To Cart Page
    Remove Product From Cart
    Verify Cart Is Empty
