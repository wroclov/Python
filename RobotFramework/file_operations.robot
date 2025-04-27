*** Settings ***
Library    OperatingSystem

*** Variables ***
${FILE_PATH}    testfile.txt
${INITIAL_TEXT}    Hello, Robot!
${UPDATED_TEXT}    Hello, Robot Framework!

*** Test Cases ***

Create File
    [Documentation]    Create a file with some text.
    Create File    ${FILE_PATH}    ${INITIAL_TEXT}
    File Should Exist    ${FILE_PATH}

Read File
    [Documentation]    Read and verify content of the file.
    ${content}=    Get File    ${FILE_PATH}
    Should Be Equal As Strings    ${content}    ${INITIAL_TEXT}

Update File
    [Documentation]    Overwrite the file with new content.
    Remove File    ${FILE_PATH}
    Create File    ${FILE_PATH}    ${UPDATED_TEXT}
    ${new_content}=    Get File    ${FILE_PATH}
    Should Be Equal As Strings    ${new_content}    ${UPDATED_TEXT}

Delete File
    [Documentation]    Delete the file and verify it’s gone.
    Remove File    ${FILE_PATH}
    File Should Not Exist    ${FILE_PATH}
