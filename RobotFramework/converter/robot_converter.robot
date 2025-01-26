*** Settings ***
Library    UnitConverterLibrary.py

*** Test Cases ***
Convert Miles To Kilometers
    ${result}=    Convert Miles To Kilometers    1
    Should Be Equal As Numbers    ${result}    1.60934

Convert Kilometers To Miles
    ${result}=    Convert Kilometers To Miles    1.60934
    Should Be Equal As Numbers    ${result}    1

Convert Fahrenheit To Celsius
    ${result}=    Convert Fahrenheit To Celsius    32
    Should Be Equal As Numbers    ${result}    0

Convert Celsius To Fahrenheit
    ${result}=    Convert Celsius To Fahrenheit    0
    Should Be Equal As Numbers    ${result}    32

Convert Celsius To Kelvin
    ${kelvin}=    Convert Celsius To Kelvin    -273.15
    Should Be Equal As Numbers    ${kelvin}    0

    ${kelvin}=    Convert Celsius To Kelvin    100
    Should Be Equal As Numbers    ${kelvin}    373.15

    Run Keyword And Expect Error    ValueError: Temperature below absolute zero is not possible.    Convert Celsius To Kelvin    -274

Convert Kelvin To Celsius
    ${celsius}=    Convert Kelvin To Celsius    0
    Should Be Equal As Numbers    ${celsius}    -273.15

    ${celsius}=    Convert Kelvin To Celsius    373.15
    Should Be Equal As Numbers    ${celsius}    100

    Run Keyword And Expect Error    ValueError: Temperature below absolute zero is not possible.    Convert Kelvin To Celsius    -1

Convert Fahrenheit To Kelvin
    ${kelvin}=    Convert Fahrenheit To Kelvin    -459.67
    Should Be Equal As Numbers    ${kelvin}    0

    ${kelvin}=    Convert Fahrenheit To Kelvin    32
    Should Be Equal As Numbers    ${kelvin}    273.15

    Run Keyword And Expect Error    ValueError: Temperature below absolute zero is not possible.    Convert Fahrenheit To Kelvin    -460

Convert Kelvin To Fahrenheit
    ${fahrenheit}=    Convert Kelvin To Fahrenheit    0
    Should Be Equal As Numbers    ${fahrenheit}    -459.67

    ${fahrenheit}=    Convert Kelvin To Fahrenheit    273.15
    Should Be Equal As Numbers    ${fahrenheit}    32

    Run Keyword And Expect Error    ValueError: Temperature below absolute zero is not possible.    Convert Kelvin To Fahrenheit    -1

Convert Pounds To Kilograms
    ${result}=    Convert Pounds To Kilograms    1
    Should Be Equal As Numbers    ${result}    0.45359237

Convert Kilograms To Pounds
    ${result}=    Convert Kilograms To Pounds    0.45359237
    Should Be Equal As Numbers    ${result}    1

Convert Yards To Meters
    ${result}=    Convert Yards To Meters    1
    Should Be Equal As Numbers    ${result}    0.9144

Convert Meters To Yards
    ${result}=    Convert Meters To Yards    0.9144
    Should Be Equal As Numbers    ${result}    1
