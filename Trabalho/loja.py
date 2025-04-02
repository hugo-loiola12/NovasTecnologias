
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
            print("Carrinho vazio. Adicione produtos antes de finalizar a compra.")
            return

        print(f"Total da compra: R${total:.2f}")
        try:
            valor_pago = float(input("Digite o valor pago: R$"))
        except ValueError:
            print("Valor inválido!")
            return

        if valor_pago < total:
            print("Pagamento insuficiente!")
        else:
            troco = valor_pago - total
            print(f"Pagamento realizado com sucesso! Troco: R${troco:.2f}")
            self.carrinho.esvaziar()
