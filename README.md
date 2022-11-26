# Gerenciador de funcionários

Repositório de gerenciamento de funcionários com objetivo de armazenar e exportar dados no formato específico para confecção de crachás.


## Variáveis de Ambiente

Para rodas este projeto, voce precisará adicionar as seguintes variáveis de ambiente. As que usei estão disponíveis como referência, mas fique a vontade para modificar informações sensíveis. Atenção na conexão de banco de dados!!! As que estão foram usadas tanto para desenvolvimento com sqlite quanto para conexão com postgres + docker.

<!-- To run this project, you will need to add the following environment variables to your .env file -->

`FLASK_SQLALCHEMY_DATABASE_URI` = Conexão com o banco de dados.

`FLASK_SECRET_KEY` = Necessário para utilização do WTForms.


## Rodar localmente

Clone o projeto e vá para o diretório

```
git clone https://github.com/rodrigofmeneses/flask-id-card-manager
cd flask-id-card-manager
```

Crie um ambiente virtual, ative-o

```
python -m venv .venv
source .venv/bin/activate # Linux
.venv/Scripts/activate # Windows
```

Instale as dependências

```
(.venv) pip install -r requirements.txt
```

Faça as migrações no banco de dados
```
flask db init
flask db migrate
flask db upgrade
```

Agora basta criar e popular o banco de dados. 

Uma pequena referência a comandos que criei (contidos no arquivo `app/ext/commands.py`)
| comando | Descrição|
| --- | --- |
| create-db |  Cria um banco de dados vazio |
| populate-db |  Popula o banco de dado com dados aleatórios |
| drop-db |  Apaga todos os dados |
| setup-db | Executa: drop-db  create-db populate-db |

Para usar os comandos é necessário `flask` antes do comando:
```
flask create-db
flask setup-db # Se preferir o banco de dados com exemplos
```

Rode o servidor de desenvolvimento com `flask run`, a saída esperada é algo assim:

```bash
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```


## Rodando os testes

Para rodar os testes, basta digitar `pytest` no terminal:

```bash
platform linux -- Python 3.10.8, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/rfm/workspace/flask-id-card-manager
plugins: Faker-15.3.1, cov-4.0.0
collected 20 items                                                                                                                                                                                 

tests/test_checkout.py ..           [ 10%]
tests/test_companies.py ......      [ 40%]
tests/test_employees.py ......      [ 70%]
tests/test_home.py ......           [100%]
```

## Docker

Atenção. Estou aprendendo a usar o docker, esse é meu primeiro projeto de teste.
Para rodar localmente com o postgres é preciso primeiro criar o banco de dados. Por algum motivo não consigo fazer as migrações com o flask migrate, então antes de repetir os comandos até `flask db migrate`, foi necessário manualmente criar um banco de dados com o nome desejado, no meu caso foi id_card.

Basicamente, com o banco de dados criado basta digitar o comando, `docker-compose up`.
Isso baixará as imagens do python e postgres, criará a rede e volumes necessárias para conectar o banco de dados e a aplicação e manter os arquivos salvos localmente caso o container seja excluido.
