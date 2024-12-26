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
    Log To Console    Entering ranking...
    Wait Until Element Is Visible    xpath=//a[@href='/dyscypliny/2-tenis-stolowy' and text()='Tenis stołowy']    2s
    Click Link         xpath=//a[@href='/dyscypliny/2-tenis-stolowy' and text()='Tenis stołowy']
    #Sleep              2
    Wait Until Element Is Visible    xpath=//a[@class='add_entity_link' and @href='/dyscypliny/2-tenis-stolowy/ranking' and text()='» więcej...']    2s
    Click Link         xpath=//a[@class='add_entity_link' and @href='/dyscypliny/2-tenis-stolowy/ranking' and text()='» więcej...']
    #Sleep              2
    Log To Console    Checking player: ${PLAYER_NAME}...
    Wait Until Element Is Visible    xpath=//a[contains(@class, 'name') and contains(text(), '${PLAYER_NAME}')]    2s
    Click Link         xpath=//a[contains(@class, 'name') and contains(text(), '${PLAYER_NAME}')]
    #Sleep              2
    ${ranking_points}=    Get Text    xpath=//tr[td[text()='Punkty rankingowe:']]//a[contains(@class, 'name')]
    Log To Console    Player: ${PLAYER_NAME} found, ranking points: ${ranking_points}.
    Log               Player: ${PLAYER_NAME} found, ranking points: ${ranking_points}.
    #Sleep              2
