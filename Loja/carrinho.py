class Carrinho:

    def __init__(self, produtos, itens):
        self.produtos = []
        self.itens = len(self.produtos)

    def get_produtos(self):
        return self.produtos

    def set_produtos(self, produtos):
        self.produtos = produtos

    def get_itens(self):
        return self.itens

    def set_itens(self, itens):
        self.itens = itens
