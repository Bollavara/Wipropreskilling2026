*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    DateTime

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000/api/v1

*** Test Cases ***

User Registration
    Create Session    foodie    ${BASE_URL}
    ${timestamp}=    Get Time    epoch
    ${email}=    Set Variable    robot_${timestamp}@mail.com

    ${payload}=    Create Dictionary
    ...    name=RobotUser
    ...    email=${email}
    ...    password=12345

    ${response}=    POST On Session    foodie    /users/register    json=${payload}
    Status Should Be    201    ${response}


Search Restaurants
    Create Session    foodie    ${BASE_URL}
    ${params}=    Create Dictionary    name=RobotRest
    ${response}=    GET On Session    foodie    /restaurants/search    params=${params}
    Status Should Be    200    ${response}


Place Order
    Create Session    foodie    ${BASE_URL}

    # Create Restaurant
    #${timestamp}=    Get Time    epoch
    #${restaurant_name}=    Set Variable    RobotRest_${timestamp}
    ${timestamp}=    Get Time    epoch
    ${random}=    Evaluate    random.randint(1000,9999)    modules=random
    ${restaurant_name}=    Set Variable    RobotRest_${timestamp}_${random}


    ${rest_payload}=    Create Dictionary
    ...    name=${restaurant_name}
    ...    category=Indian
    ...    location=Hyderabad
    ...    contact=9999999999

    ${rest_resp}=    POST On Session    foodie    /restaurants    json=${rest_payload}
    Status Should Be    201    ${rest_resp}

    ${rest_data}=    Set Variable    ${rest_resp.json()}
    ${restaurant_id}=    Get From Dictionary    ${rest_data}    id


    # Add Dish
    ${dish_payload}=    Create Dictionary
    ...    name=Biryani
    ...    type=Non-Veg
    ...    price=250
    ...    available_time=Lunch
    ...    image=

    ${dish_resp}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${dish_payload}
    Status Should Be    201    ${dish_resp}

    ${dish_data}=    Set Variable    ${dish_resp.json()}
    ${dish_id}=    Get From Dictionary    ${dish_data}    id


    # Register User
    ${email}=    Set Variable    user_${timestamp}@mail.com

    ${user_payload}=    Create Dictionary
    ...    name=RobotUser
    ...    email=${email}
    ...    password=12345

    ${user_resp}=    POST On Session    foodie    /users/register    json=${user_payload}
    Status Should Be    201    ${user_resp}

    ${user_data}=    Set Variable    ${user_resp.json()}
    ${user_id}=    Get From Dictionary    ${user_data}    id


    # Place Order
    @{dish_list}=    Create List    ${dish_id}

    ${order_payload}=    Create Dictionary
    ...    user_id=${user_id}
    ...    restaurant_id=${restaurant_id}
    ...    dishes=@{dish_list}

    ${order_resp}=    POST On Session    foodie    /orders    json=${order_payload}
    Status Should Be    201    ${order_resp}

    # Capture Order ID for Rating
    ${order_data}=    Set Variable    ${order_resp.json()}
    ${order_id}=    Get From Dictionary    ${order_data}    id
    Set Suite Variable    ${order_id}


Give Rating
    Create Session    foodie    ${BASE_URL}

    ${payload}=    Create Dictionary
    ...    order_id=${order_id}
    ...    rating=5
    ...    comment=Excellent

    ${response}=    POST On Session    foodie    /ratings    json=${payload}
    Status Should Be    201    ${response}
