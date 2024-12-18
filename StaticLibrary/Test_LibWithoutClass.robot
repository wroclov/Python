*** Settings ***
Library    LibraryWithoutClass.py

*** Test Cases ***
Use Custom Keywords
    ${base64}    Encode As Base64    This is a Test String
    Log    ${base64}
    ${decoded}    Decode From Base64    ${base64}
    Log    ${decoded}
    ${length}    Return Length    Abracadabra
    Log    ${length}
    ${reverse}    Return Reverse    Welcome to Wroclove
    Log    ${length}