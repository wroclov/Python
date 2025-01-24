Library    EmailLibrary.py

*** Test Cases ***
Email Validation Test
    ${result}=    Validate Email    test@example.com
    Should Be True    ${result}
