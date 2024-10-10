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

    tv = ttk.Treeview(root, columns=('nome','qto'), show='headings')
    tv.column('nome',minwidth=0, width=90)
    tv.column('qto',minwidth=0, width=90)
    tv.heading('nome', text="NOME")
    tv.heading('qto', text="ESTOQUE")  
    produtoBuscado = buscarProduto(codigo)
    tv.insert("", tk.END,values=produtoBuscado)
    tv.place(x=35, y=130)
    