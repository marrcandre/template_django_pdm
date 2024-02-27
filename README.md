# Template de projeto Django com DRF e PDM

Esse é um template de projeto Django com DRF, PDM e muito mais. Ele já vem com algumas configurações e pacotes pré-instalados, como o [PDM](https://pdm.fming.dev/), [Django](https://www.djangoproject.com/), [Django REST Framework](https://www.django-rest-framework.org/), [PostgreSQL](https://www.postgresql.org/), [SQLite](https://www.sqlite.org/index.html), [Swagger](https://swagger.io/), [Black](), [isort](), [Fl0](), [Cloudinary](), [Corsheaders](), [Django-Extensions](), [Django-Filter](), [dotenv](), [drf-spectacular](), [gunicon](), [netifaces](), [rest-framework-simplejwt]() e [whitenoise]().

Esse template já está pronto para ser utilizado em produção, com o [Fl0](http://fl0.com) e o [PostgreSQL](https://www.postgresql.org/). Mas também pode ser utilizado em desenvolvimento, com o [PDM](https://pdm.fming.dev/) e o [SQLite](https://www.sqlite.org/index.html).

O template também já vem com alguns arquivos de configuração pré-configurados, como:

- `pyproject.toml`: Arquivo de configuração do PDM.
- `Procfile`: Arquivo de configuração do Fl0.
- `settings.py`: Arquivo de configuração do Django.
- `urls.py`: Arquivo de configuração das rotas do Django.
- `wsgi.py`: Arquivo de configuração do Gunicorn.
- `.env.exemplo`: Arquivo de exemplo de configuração das variáveis de ambiente.
- `.gitignore`: Arquivo de configuração do Git, para ignorar arquivos e diretórios.

O template também traz o usuário padrão modificado, com o login sendo feito com o `e-mail` e não com o `username`. Inclusões de campos, como `telefone`, `data de nascimento` e `foto de perfil`, podem ser feitas facilmente.


## Instalação e Configuração

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu sistema.

2. Crie um novo projeto a partir desse template:
- Acesse o _template_ em https://github.com/marrcandre/template_django_pdm.
- Clique no botão `Use this template` em `Create a new repository`.
- Preencha as informações solicitadas:
  - `Owner`: <seu usuário no GitHub>
  - `Repository name`: `livraria`
- Click no botão `Create repository`.

3. Abra o projeto no vscode e execute o terminal.

2. Crie um ambiente virtual usando o [PDM](https://pdm.fming.dev/):

   ```
   pdm install
   ```

3. Crie o arquivo .env, a partir do arquivo .env.exemplo, e configure as variáveis de ambiente:

   ```
   cp .env.exemplo .env
   ```

4. Execute o servidor de desenvolvimento:

   ```
   pdm run dev
   ```

5. Acesse a API em http://localhost:19003/api/

## Uso da API

A documentação completa dos endpoints da API e exemplos de uso estão disponíveis na [Documentação da API](http://localhost:19003/api/swagger/).

## Comandos Úteis

- `pdm run dev`: Executa o servidor de desenvolvimento. Antes de executar o servidor, descobre o endereço IP da máquina e atualiza o arquivo `.env` com o endereço IP.
- `pdm run migrate`: Executa as migrações do banco de dados. Antes de executar o `migrate`, executa o `makemigrations`. Depois de executar o `migrate`, executa o `graph_models`, atualizando o diagrama de classes dos modelos do projeto.

## Detalhes do Projeto

Esse projeto utiliza os seguintes pacotes e tecnologias:

- [PDM](https://pdm.fming.dev/): Gerenciador de pacotes e ambiente virtual para Python.
- [Django](https://www.djangoproject.com/): Framework web de alto nível escrito em Python.
- [Django REST Framework](https://www.django-rest-framework.org/): Framework para desenvolvimento de APIs REST com Django.
- [PostgreSQL](https://www.postgresql.org/): Banco de dados relacional, utilizado no ambiente de produção.
- [SQLite](https://www.sqlite.org/index.html): Banco de dados relacional, utilizado no ambiente de desenvolvimento.
- [Swagger](https://swagger.io/): Framework para documentação de APIs REST.
- [Black](https://github.com/psf/black): Ferramenta de formatação de código Python.
- [isort](https://pycqa.github.io/isort/): Ferramenta de ordenação de imports Python.
- [Fl0](http://fl0.com): Ferramenta de _deploy_ de aplicações backend e banco de dados.
- [Cloudinary](https://cloudinary.com/): Serviço de armazenamento de arquivos estáticos em nuvem.
- [Corsheaders](https://pypi.org/project/django-cors-headers/): Pacote para habilitar o CORS em aplicações Django. O CORS é utilizado para permitir que aplicações frontend acessem a API.
- [Django-Extensions](https://django-extensions.readthedocs.io/en/latest/): Pacote com extensões para o Django, como o `shell_plus`, que permite acessar o shell do Django com todos os modelos importados e o comando `graph_models`, que gera um diagrama de classes dos modelos do projeto.
- [Django-Filter](https://django-filter.readthedocs.io/en/stable/): Pacote para filtragem, ordenação e paginação de dados em APIs REST.
- [dotenv](https://pypi.org/project/python-dotenv/): Pacote para carregar variáveis de ambiente a partir de um arquivo `.env`.
- [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/): Pacote para geração de documentação de APIs REST com o Swagger.
- [gunicon](https://gunicorn.org/): Pacote para servir aplicações Django em produção.
- [netifaces](https://pypi.org/project/netifaces/): Pacote para obter o endereço IP da máquina.
- [rest-framework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/): Pacote para autenticação JWT em APIs REST.
- [whitenoise](http://whitenoise.evans.io/en/stable/): Pacote para servir arquivos estáticos em aplicações Django.

## Licença

Este projeto está licenciado sob a [Licença GPL](https://www.gnu.org/licenses/gpl-3.0.html), uma licença de software livre.



