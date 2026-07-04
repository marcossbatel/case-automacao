# Case Automação - Marcos Batel

O repositório tem como objetivo armazenar o conteúdo criado para o Case de Automação de Testes.

<br>

## Estruturas

O projeto está estruturado seguindo a ordem dos testes propostos, da seguinte forma:

### Pasta 1 - Web
**Requisito:** Criar um plano de testes para a aplicação https://www.saucedemo.com/inventory.html


### Pasta 2 - API
**Requisito:** Criar um plano e execução de testes para no mínimo TRES das APIs. Criar também testes de Performance.

**URL selecionada:** https://jsonplaceholder.typicode.com

**APIs selecionadas:** GET /posts, GET /posts/1, POST /posts


### Pasta 3 - Mobile
**Requisito:** Criar um script de automação para o App Calculadora de um dispositivo Android, com cálculo de operações básicas e validação do resultado; geração de relatório de execução. Criar a automação também para iOS.

<br>

## Execução

### 1 - Web

A automação de testes Web, da pasta "1 - Web" é feita utilizando `Robot Framework` em conjunto com o plugin `SeleniumLibrary`.

Ela é executada via Terminal através dos seguintes comandos, dentro do diretório `./1 - Web/`:


#### Execução básica
Usada para executar toda a automação

```bash
robot .\tests\automacao.robot
```


#### Execução com variáveis
Usada para alterar variáveis contidas na automação, variando dados. No exemplo abaixo, alteramos a variável USERNAME para simular diferentes comportamentos e validar os testes contidos na automação.

```bash
robot -v USERNAME:locked_out_user .\tests\saucedemo_tests.robot
```


#### Execução com Tags
Utilizada para executar cenários que contenham determinada Tag. No exemplo abaixo, executamos todos os cenários elencados para um possível teste regressivo da aplicação, por meio da tag "regressivo".

```bash
robot -i regressivo .\tests\automacao.robot
```

<br>

### 2 - API (Testes Funcionais)

A automação de testes de API, da pasta "2 - API" é feita utilizando `vitest` em conjunto com o plugin `axios`, para gerar o relatório de excecuções.

Sua execução se dá por meio do comando abaixo, dentro do diretório `./2 - API/`:

```bash
npm run test:vitest
```

O último parametro do comando acima se refere ao script. Para mais scripts, utilize:

`test:vitest` - Execução dos cenários com resultados exibidos apenas em console\
`test:ui` - Execução dos cenários com exibição do andamento dos testes em uma página HTML\
`test:report` - Execução dos cenários com geração de um report em HTML

<br>

### 2 - API (Testes Manuais)

Os testes manuais foram feitos utilizando a aplicação [Bruno](https://www.usebruno.com/). 

A collection foi disponibilizada no diretório `./2 - API/Collection Bruno`. Para configurar:

1. Baixe o Bruno no link acima;
2. Execute a aplicação;
3. Dentro do Bruno,  clique no botão '+' no canto superior esquerdo e selecione a opção `Open Collection`;
4. Navegue até a pasta `./2 - API/Collection Bruno`, selecione a pasta `Case QA - 2 API` e clique no botão "Selecionar pasta".

A collection será aberta e estará pronta para utilização.

<br>

### 2 - API (Testes de Performance)

Para os Testes de Performance, foi utilizado o `k6`. Foram criados 4 scripts:

`k6-get-posts.js` - Testes de performance isolados para o endpoint GET /posts\
`k6-post-posts.js` - Testes de performance isolados para o endpoint POST /posts\
`k6-get-posts-id.js` - Testes de performance isolados para o endpoint GET /posts/1\
`k6-consolidado.js` - Testes de performance para todos os endpoints acima, criando agrupamentos por endpoint e métricas customizadas para exibir os dados de cada um deles de forma isolada, bem como os dados consolidados dos três

Para a execução, utilize o comando abaixo, dentro do diretório `./2 - API/k6/`, variando o arquivo selecionado:

```bash
k6 run k6-get-posts-id.js
```

<br>

### 3 - Mobile

🚧 EM CONSTRUÇÃO 🚧
