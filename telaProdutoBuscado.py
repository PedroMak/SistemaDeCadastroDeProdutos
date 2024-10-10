import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *
from telaDeUpdate import *

def produtoBuscado(codigo):
    root = tk.Tk()
    root.title("Tela de Update")
    root.resizable(False, False)
    root.geometry("300x500")

    tv = ttk.Treeview(root, columns=('nome','qtd'), show='headings')
    tv.column('nome',minwidth=0, width=90)
    tv.column('qtd',minwidth=0, width=90)
    tv.heading('nome', text="NOME")
    tv.heading('qtd', text="ESTOQUE")  
    produtoBuscado = buscarProduto(codigo)
    tv.insert("", tk.END,values=produtoBuscado)
    tv.place(x=35, y=130)
    