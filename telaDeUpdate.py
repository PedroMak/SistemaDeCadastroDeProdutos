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

    intEntrada = tk.IntVar()
    entradaBusca = tk.Entry(root)
    entradaBusca.place(x = 100, y = 125)
    #entradaBusca.bind('<Key>', lambda x:)

    
    buscaButton = tk.Button(root, text = "Pesquisar")
    buscaButton['command'] = lambda :produtoBuscado(entradaBusca.get())
    buscaButton.place(x = 100, y = 150)

    labelAtualiza = tk.Label(root, text = "Atualizar Estoque")
    labelAtualiza.place(x = 100, y = 250)
    
    intQtdEntrada = tk.IntVar()
    atualizaBox = tk.Entry(root)
    atualizaBox.place(x = 100, y = 275)

    #TODO: comando para atualizar a quantidade no estoque
    atualizaButton = tk.Button(root, text= "Atualizar")
    #atualizaButton['comand'] =
    atualizaButton.place(x = 100 ,y = 295)

    # label id   
    # caixinha de digita ID
    # botao de buscar ID
    # telinha aqui que mostra as info do ID buscado  
    # caixa pra mudar a qtd.
    # botao de mudar quantidade

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()