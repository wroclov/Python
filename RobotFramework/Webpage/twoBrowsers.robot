*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER_A}       chrome
${BROWSER_B}       firefox
${URL_1}           https://robotframework.org
${URL_2}           https://robocon.io
${URL_3}           https://github.com/robotframework
${URL_B}           https://github.com

*** Test Cases ***
Test Managing Multiple Browsers and Windows
    [Documentation]    Test opening multiple windows in BrowserA and a separate BrowserB, navigating between them, and retrieving locations.

    # Open BrowserA and its first window
    Open Browser    ${URL_1}    ${BROWSER_A}    alias=BrowserA
    ${handle_window_1}=    Get Window Handles
    Log    First window handle: ${handle_window_1[0]}
    # Window handles are unique identifiers assigned by the browser to each open window or tab in a Selenium session.
    # They allow Selenium to distinguish between different browser windows or tabs,
    # making it possible to switch between them programmatically.

    # Open the second window in BrowserA and navigate to a new URL
    Execute Javascript    window.open()
    ${handles_after_second}=    Get Window Handles
    ${handle_window_2}=    Set Variable    ${handles_after_second[-1]}
    Switch Window    ${handle_window_2}
    Go To    ${URL_2}
    Log    Second window handle: ${handle_window_2}

    # Open the third window in BrowserA and navigate to another URL
    Execute Javascript    window.open()
    ${handles_after_third}=    Get Window Handles
    ${handle_window_3}=    Set Variable    ${handles_after_third[-1]}
    Switch Window    ${handle_window_3}
    Go To    ${URL_3}
    Log    Third window handle: ${handle_window_3}

    # Open BrowserB and its first window
    Open Browser    ${URL_B}    ${BROWSER_B}    alias=BrowserB
    ${browser_b_handles}=    Get Window Handles
    Log    BrowserB handles: ${browser_b_handles}
    ${browser_b_location}=    Get Location
    Log    BrowserB is at: ${browser_b_location}

    # Switch back to the second window in BrowserA
    Switch Window    ${handle_window_2}    browser=BrowserA
    ${second_window_location}=    Get Location
    Log    BrowserA second window is at: ${second_window_location}

    # Retrieve all locations for BrowserA
    @{locations_browser_a}=    Get Locations    browser=BrowserA
    Log    All locations in BrowserA: @{locations_browser_a}

    # Retrieve all locations across all browsers
    @{all_locations}=    Get Locations    browser=ALL
    Log    All locations across all browsers: @{all_locations}
    Log To Console    \nAll locations across all browsers: @{all_locations}

    Close All Browsers
