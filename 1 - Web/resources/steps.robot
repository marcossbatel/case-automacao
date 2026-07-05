*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Resource    ./locators.robot
Resource    ./environment.robot

*** Variables ***
${SCREENSHOT_DIR}    ${EXECDIR}/results/screenshots

*** Keywords ***
Tirar Screenshot
    [Arguments]    ${name}
    Create Directory    ${SCREENSHOT_DIR}
    Capture Page Screenshot    ${SCREENSHOT_DIR}/${name}.png

Abrir Pagina de Login do SauceDemo
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --disable-features\=PasswordLeakDetection
    Call Method    ${options}    add_argument    --disable-save-password-bubble
    Call Method    ${options}    add_argument    --disable-password-manager-reauthentication
    Call Method    ${options}    add_argument    --headless\=new
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method    ${options}    add_argument    --disable-dev-shm-usage
    Call Method    ${options}    add_argument    --window-size\=1920,1080
    Open Browser
    ...    ${BASE_URL}
    ...    browser=${BROWSER}
    ...    options=${options}
    Maximize Browser Window
    Wait Until Page Contains Element    ${USERNAME_INPUT}
    Tirar Screenshot    login_page

Remover Backpack do carrinho
    Click Button    id:remove-sauce-labs-backpack
    Page Should Contain    Your Cart
    Page Should Not Contain    Sauce Labs Backpack


Realizar login com credenciais válidas
    Input Text    ${USERNAME_INPUT}    ${USERNAME}
    Input Password    ${PASSWORD_INPUT}    ${PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Wait Until Location Contains    /inventory.html
    Wait Until Page Contains Element    ${INVENTORY_LIST}
    Tirar Screenshot    inventory_page

Adicionar Backpack ao Carrinho
    Click Button    ${BACKPACK_ADD_BUTTON}
    Wait Until Element Contains    ${CART_BADGE}    1
    Tirar Screenshot    cart_with_item

Abrir Carrinho
    Click Link    ${CART_LINK}
    Wait Until Page Contains    ${CART_TITLE}
    Page Should Contain    ${CART_ITEM_NAME}
    Tirar Screenshot    cart_page

Finalizar Checkout
    Click Button    ${CHECKOUT_BUTTON}
    Input Text    ${FIRST_NAME_INPUT}    ${FIRST_NAME}
    Input Text    ${LAST_NAME_INPUT}    ${LAST_NAME}
    Input Text    ${ZIP_CODE_INPUT}    ${ZIP_CODE}
    Click Button    ${CONTINUE_BUTTON}
    Tirar Screenshot    checkout_overview
    Wait Until Location Contains    /checkout-step-two.html
    Wait Until Page Contains    Payment Information
    Click Button    xpath://button[contains(., 'Finish')]
    Wait Until Page Contains    ${CHECKOUT_COMPLETE_MESSAGE}
    Tirar Screenshot    checkout_complete

Verificar se a Home Page está aberta
    Location Should Be    ${INVENTORY_URL}
    Page Should Contain Element    ${INVENTORY_LIST}
    Tirar Screenshot    inventory_validation

Finalizar Sessão
    Tirar Screenshot    session_closed
    Close Browser
