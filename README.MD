# CRUD de Produtos com MongoDB e Python

Este é um projeto simples em Python para gerenciar produtos utilizando o MongoDB. Ele foi desenvolvido como uma maneira de aprimorar os meus estudos com o MongoDB e Python, criando um CRUD básico (Criar, Ler, Atualizar e Deletar) para gerenciar um inventário de produtos.

## Como Usar

### 1. Clone o Repositório

Primeiro, clone o repositório para sua máquina:

```bash
git clone https://github.com/LucasS059/CRUD-DE-PRODUTOS.git
cd CRUD-DE-PRODUTOS
```

### 2. Configure o MongoDB

Você tem duas opções para configurar o MongoDB: **MongoDB Atlas** (para usar na nuvem) ou **MongoDB Local** (para usar na sua máquina).

#### Opção 1: Usando o MongoDB Atlas (nuvem)

O MongoDB Atlas é uma solução de banco de dados como serviço (DBaaS) oferecida pela MongoDB. Para configurá-lo, siga os passos abaixo:

1. Crie uma conta em [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) se ainda não tiver uma.
2. Crie um **Cluster** no Atlas (pode ser na opção gratuita).
3. Crie um **usuário** com permissões de leitura e escrita para acessar o banco de dados.
4. Crie um banco de dados e uma coleção dentro do seu cluster.
5. Após configurar o cluster, copie a **URL de Conexão** fornecida pelo Atlas. Ela será algo como:

   ```env
   MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/<nome-do-banco>?retryWrites=true&w=majority
   ```

   - Substitua `<usuario>` e `<senha>` pelo usuário e senha criados no Atlas.
   - Substitua `<nome-do-banco>` pelo nome do banco de dados que você criou no Atlas.

6. **Crie um arquivo `.env`** na raiz do projeto com o conteúdo abaixo, contendo a URL de conexão:

   ```env
   MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/<nome-do-banco>?retryWrites=true&w=majority
   ```

#### Opção 2: Usando o MongoDB Local (Compass ou Servidor Local)

Se você deseja rodar o MongoDB localmente, siga os passos abaixo para configurar a conexão.

1. **Instale o MongoDB**:

   - **Windows**: [Baixar MongoDB para Windows](https://www.mongodb.com/try/download/community)
   - **Linux/Mac**: Siga as instruções [aqui](https://docs.mongodb.com/manual/installation/).

2. **Inicie o MongoDB**:
   - Se você estiver usando o **MongoDB Compass**, basta abrir o Compass e conectar-se localmente usando a string de conexão padrão:
     ```env
     MONGO_URI=mongodb://localhost:27017
     ```
     Isso conecta ao MongoDB rodando na sua máquina local.

3. **MongoDB Compass**: Se você usar o MongoDB Compass, ao abrir o Compass, você verá a opção de conectar-se usando `mongodb://localhost:27017`. Escolha essa opção e você poderá visualizar e gerenciar seus bancos de dados e coleções localmente.

4. **Crie um banco de dados e coleção** no MongoDB Compass ou diretamente no MongoDB Local, caso ainda não tenha feito isso.

5. **Crie o arquivo `.env`** na raiz do projeto com o conteúdo abaixo:

   ```env
   MONGO_URI=mongodb://localhost:27017
   ```

---

### 3. Alterar o Nome do Banco de Dados e da Coleção

No código Python, você pode alterar o nome do banco de dados e da coleção. Para fazer isso, basta alterar as variáveis abaixo:

```python
# Nome do banco de dados
db = client["nome_do_seu_banco"]

# Nome da coleção
colecao = db["nome_da_sua_colecao"]
```

Substitua `nome_do_seu_banco` e `nome_da_sua_colecao` pelos nomes desejados para o banco e a coleção que você criou no MongoDB (seja no Atlas ou no MongoDB local).

---

### 4. Instalar Dependências

Para rodar o projeto, você precisa instalar as dependências. Utilize o `pip` para instalar os pacotes necessários:

```bash
pip install -r requirements.txt
```

---

### 5. Rodar o Projeto

Após configurar o MongoDB e as dependências, basta rodar o arquivo `crud.py` para interagir com o sistema:

```bash
python produtos.py
```
