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
    labelNome.place(x = 100, y = 100)
    labelPreco = tk.Label(root, text = "Preço do Produto")
    labelPreco.place(x = 100, y = 200)
    labelQuantidade = tk.Label(root, text = "Quantidade no Estoque")
    labelQuantidade.place(x = 100, y = 300)

    entryNome = tk.Entry(root)
    #entryNome.bind(lambda x:textoEntradaNome.set(entryNome.get()+x.char))
    entryNome.place(x = 100, y = 120)

    entryPreco = tk.Entry(root)
    entryPreco.place(x = 100, y = 220)

    entryQuantidade = tk.Entry(root)
    entryQuantidade.place(x = 100, y = 320)

    # Parte dos botões
    buttonCommit = tk.Button(root, text="Cadastrar")
    buttonCommit['command'] = lambda: insertIntoDB(entryNome.get(), float(entryPreco.get()), int(entryQuantidade.get()))
    buttonCommit.place(x = 100, y = 360)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()