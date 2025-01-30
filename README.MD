# CRUD de Produtos

Um projeto em Python para gerenciar produtos usando MongoDB.

**Repositório**: [CRUD DE PRODUTOS - GitHub](https://github.com/LucasS059/CRUD-DE-PRODUTOS.git)

## Funcionalidades

- Adicionar, listar, atualizar e remover produtos.

## Tecnologias

- Python
- MongoDB (PyMongo)
- dotenv

## Como Usar

### 1. Clone o Repositório

```bash
git clone https://github.com/LucasS059/CRUD-DE-PRODUTOS.git
cd CRUD-DE-PRODUTOS
```

### 2. Configure o MongoDB

- **MongoDB Local**: Crie um arquivo `.env` com a seguinte linha:

  ```env
  MONGO_URI=mongodb://localhost:27017
  ```

- **MongoDB Atlas**: Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), configure um banco de dados e um usuário, e use a URL de conexão parecida com:

  ```env
  MONGO_URI=mongodb+srv://<usuario>:<senha>@cluster0.mongodb.net/<nome-do-banco>?retryWrites=true&w=majority
  ```

  Substitua `<usuario>`, `<senha>` e `<nome-do-banco>` com suas credenciais e o nome do banco criado no Atlas.

- **Banco de Dados e Coleção**: No código, o banco de dados e a coleção são definidos como:

  ```python
  db = client["loja"]  # Nome do banco de dados
  colecao = db["produtos"]  # Nome da coleção
  ```

  Caso queira usar outro banco de dados ou coleção, basta alterar os nomes de `"loja"` e `"produtos"` no código acima.

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Projeto

```bash
python app.py
```
