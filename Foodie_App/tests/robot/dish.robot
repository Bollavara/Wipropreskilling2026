*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***
Add Dish
    Create Session    foodie    ${BASE_URL}

    ${restaurant_payload}=    Create Dictionary
    ...    name=TempRest
    ...    category=Indian
    ...    location=Hyd
    ...    images=
    ...    contact=9999999999

    ${res}=    POST On Session    foodie    /restaurants    json=${restaurant_payload}
    Status Should Be    201    ${res}

    ${restaurant_id}=    Set Variable    ${res.json()['id']}

    ${dish_payload}=    Create Dictionary
    ...    name=Biryani
    ...    type=Veg
    ...    price=200
    ...    available_time=Lunch
    ...    image=

    ${response}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${dish_payload}
    Status Should Be    201    ${response}


Update Dish
    Create Session    foodie    ${BASE_URL}
    ${payload}=    Create Dictionary    price=300
    ${response}=    PUT On Session    foodie    /dishes/1    json=${payload}
    Status Should Be    200    ${response}

Enable Disable Dish
    Create Session    foodie    ${BASE_URL}
    ${payload}=    Create Dictionary    enabled=${False}
    ${response}=    PUT On Session    foodie    /dishes/1/status    json=${payload}
    Status Should Be    200    ${response}

Delete Dish
    Create Session    foodie    ${BASE_URL}
    ${response}=    DELETE On Session    foodie    /dishes/1
    Status Should Be    200    ${response}
