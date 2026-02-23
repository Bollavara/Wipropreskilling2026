*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***
Register Restaurant

    Create Session    foodie    ${BASE_URL}

    ${unique}=    Generate Random String    5
    ${restaurant}=    Create Dictionary
    ...    name=RobotRes_${unique}
    ...    category=Indian
    ...    location=Hyderabad
    ...    images=[]
    ...    contact=9999999999

    ${res}=    POST On Session    foodie    /restaurants    json=${restaurant}
    Status Should Be    201    ${res}

View Restaurant Profile

    ${res}=    GET On Session    foodie    /restaurants/1
    Status Should Be    200    ${res}

Disable Restaurant

    ${res}=    PUT On Session    foodie    /restaurants/1/disable
    Status Should Be    200    ${res}
