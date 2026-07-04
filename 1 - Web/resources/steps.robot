*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Resource    ./locators.robot
Resource    ./environment.robot

*** Variables ***
${SCREENSHOT_DIR}    ${EXECDIR}/results/screenshots

*** Keywords ***
Take Screenshot Step
    [Arguments]    ${name}
    Create Directory    ${SCREENSHOT_DIR}
    Capture Page Screenshot    ${SCREENSHOT_DIR}/${name}.png

Open SauceDemo Login Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --disable-features\=PasswordLeakDetection
    Call Method    ${options}    add_argument    --disable-save-password-bubble
    Call Method    ${options}    add_argument    --disable-password-manager-reauthentication
    Open Browser
    ...    ${BASE_URL}
    ...    browser=${BROWSER}
    ...    options=${options}
    Maximize Browser Window
    Wait Until Page Contains Element    ${USERNAME_INPUT}
    Take Screenshot Step    login_page

Realizar login com credenciais válidas
    Input Text    ${USERNAME_INPUT}    ${USERNAME}
    Input Password    ${PASSWORD_INPUT}    ${PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Wait Until Location Contains    /inventory.html
    Wait Until Page Contains Element    ${INVENTORY_LIST}
    Take Screenshot Step    inventory_page

Add Backpack To Cart
    Click Button    ${BACKPACK_ADD_BUTTON}
    Wait Until Element Contains    ${CART_BADGE}    1
    Take Screenshot Step    cart_with_item

Open Cart
    Click Link    ${CART_LINK}
    Wait Until Page Contains    ${CART_TITLE}
    Page Should Contain    ${CART_ITEM_NAME}
    Take Screenshot Step    cart_page

Finish Checkout
    Click Button    ${CHECKOUT_BUTTON}
    Input Text    ${FIRST_NAME_INPUT}    ${FIRST_NAME}
    Input Text    ${LAST_NAME_INPUT}    ${LAST_NAME}
    Input Text    ${ZIP_CODE_INPUT}    ${ZIP_CODE}
    Click Button    ${CONTINUE_BUTTON}
    Take Screenshot Step    checkout_overview
    Wait Until Location Contains    /checkout-step-two.html
    Wait Until Page Contains    Payment Information
    Click Button    xpath://button[contains(., 'Finish')]
    Wait Until Page Contains    ${CHECKOUT_COMPLETE_MESSAGE}
    Take Screenshot Step    checkout_complete

Verify Inventory Page Is Open
    Location Should Be    ${INVENTORY_URL}
    Page Should Contain Element    ${INVENTORY_LIST}
    Take Screenshot Step    inventory_validation

Close SauceDemo Session
    Take Screenshot Step    session_closed
    Close Browser
