*** Settings ***
Resource          ../resources/steps.robot
Test Setup        Abrir Pagina de Login do SauceDemo
Test Teardown     Finalizar Sessão

*** Test Cases ***
CT01 - Acessar a home page após login
    [Documentation]    Verificar se o usuário consegue acessar a home page após login com credenciais válidas
    [Tags]    regressivo    CT01
    Realizar login com credenciais válidas
    Verificar se a Home Page está aberta

CT02 - Adicionar item ao carrinho e validar na página do carrinho
    [Documentation]    Adicionar item ao carrinho e validar na página do carrinho
    [Tags]    CT02
    Realizar login com credenciais válidas
    Adicionar Backpack ao Carrinho
    Abrir Carrinho

CT03 - Adicionar e remover o item do carrinho
    [Documentation]    Adicionar e remover o item do carrinho
    [Tags]    CT03
    Realizar login com credenciais válidas
    Adicionar Backpack ao Carrinho
    Abrir Carrinho
    Remover Backpack do carrinho


CT04 - Adicionar item ao carrinho e finalizar compra
    [Documentation]    Adicionar item ao carrinho, preencher informações de checkout e finalizar a compra
    [Tags]    regressivo    CT04
    Realizar login com credenciais válidas
    Adicionar Backpack ao Carrinho
    Abrir Carrinho
    Finalizar Checkout


