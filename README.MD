# CRUD de Produtos

Este é um projeto desenvolvido em Python para gerenciar produtos em um banco de dados MongoDB. A ideia surgiu como uma maneira de aprimorar meus estudos de MongoDB e Python, criando um CRUD (Create, Read, Update, Delete) completo para manipulação de produtos em um sistema de gerenciamento de estoque.

## Funcionalidades

- Adicionar, listar, atualizar e remover produtos.
- Cada produto contém informações como nome, preço e quantidade em estoque.

## Tecnologias

- **Python**: Linguagem utilizada para desenvolvimento do CRUD.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os produtos.
- **PyMongo**: Biblioteca para conectar e interagir com o MongoDB a partir do Python.
- **dotenv**: Biblioteca utilizada para carregar variáveis de ambiente (como a URL de conexão com o MongoDB) de forma segura.

## Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/LucasS059/CRUD-DE-PRODUTOS.git
cd CRUD-DE-PRODUTOS
```

## Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/LucasS059/CRUD-DE-PRODUTOS.git
cd CRUD-DE-PRODUTOS
```

### 2. Configure o MongoDB

Você tem duas opções para configurar o MongoDB: **MongoDB Atlas** (para uma solução em nuvem) ou **MongoDB Local** (para rodar em sua máquina).

#### Opção 1: Usando o MongoDB Atlas

O MongoDB Atlas é uma solução de banco de dados como serviço (DBaaS) fornecida pela MongoDB. Siga os passos abaixo para configurar a conexão:

1. Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) caso não tenha uma.
2. Crie um **Cluster** no Atlas (pode ser na opção gratuita).
3. Configure um **usuário** com permissões de leitura e escrita.
4. Crie um banco de dados e uma coleção para armazenar os dados dos produtos.
5. Após a configuração do Cluster, copie a **URL de Conexão** fornecida pelo Atlas. Ela será algo como:

   ```env
   MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/<nome-do-banco>?retryWrites=true&w=majority
   ```

   - Substitua `<usuario>` e `<senha>` pelo usuário e senha criados no Atlas.
   - Substitua `<nome-do-banco>` pelo nome do banco de dados que você criou no Atlas.

6. Crie um arquivo `.env` na raiz do projeto e insira a URL de conexão copiada:

   ```env
   MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/<nome-do-banco>?retryWrites=true&w=majority
   ```

#### Opção 2: Usando o MongoDB Local (Compass ou Servidor Local)

Caso queira rodar o MongoDB localmente, você pode usar o **MongoDB Compass** (interface gráfica) ou rodar o MongoDB diretamente na sua máquina.

1. **Instale o MongoDB**:

   - **Windows**: [Baixar MongoDB para Windows](https://www.mongodb.com/try/download/community)
   - **Linux/Mac**: Siga as instruções [aqui](https://docs.mongodb.com/manual/installation/).

2. **Inicie o MongoDB**:
   - Se você estiver usando o MongoDB Compass, basta abrir o Compass e conectar-se localmente usando a string de conexão padrão:
     ```env
     MONGO_URI=mongodb://localhost:27017
     ```
     - Isso conecta ao MongoDB rodando na sua máquina local.

3. **MongoDB Compass**: Se você usar o MongoDB Compass, ao abrir o Compass, você verá a opção de conectar-se usando `mongodb://localhost:27017`. Escolha essa opção e você poderá visualizar e gerenciar seus bancos de dados e coleções localmente.

4. **Crie um banco de dados e coleção** no MongoDB Compass ou no seu servidor local, se ainda não tiver feito isso.

5. **Crie o arquivo `.env`** na raiz do projeto e insira a URL de conexão para o MongoDB local:

   ```env
   MONGO_URI=mongodb://localhost:27017
   ```

   Essa string de conexão conecta ao MongoDB rodando localmente na porta 27017.

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Projeto

```bash
python app.py
```
