*** Settings ***
Library           Fibonacci.py

*** Variables ***
${EMPTY_LIST}    []

*** Test Cases ***
Test Fibonacci for Zero
    [Documentation]    Test the Fibonacci function when input is 0.
    ${result}=    Fibonacci    0
    Log    Fibonacci result for 0: ${result}
    Should Be Equal As Strings    ${result}    ${EMPTY_LIST}

Test Fibonacci for Negative
    [Documentation]    Test the Fibonacci function when input is negative.
    ${result}=    Fibonacci    -7
    Log    Fibonacci result for -7: ${result}
    Should Be Equal As Strings    ${result}    ${EMPTY_LIST}

Test Fibonacci for String
    [Documentation]    Test the Fibonacci function for random string
    ${result}=    Fibonacci    cat_and_dog
    Log    Fibonacci result for cat_and_dog: ${result}
    Should Be Equal As Strings    ${result}    Error: input must be an integer

Test Fibonacci for One
    [Documentation]    Test the Fibonacci function when input is 1.
    ${result}=    Fibonacci    1
    Log    Fibonacci result for 1: ${result}
    Should Be Equal As Strings    ${result}    [0]

Test Fibonacci for Ten
    [Documentation]    Test the Fibonacci function when input is 10.
    ${result}=    Fibonacci    10
    Log    Fibonacci result for 10: ${result}
    Should Be Equal As Strings    ${result}    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


