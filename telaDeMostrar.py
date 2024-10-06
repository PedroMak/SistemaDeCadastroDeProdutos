import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from DataBase import *

def telaDeMostrar():
    root = tk.Tk()
    root.title("Banco de dados")
    root.resizable(False, False)
    root.geometry("300x500")

    #labelTeste = tk.Label(root, text=mostrarBanco())
    #labelTeste.place(x=150,y=250)

    tv = ttk.Treeview(root, columns=('nome', 'preco', 'qtd', 'codigo'), show='headings')
    tv.column('nome',minwidth=0, width=58)
    tv.column('preco',minwidth=0, width=58)
    tv.column('qtd',minwidth=0, width=58)
    tv.column('codigo',minwidth=0, width=58)
    tv.heading('nome', text="NOME")
    tv.heading('preco', text="PRECO")
    tv.heading('qtd', text="QTD")
    tv.heading('codigo', text="CODIGO")
    linhasDB = mostrarBanco()
    for linha in linhasDB:
        tv.insert("",tk.END,values=linha)
    tv.place(x=35, y=130)