*** Settings ***
Library    AppiumLibrary
Resource    ./locators.robot
Resource    ./environment.robot

*** Keywords ***
Abrir Aplicativo Calculadora
    Open Application    ${APPIUM_SERVER}
    ...    platformName=${PLATFORM_NAME}
    ...    platformVersion=${PLATFORM_VERSION}
    ...    deviceName=${DEVICE_NAME}
    ...    appPackage=${APP_PACKAGE}
    ...    appActivity=${APP_ACTIVITY}
    ...    automationName=${AUTOMATION_NAME}
    Wait Until Page Contains Element    ${RESULT_FIELD}

Fechar Aplicativo Calculadora
    Close Application

Pressionar Botões
    [Arguments]    @{buttons}
    FOR    ${button}    IN    @{buttons}
        Click Element    ${button}
    END

Obter Texto do Resultado
    ${resultado}=    Get Text    ${RESULT_FIELD}
    RETURN    ${resultado}
