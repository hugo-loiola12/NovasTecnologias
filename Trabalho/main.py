

from loja import Loja
from produto import Produto


def main():
    loja = Loja()
    loja.adicionar_produto(Produto(1, "Camiseta", 50.0, 10))
    loja.adicionar_produto(Produto(2, "Calça", 80.0, 5))
    loja.adicionar_produto(Produto(3, "Tênis", 120.0, 3))
    loja.adicionar_produto(Produto(4, "Jaqueta", 200.0, 2))
    loja.adicionar_produto(Produto(5, "Boné", 30.0, 15))

    while True:
        print("\n=== Menu da Loja ===")
        print("1. Visualizar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Aplicar desconto em um produto")
        print("4. Visualizar itens do carrinho")
        print("5. Finalizar compra")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.listar_produtos()
        elif opcao == "2":
            try:
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Digite a quantidade desejada: "))
                loja.adicionar_ao_carrinho(id_produto, quantidade)
            except ValueError:
                print("Entrada inválida!")
        elif opcao == "3":
            try:
                id_produto = int(input("Digite o ID do produto: "))
                percentual = float(input("Digite o percentual de desconto: "))
                loja.aplicar_desconto(id_produto, percentual)
            except ValueError:
                print("Entrada inválida!")
        elif opcao == "4":
            loja.carrinho.mostrar_itens()
        elif opcao == "5":
            loja.finalizar_compra()
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
