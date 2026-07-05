*** Settings ***
Resource          ../resources/steps.robot
Test Setup        Open SauceDemo Login Page
Test Teardown     Close SauceDemo Session

*** Test Cases ***
CT01 - Acessar a home page após login
    [Documentation]    Verificar se o usuário consegue acessar a home page após login com credenciais válidas
    [Tags]    regressivo    CT01
    Realizar login com credenciais válidas
    Verify Inventory Page Is Open

CT02 - Adicionar item ao carrinho e validar na página do carrinho
    [Documentation]    Adicionar item ao carrinho e validar na página do carrinho
    [Tags]    CT02
    Realizar login com credenciais válidas
    Add Backpack To Cart
    Open Cart

CT03 - Adicionar e remover o item do carrinho
    [Documentation]    Adicionar e remover o item do carrinho
    [Tags]    CT03
    Realizar login com credenciais válidas
    Add Backpack To Cart
    Open Cart
    Click Button    id:remove-sauce-labs-backpack
    Page Should Contain    Your Cart
    Page Should Not Contain    Sauce Labs Backpack

CT04 - Adicionar item ao carrinho e finalizar compra
    [Documentation]    Adicionar item ao carrinho, preencher informações de checkout e finalizar a compra
    [Tags]    regressivo    CT04
    Realizar login com credenciais válidas
    Add Backpack To Cart
    Open Cart
    Finish Checkout


