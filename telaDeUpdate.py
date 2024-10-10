import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *
from telaProdutoBuscado import *

def telaDeUpdate():
    root = tk.Tk()
    root.title("Tela de Update")
    root.resizable(False, False)
    root.geometry("300x500")

    labelBusca = tk.Label(root, text = "Buscar Produto")
    labelBusca.place(x = 100, y = 100)

    entradaBusca = tk.Entry(root)
    entradaBusca.place(x = 100, y = 125)

    
    buscaButton = tk.Button(root, text = "Pesquisar")
    buscaButton['command'] = lambda :produtoBuscado(entradaBusca.get())
    buscaButton.place(x = 100, y = 150)

    labelAtualiza = tk.Label(root, text = "Atualizar Estoque")
    labelAtualiza.place(x = 100, y = 250)
    
    # Entry de codigo para atualizar
    labelCodigoParaAtualizar = tk.Label(root, text = "Código:")
    labelCodigoParaAtualizar.place(x = 50, y = 275)

    codigoDoProdutoParaAtualizar = tk.Entry(root)
    codigoDoProdutoParaAtualizar.place(x = 100, y =275)
    
    # Entry de qt para atualizar
    labelQtdAtualizar = tk.Label(root, text = "Quantidade:")
    labelQtdAtualizar.place(x = 25, y = 300)
    
    atualizaBox = tk.Entry(root)
    atualizaBox.place(x = 100, y = 300)

    #TODO: comando para atualizar a quantidade no estoque
    atualizaButton = tk.Button(root, text= "Atualizar")
    atualizaButton['command'] = lambda : atualizarBanco(codigoDoProdutoParaAtualizar.get(), atualizaBox.get())
    atualizaButton.place(x = 100 ,y = 325)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()