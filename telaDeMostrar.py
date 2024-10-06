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

    tv = ttk.Treeview(root, columns=('nome', 'preco', 'qtd'), show='headings')
    tv.column('nome',minwidth=0, width=50)
    tv.column('preco',minwidth=0, width=50)
    tv.column('qtd',minwidth=0, width=50)
    tv.heading('nome', text="NOME")
    tv.heading('preco', text="PRECO")
    tv.heading('qtd', text="QTD")
    linhasDB = mostrarBanco()
    for linha in linhasDB:
        tv.insert("",tk.END,values=linha)
    tv.place(x=80, y=130)