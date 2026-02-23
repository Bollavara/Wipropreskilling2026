*** Settings ***
Resource    ../resources/common.robot
Resource    ../keywords/cart_keywords.robot
Variables   ../variables/variables.py
Test Setup      Open Application
Test Teardown   Close Browser

*** Test Cases ***

#Add Product To Cart
#    Open Shop Page
#    Add First Product To Cart
#    Cart Should Be Updated

Add Multiple Products
    Open Browser    https://practice.automationtesting.in/    chrome
    Maximize Browser Window
    Add Product To Cart By Index    1
    Add Product To Cart By Index    2
    Close Browser