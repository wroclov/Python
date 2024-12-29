*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Process
Suite Setup       Open Browser    https://turniejeamatorskie.info    Chrome
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://turniejeamatorskie.info
${DESKTOP_SIZE}   1920    1080
${TABLET_SIZE}    768     1024
${MOBILE_SIZE}    375     667

*** Test Cases ***
Verify Page Title
    [Documentation]    Ensure the page title follows the expected format.
    ${title}=    Get Title
    Log    Current page title: ${title}
    ${length}=    Get Length    ${title}
    Log    Length of title: ${length}
    Should Match Regexp    ${title}    Kalendarz imprez -[\\w\\s]+\\d{4} - TurniejeAmatorskie\.info



Check for Broken Links
    [Documentation]    Verify that all links on the page are functional.
    ${links}=    Get WebElements    xpath=//a
    FOR    ${link}    IN    @{links}
        ${href}=    Get Element Attribute    ${link}    href
        Log    Checking link: ${href}
        Run Keyword And Continue On Failure    Check Link Accessibility    ${href}
    END

Responsive Design Testing
    [Documentation]    Check the site layout on desktop, tablet, and mobile resolutions.
    Set Window Size    ${DESKTOP_SIZE}[0]    ${DESKTOP_SIZE}[1]
    Sleep    2
    Capture Page Screenshot    desktop_view.png
    Set Window Size    ${TABLET_SIZE}[0]    ${TABLET_SIZE}[1]
    Sleep    2
    Capture Page Screenshot    tablet_view.png
    Set Window Size    ${MOBILE_SIZE}[0]    ${MOBILE_SIZE}[1]
    Sleep    2
    Capture Page Screenshot    mobile_view.png

#Navigation Test
#    [Documentation]    Verify that navigation links function as expected.
#    Click Element    xpath=//a[contains(text(), 'Kalendarz imprez')]    # Updated locator
#    Sleep    2
#    Location Should Contain    /kalendarz-imprez

#Static Content Test
#    [Documentation]    Ensure key page content is present.
#    Page Should Contain Element    xpath=//h1[contains(text(), 'Turnieje')]
#    Page Should Contain    Regulamin

HTTPS Verification
    [Documentation]    Ensure the site uses HTTPS.
    ${current_url}=    Get Location
    Should Start With    ${current_url}    https
    Log    Current URL uses HTTPS: ${current_url}

Page Load Screenshot
    [Documentation]    Take a screenshot after page load.
    Sleep    3
    Capture Page Screenshot    homepage_loaded.png

*** Keywords ***
Check Link Accessibility
    [Arguments]    ${url}
    ${response}=    Run Process    curl    -I    ${url}    shell=True
    Log    Response: ${response.stdout}
    Should Contain    ${response.stdout}    200 OK
