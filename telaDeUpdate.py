import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *

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
    buscaButton['command'] = lambda :addLabel(buscarProduto(entradaBusca.get()), root)
    buscaButton.place(x = 100, y = 150)
    
    quadradoBranco = tk.Canvas(root, width = 150, height = 20, bg="white")
    quadradoBranco.place(x = 100, y = 190)

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

    atualizaButton = tk.Button(root, text= "Atualizar")
    atualizaButton['command'] = lambda : atualizarBanco(codigoDoProdutoParaAtualizar.get(), atualizaBox.get())
    atualizaButton.place(x = 100 ,y = 325)

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

#TODO: consertar isso aqui
def addLabel(tupla, root):
    # transforma o var em um StrinVar do TK
    #var = tk.StringVar()
    
    #combina Strings com .join mas nossa tupla tem string e int, dai não ta funcionando
    #varCombinado = " ".join(map(str,tupla))

    # na documentação ta escrito que tem que dar set com StringVar entao aqui nois ia dar o set com a tupla combinada em 1 só string
    #var.set(varCombinado)

    # Aparentemente pra isso aqui ficar dinâmico tem que usar textvariable no lugar de text, mas a gente não tem certeza
    newLabel = tk.Label(root, text=tupla)
    newLabel.place(x = 100, y = 190)


