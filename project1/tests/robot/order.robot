*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***
Full Order Flow
    Create Session    foodie    ${BASE_URL}

    # Register Restaurant
    ${restaurant}=    Create Dictionary
    ...    name=RobotRes_${TEST NAME}
    ...    category=Indian
    ...    location=Hyderabad
    ...    images=[]
    ...    contact=9999999999

    ${res}=    POST On Session    foodie    /restaurants    json=${restaurant}
    Status Should Be    201    ${res}
    ${restaurant_id}=    Set Variable    ${res.json()['id']}

    # Register User
    ${user}=    Create Dictionary
    ...    name=RobotUser_${TEST NAME}
    ...    email=robot_${TEST NAME}@gmail.com
    ...    password=12345

    ${user_res}=    POST On Session    foodie    /users/register    json=${user}
    Status Should Be    201    ${user_res}
    ${user_id}=    Set Variable    ${user_res.json()['id']}

    # Add Dish
    ${dish}=    Create Dictionary
    ...    name=Biryani
    ...    type=Non-Veg
    ...    price=250
    ...    available_time=Lunch
    ...    image=

    ${dish_res}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${dish}
    Status Should Be    201    ${dish_res}
    ${dish_id}=    Set Variable    ${dish_res.json()['id']}

    # Create List Properly
    ${dish_list}=    Create List    ${dish_id}

    # Place Order
    ${order}=    Create Dictionary
    ...    user_id=${user_id}
    ...    restaurant_id=${restaurant_id}
    ...    dishes=${dish_list}

    ${order_res}=    POST On Session    foodie    /orders    json=${order}
    Status Should Be    201    ${order_res}
