*** Settings ***
Library           SeleniumLibrary
Suite Setup       Open Browser    https://turniejeamatorskie.info/    chrome
Suite Teardown    Close Browser

*** Variables ***
${PLAYER_NAME}    Piotr Laskowski

*** Test Cases ***
Click Table Tennis Ranking and Find Player
    [Documentation]    Test that table tennis ranking exists and specific player is present
    [Tags]             ranking
    Maximize Browser Window
    Navigate to Table Tennis Ranking
    ${ranking_points}=    Find Player and Get Ranking Points    ${PLAYER_NAME}
    Log    Player: ${PLAYER_NAME} found, ranking points: ${ranking_points}.
    ${ranking_points_int}=    Convert To Integer    ${ranking_points}
    Run Keyword If    ${ranking_points_int} <= 0    Fail    Ranking points should be positive but got ${ranking_points_int}.
    Log To Console    Test passed for player ${PLAYER_NAME} with ranking points ${ranking_points}.
    #Sleep    2


*** Keywords ***
Navigate to Table Tennis Ranking
    Log To Console    Navigating to Table Tennis Ranking...
    Wait Until Element Is Visible    xpath=//a[@href='/dyscypliny/2-tenis-stolowy' and text()='Tenis stołowy']    2s
    #Sleep         2
    Click Link    xpath=//a[@href='/dyscypliny/2-tenis-stolowy' and text()='Tenis stołowy']


Find Player and Get Ranking Points
    [Arguments]    ${player_name}
    Log To Console    Searching for player: ${player_name}...
    Wait Until Element Is Visible    xpath=//a[contains(@class, 'name') and contains(text(), '${player_name}')]    2s
    #Sleep         2
    Click Link    xpath=//a[contains(@class, 'name') and contains(text(), '${player_name}')]
    ${points}=    Get Text    xpath=//tr[td[text()='Punkty rankingowe:']]//a[contains(@class, 'name')]
    Log To Console    Player: ${player_name} found, ranking points: ${points}.
    Return From Keyword    ${points}

