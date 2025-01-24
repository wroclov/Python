*** Settings ***
Library    EmailLibrary.py

*** Test Cases ***
Valid Email Validation Test
    [Template]    Validate Email Address Should Be Valid
    valid.email@example.com
    user.name+tag+sorting@example.com
    user_name@example.co.uk
    user-name@sub.example.com
    user-name@123.123.123.123
    email@[123.123.123.123]
    _______@example.com
    1234567890@e.co
    "email"@example.com

Invalid Email Validation Test
    [Template]    Validate Email Address Should Be Invalid
    plainaddress
    @example.com
    email@example@example.com
    email@example
    .email@example
    something..@example
    username@missingtld;com


*** Keywords ***
Validate Email Address Should Be Valid
    [Arguments]    ${email}
    ${result}=    Validate Email    ${email}
    Log To Console    Email: ${email} - Validation Result: ${result}
    Should Be Equal    ${result}    ${True}

Validate Email Address Should Be Invalid
    [Arguments]    ${email}
    ${result}=    Validate Email    ${email}
    Log To Console    Email: ${email} - Validation Result: ${result}
    Should Be Equal    ${result}    ${False}
