*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    DateTime

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***

Approve Restaurant
    Create Session    foodie    ${BASE_URL}

    ${timestamp}=    Get Time    epoch
    ${restaurant_name}=    Set Variable    AdminRest_${timestamp}

    ${payload}=    Create Dictionary
    ...    name=${restaurant_name}
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${response}=    POST On Session    foodie    /restaurants    json=${payload}
    Status Should Be    201    ${response}

    ${data}=    Set Variable    ${response.json()}
    ${restaurant_id}=    Get From Dictionary    ${data}    id

    Set Suite Variable    ${restaurant_id}

    ${approve}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${approve}


Disable Restaurant By Admin
    Create Session    foodie    ${BASE_URL}
    ${disable}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/disable
    Status Should Be    200    ${disable}


View Feedback
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /admin/feedback
    Status Should Be    200    ${response}


View Orders
    Create Session    foodie    ${BASE_URL}
    ${response}=    GET On Session    foodie    /admin/orders
    Status Should Be    200    ${response}
