from application import app
from flask import render_template
from application.model.entity.produto import Produto
from application.model.dao.produtoDAO import ProdutoDAO

produto_dao = ProdutoDAO()
produto_lista = produto_dao.listar_todos()

@app.route('/')
def index():
    return render_template("home.html", produto_lista=produto_lista[0:4])