import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *
from telaDeUpdate import *

def produtoBuscado():
    root = tk.Tk()
    root.title("Tela de Update")
    root.resizable(False, False)
    root.geometry("200x200")

    tv = ttk.Treeview(root, columns=('nome'), show='headings')
    tv.column('nome',minwidth=0, width=30)
    tv.heading('nome', text="NOME")    
    produtoBuscado = buscarProduto(entradaBusca.get())
    #TODO:como pegar o parametro pra função acima sendo q o parametro vem de outro arquivo (teladeupdate)
    #TODO: é pra ser um PopUp que mostra oque foi buscado, pode ser um treeview ou outra forma mais simples como uma label simples, mas sem () e ,  
    #TODO: O treeview por alguma razão não abre tbm
    tv.place(x=100, y=100)