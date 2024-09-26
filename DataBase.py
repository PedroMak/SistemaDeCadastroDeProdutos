import sqlite3 as sq

#Configurações do SQLITE3
connection = sq.connect("DBmain")
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS Produtos(nome TEXT, preco REAL, qto INTEGER)"
cursor.execute(query)


def insertIntoDB(nome, preco, qto):
    cursor.execute("INSERT INTO Produtos VALUES('" + nome + "', '" + str(preco) + "', '" + str(qto) + "')")
    connection.commit()

def mostrarBanco():
    cursor.execute("SELECT * FROM Produtos").fetchall()