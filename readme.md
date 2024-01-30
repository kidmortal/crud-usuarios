# CRUD Usuários
API que disponibiliza o cadastro, consulta, edição e exclusão de usuários.


## Como executar este código

1) Ter python (versão 3) instalado na máquina 

1) Instalar dependências    
```pip install -r requirements.txt```

2) executar aplicação flask  
```flask run```


## Endpoints

### Consulta usuários (method = GET)

* Retorna todos os usuários cadastrados  
http://localhost:5000/usuarios 

* Retorna usuário pelo id  
http://localhost:5000/usuario/{id} 

### Edita usuário (method = PUT)

* Altera informações do usuário com base no id e body  
http://localhost:5000/editar/{id} 

* Body:
```
{
    'Nome': string,
    'E-mail': string,
} 
```

### Deleta usuário (method = DELETE)
* Remove usuário a partir do id  
http://localhost:5000/deletar/{id} 

### Cadastra usuário (method = POST)
* Cria um novo usuário com base no body    
http://localhost:5000/cadastrar 

* Body:
```
{
    'id': int,
    'Nome': string,
    'E-mail': string,
}
```

## Melhorias/funcionalidades a serem incrementadas

1) Auto incremento do id ao cadastrar um novo usuário caso usuário não informe o id no body
2) Retornar "id já cadastrado" caso usuário informe um id já existente na hora do cadastro
3) Adicionar banco de dados
4) Desenvolver interface visual básica
