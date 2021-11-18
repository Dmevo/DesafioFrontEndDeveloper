from application import produto_lista
from application.model.entity.produto import Produto
import json

class ProdutoDAO:

    def __init__(self):
        self.produto_lista = produto_lista

    def mostrar_produto(self):
        return self.produto_lista

    def dict_to_list(self, json):
        list = []
        for product in json:
            produto = Produto()
            produto.set_id(product['id'])
            produto.set_nome(product['name'])
            produto.set_img(product['image'])
            produto.set_valor_antigo(product['oldPrice'])
            produto.set_valor(product['price'])
            produto.set_descricao(product['description'])
            parcela = product['installments']
            produto.set_parcela(parcela['count'])
            produto.set_valor_parcela(parcela['value'])
            list.append(produto)
        return list

    def listar_todos(self):
        resultado = []
        with open("application/json/products.json", "r") as file:
            produto_lista = json.load(file)
            resultado = self.dict_to_list(produto_lista)
        return resultado