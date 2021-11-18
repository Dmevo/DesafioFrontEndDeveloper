class Produto:

    def __init__(self, id=None, nome=None, img=None, valor=None, valor_antigo=None, descricao=None, parcela=None, valor_parcela=None):
        self.id = id
        self.nome = nome
        self.img = img
        self.valor = valor
        self.valor_antigo = valor_antigo
        self.descricao = descricao
        self.parcela = parcela
        self.valor_parcela = valor_parcela

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_img(self):
        return self.img

    def set_img(self, img):
        self.img = img

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_valor_antigo(self):
        return self.valor_antigo

    def set_valor_antigo(self, valor_antigo):
        self.valor_antigo = valor_antigo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_parcela(self):
        return self.parcela

    def set_parcela(self, parcela):
        self.parcela = parcela

    def get_valor_parcela(self):
        return self.valor_parcela

    def set_valor_parcela(self, valor_parcela):
        self.valor_parcela = valor_parcela