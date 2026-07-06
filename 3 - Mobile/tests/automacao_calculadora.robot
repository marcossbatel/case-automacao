*** Settings ***
Resource    ../resources/base.robot
Test Setup    Abrir Calculadora
Test Teardown    Fechar Calculadora

*** Test Cases ***
CT01 - Validar soma
    [Tags]    CT01
    Realizar Soma

CT02 - Validar subtração
    [Tags]    CT02
    Realizar Subtracao

CT03 - Validar multiplicação
    [Tags]    CT03
    Realizar Multiplicacao

CT04 - Validar divisão
    [Tags]    CT04
    Realizar Divisao
