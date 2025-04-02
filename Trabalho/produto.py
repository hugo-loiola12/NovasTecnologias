class Produto:

    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def aplicar_desconto(self, percentual):
        self.preco *= (1 - percentual / 100)

    def __str__(self):
        return f"[{self.id}] {self.nome} - Preço: R${self.preco:.2f} | Estoque: {self.estoque}"
