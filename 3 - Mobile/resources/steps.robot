*** Settings ***
Resource    ./page_objects.robot

*** Keywords ***
Abrir Calculadora
    Abrir Aplicativo Calculadora

Fechar Calculadora
    Fechar Aplicativo Calculadora

Realizar Soma
    Pressionar Botões    ${BUTTON_5}    ${BUTTON_MAIS}    ${BUTTON_5}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    RETURN    ${resultado}

Realizar Subtracao
    Pressionar Botões    ${BUTTON_5}    ${BUTTON_MENOS}    ${BUTTON_2}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    RETURN    ${resultado}

Realizar Multiplicacao
    Pressionar Botões    ${BUTTON_6}    ${BUTTON_MULTIPLICA}    ${BUTTON_2}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    RETURN    ${resultado}

Realizar Divisao
    Pressionar Botões    ${BUTTON_8}    ${BUTTON_DIVIDE}    ${BUTTON_4}    ${BUTTON_EQUALS}
    ${resultado}=    Obter Texto do Resultado
    RETURN    ${resultado}
