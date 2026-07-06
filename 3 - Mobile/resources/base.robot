*** Settings ***
Resource    ./pages/page_calculadora.robot

*** Keywords ***
Abrir Calculadora
    Abrir Aplicativo Calculadora

Fechar Calculadora
    Fechar Aplicativo Calculadora

Realizar Soma
    Pressionar Botões    ${BUTTON_5}    ${BUTTON_MAIS}    ${BUTTON_5}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    Should Be Equal As Strings    ${resultado}    10

Realizar Subtracao
    Pressionar Botões    ${BUTTON_5}    ${BUTTON_MENOS}    ${BUTTON_2}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    Should Be Equal As Strings    ${resultado}    3

Realizar Multiplicacao
    Pressionar Botões    ${BUTTON_6}    ${BUTTON_MULTIPLICA}    ${BUTTON_2}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    Should Be Equal As Strings    ${resultado}    12

Realizar Divisao
    Pressionar Botões    ${BUTTON_8}    ${BUTTON_DIVIDE}    ${BUTTON_4}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    Should Be Equal As Strings    ${resultado}    2
