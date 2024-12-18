*** Settings ***
Library    Calculate.py

*** Test Cases ***
Perform Calculations
    ${result}    Calculate    1 + 2
    Should Be Equal As Numbers    ${result}    3
    ${result}    Calculate    1 - 7
    Should Be Equal As Numbers    ${result}    -6
    ${result}    Calculate    22 * 4
    Should Be Equal As Numbers    ${result}    88
    ${result}    Calculate    33 / 3
    Should Be Equal As Numbers    ${result}    11