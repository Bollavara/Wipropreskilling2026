*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***
View Orders By Restaurant
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /restaurants/1/orders
    Status Should Be    200    ${response}

View Orders By User
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /users/1/orders
    Status Should Be    200    ${response}
