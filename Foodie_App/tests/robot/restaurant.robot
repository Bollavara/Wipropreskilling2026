*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***
Register Restaurant
    Create Session    foodie    ${BASE_URL}
    ${timestamp}=    Get Time    epoch
    ${restaurant_name}=    Set Variable    RobotRest_${timestamp}

    ${payload}=    Create Dictionary
    ...    name=${restaurant_name}
    ...    category=Indian
    ...    location=Hyderabad
    ...    images=${EMPTY}
    ...    contact=9999999999
    ${response}=    POST On Session    foodie    /restaurants    json=${payload}
    Status Should Be    201    ${response}

Update Restaurant
    Create Session    foodie    ${BASE_URL}
    ${payload}=    Create Dictionary    location=Bangalore
    ${response}=    PUT On Session    foodie    /restaurants/1    json=${payload}
    Status Should Be    200    ${response}

Disable Restaurant
    Create Session    foodie    ${BASE_URL}
    ${response}=    PUT On Session    foodie    /restaurants/1/disable
    Status Should Be    200    ${response}

View Restaurant Profile
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /restaurants/1
    Status Should Be    200    ${response}
