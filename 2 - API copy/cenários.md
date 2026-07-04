# Cenários de testes para os endpoints de posts

## Objetivo
Mapear os cenários de teste necessários para validar os três endpoints exemplificados:

- GET /posts?userId=1
- POST /posts
- GET /posts/1

## Cenários em Gherkin (Português Brasileiro)

### Cenário 1: Consultar posts por usuário
```gherkin
Funcionalidade: Consulta de posts
  Como usuário da API
  Quero consultar posts de um usuário específico
  Para validar a resposta retornada pelo endpoint GET /posts

  Cenário: Retornar posts do usuário informado
    Dado que o endpoint GET /posts?userId=1 está disponível
    Quando eu envio uma requisição GET para o endpoint
    Então o status da resposta deve ser 200
    E a resposta deve ser uma lista
    E cada item da lista deve possuir o campo userId igual a 1
    E cada item deve conter os campos id, title, body e userId
```

### Cenário 2: Criar um novo post
```gherkin
Funcionalidade: Criação de posts
  Como usuário da API
  Quero criar um novo post
  Para validar a criação via endpoint POST /posts

  Cenário: Criar um post com sucesso
    Dado que o endpoint POST /posts está disponível
    Quando eu envio uma requisição POST com os dados title "foo", body "bar" e userId 1
    Então o status da resposta deve ser 201
    E a resposta deve ser um objeto JSON
    E o objeto deve conter os campos id, title, body e userId
    E os valores enviados devem ser refletidos na resposta
```

### Cenário 3: Consultar um post por identificador
```gherkin
Funcionalidade: Consulta de post por id
  Como usuário da API
  Quero consultar um post específico pelo seu identificador
  Para validar a resposta do endpoint GET /posts/1

  Cenário: Retornar um post existente
    Dado que o endpoint GET /posts/1 está disponível
    Quando eu envio uma requisição GET para o endpoint
    Então o status da resposta deve ser 200
    E a resposta deve ser um objeto JSON
    E o objeto deve possuir o campo id igual a 1
    E o objeto deve conter os campos userId, title e body
```

### Cenário 4: Consultar posts de um usuário sem registros
```gherkin
Funcionalidade: Consulta de posts sem resultado
  Como usuário da API
  Quero consultar posts de um usuário que não possui registros
  Para validar o comportamento do endpoint GET /posts?userId=999

  Cenário: Retornar uma lista vazia quando não existem posts para o usuário
    Dado que o endpoint GET /posts?userId=999 está disponível
    Quando eu envio uma requisição GET para o endpoint
    Então o status da resposta deve ser 200
    E a resposta deve ser uma lista vazia
```

### Cenário 5: Consultar um post inexistente
```gherkin
Funcionalidade: Consulta de post inexistente
  Como usuário da API
  Quero consultar um post que não existe
  Para validar o comportamento do endpoint GET /posts/999

  Cenário: Retornar erro quando o post não existe
    Dado que o endpoint GET /posts/999 está disponível
    Quando eu envio uma requisição GET para o endpoint
    Então o status da resposta deve ser 404
    E a resposta deve ser um objeto vazio
```
