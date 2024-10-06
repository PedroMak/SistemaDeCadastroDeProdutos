import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *

def telaDeCadastro():
    root = tk.Tk()
    root.title("Tela de Cadastro")
    root.resizable(False, False)
    root.geometry("300x500")

    #nomeDoProduto, Preço, QuantidadeNoEstoque, (ID)

    #Parte das labels
    labelNome = tk.Label(root, text="Nome do Produto")
    labelNome.place(x = 100, y = 50)
    labelPreco = tk.Label(root, text = "Preço do Produto")
    labelPreco.place(x = 100, y = 120)
    labelQuantidade = tk.Label(root, text = "Quantidade no Estoque")
    labelQuantidade.place(x = 100, y = 185)
    labelCodigoDeBarra = tk.Label(root, text = "Código de Barras")
    labelCodigoDeBarra.place(x=100, y=250)

    entryNome = tk.Entry(root)
    #entryNome.bind(lambda x:textoEntradaNome.set(entryNome.get()+x.char))
    entryNome.place(x = 100, y = 70)

    entryPreco = tk.Entry(root)
    entryPreco.place(x = 100, y = 140)

    entryQuantidade = tk.Entry(root)
    entryQuantidade.place(x = 100, y = 205)

    entryCodigo = tk.Entry(root)
    entryCodigo.place (x = 100, y = 270)

    # Parte dos botões
    buttonCommit = tk.Button(root, text="Cadastrar")
    buttonCommit['command'] = lambda: insertIntoDB(entryNome.get(), float(entryPreco.get()), int(entryQuantidade.get()))
    buttonCommit.place(x = 100, y = 315)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()