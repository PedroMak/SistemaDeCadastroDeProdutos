import sqlite3 as sq

#Configurações do SQLITE3
connection = sq.connect("DBmain")
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS Produtos(nome TEXT, preco REAL, qto INTEGER, codigo INTEGER)"
cursor.execute(query)


def insertIntoDB(nome, preco, qto, codigo):
    cursor.execute("INSERT INTO Produtos VALUES('" + nome + "', '" + str(preco) + "', '" + str(qto) + "', '" + str(codigo) + "')")
    connection.commit()

def mostrarBanco():
    lista = cursor.execute("SELECT * FROM Produtos").fetchall()
    print(lista)
    return lista
    
def buscarProduto(codigoBarra):
    nomeEQuantidade = cursor.execute("SELECT nome, qto FROM Produtos WHERE codigo LIKE '" + str(codigoBarra) + "'").fetchone()
    print(nomeEQuantidade)
    return nomeEQuantidade

#def atualizarBanco():
    