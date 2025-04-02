class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome

        self.preco = preco
        self.quantidade = quantidade

    def get_id(self):
        return self.id

    def set_id(self):
        return self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
