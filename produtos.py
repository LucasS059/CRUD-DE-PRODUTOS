from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["loja"]
colecao = db["produtos"]

def criar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Quantidade em estoque: "))
    
    produto = {"nome": nome, "preco": preco, "estoque": estoque}
    colecao.insert_one(produto)
    print(f"✅ Produto '{nome}' adicionado!\n")

def listar_produtos():
    produtos = list(colecao.find())
    if not produtos:
        print("\n⚠ Nenhum produto cadastrado!\n")
        return []

    print("\n📋 Produtos disponíveis:")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i} - {produto['nome']} | Preço: R${produto['preco']} | Estoque: {produto['estoque']}")
    print("\n")

    return produtos

def atualizar_produto():
    produtos = listar_produtos()
    if not produtos:
        return

    try:
        indice = int(input("Digite o número do produto que deseja atualizar: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("⚠ Número inválido.\n")
            return
    except ValueError:
        print("⚠ Entrada inválida. Digite um número.\n")
        return

    produto = produtos[indice]
    nome = produto["nome"]

    novo_preco = input("Novo preço (ou pressione Enter para manter o mesmo): ")
    novo_estoque = input("Novo estoque (ou pressione Enter para manter o mesmo): ")

    atualizacao = {}
    if novo_preco:
        atualizacao["preco"] = float(novo_preco)
    if novo_estoque:
        atualizacao["estoque"] = int(novo_estoque)

    if atualizacao:
        colecao.update_one({"nome": nome}, {"$set": atualizacao})
        print(f"✅ Produto '{nome}' atualizado com sucesso!\n")
    else:
        print("⚠ Nenhuma alteração feita.\n")

def deletar_produto():
    produtos = listar_produtos()
    if not produtos:
        return

    try:
        indice = int(input("Digite o número do produto que deseja remover: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("⚠ Número inválido.\n")
            return
    except ValueError:
        print("⚠ Entrada inválida. Digite um número.\n")
        return

    nome = produtos[indice]["nome"]
    colecao.delete_one({"nome": nome})
    print(f"✅ Produto '{nome}' removido!\n")

def menu():
    while True:
        print("\n📌 Sistema de Gerenciamento de Produtos")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto (Preço e/ou Estoque)")
        print("4 - Deletar Produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "5":
            print("🔚 Encerrando o sistema...")
            break
        else:
            print("⚠ Opção inválida! Tente novamente.")

menu()