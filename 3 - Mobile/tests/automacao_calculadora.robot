*** Settings ***
Resource    ../resources/steps.robot
Test Setup    Abrir Calculadora
Test Teardown    Fechar Calculadora

*** Test Cases ***
CT01 - Validar soma
    ${resultado}=    Realizar Soma
    Should Be Equal As Strings    ${resultado}    10

CT02 - Validar subtração
    ${resultado}=    Realizar Subtracao
    Should Be Equal As Strings    ${resultado}    3

CT03 - Validar multiplicação
    ${resultado}=    Realizar Multiplicacao
    Should Be Equal As Strings    ${resultado}    12

CT04 - Validar divisão
    ${resultado}=    Realizar Divisao
    Should Be Equal As Strings    ${resultado}    2
