# CRUD Usuários

API que disponibiliza o cadastro, consulta, edição e exclusão de usuários.

## Como executar este código

1. Ter python (versão 3) instalado na máquina

1. Instalar dependências  
   `pip install -r requirements.txt`

1. executar aplicação flask  
   `flask run`

## Endpoints

### Consulta usuários (method = GET)

- Retorna todos os usuários cadastrados  
  http://localhost:5000/users

- Retorna usuário pelo id  
  http://localhost:5000/users/{id}

### Edita usuário (method = PUT)

- Altera informações do usuário com base no id e body  
  http://localhost:5000/users/{id}

- Body:

```
{
    "Name": string,
    "Email": string
}
```

### Deleta usuário (method = DELETE)

- Remove usuário a partir do id  
  http://localhost:5000/users/delete/{id}

### Cadastra usuário (method = POST)

- Cria um novo usuário com base no body  
  http://localhost:5000/users

- Body:

```
{
    "id": int,
    "Name": string,
    "Email": string
}
```

## Melhorias/funcionalidades a serem incrementadas

1. Auto incremento do id ao cadastrar um novo usuário caso usuário não informe o id no body
2. Retornar "id já cadastrado" caso usuário informe um id já existente na hora do cadastro
3. Adicionar banco de dados
4. Desenvolver interface visual básica
