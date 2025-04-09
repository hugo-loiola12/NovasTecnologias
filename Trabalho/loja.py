# Loja.py

from pagamento import Pagamento
from carrinho import Carrinho


class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print("Produtos disponíveis:")
        for produto in self.produtos:
            print(produto)

    def aplicar_desconto(self, id_produto, percentual):
        for produto in self.produtos:
            if produto.id == id_produto:
                produto.aplicar_desconto(percentual)
                print(
                    f"Desconto aplicado em {produto.nome}. Novo preço: R${produto.preco:.2f}")
                return
        print("Produto não encontrado!")

    def adicionar_ao_carrinho(self, id_produto, quantidade):
        for produto in self.produtos:
            if produto.id == id_produto:
                if self.carrinho.adicionar_produto(produto, quantidade):
                    produto.estoque -= quantidade
                return
        print("Produto não encontrado!")

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        if total == 0:
            print("Carrinho vazio. Adicione produtos antes de finalizar a compra!")
            return

        print(f"\nTotal da compra: R${total:.2f}\n")
        metodo = input(
            "Escolha o método de pagamento (pix/cartao/boleto): ").strip().lower()

        sucesso = False
        if metodo == "pix":
            sucesso = Pagamento().pix(total)
        elif metodo == "cartao":
            sucesso = Pagamento().cartao(total)
        elif metodo == "boleto":
            sucesso = Pagamento().boleto(total)
        else:
            print("Método de pagamento inválido!")

        if sucesso:
            print("\nCompra finalizada com sucesso! Obrigado pela preferência.")
            self.carrinho.esvaziar()
        else:
            print("\nFalha no processamento do pagamento. Tente novamente.")
