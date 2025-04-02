class Carrinho:

    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):

        if quantidade < 1 or quantidade > 99:
            print("Quantidade deve ser entre 1 e 99.")
            return False

        if quantidade > produto.estoque:
            print("Estoque insuficiente!")
            return False

        self.itens.append((produto, quantidade))
        print(f"{produto.nome} adicionado ao carrinho ({quantidade} unidades).")
        return True

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total

    def mostrar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        print("Itens no carrinho:")
        for produto, quantidade in self.itens:
            print(f"{produto.nome} - R${produto.preco:.2f} x {quantidade}")
        print(f"Total da compra: R${self.calcular_total():.2f}")

    def esvaziar(self):
        self.itens = []
