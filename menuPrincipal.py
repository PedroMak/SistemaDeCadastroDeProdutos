import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from telaDeCadastro import *
import telaDeUpdate
from DataBase import *

def menuPrincipal():
    # Configurações do TK
    root = tk.Tk()
    root.title("Tela Principal")
    root.resizable(False, False)
    root.geometry("300x500")
    

    # Botão de cadastro
    buttonCadastro = tk.Button(root, text="Cadastrar Produto")
    buttonCadastro['command'] = telaDeCadastro
    buttonCadastro.place(x = 100, y = 100)

    # Botão de atualizar
    buttonAtualizar = tk.Button(root, text="Atualizar Produtos")
    #buttonMostrar['command']
    buttonAtualizar.place(x = 100, y = 200)

    # Botão de mostrar produtos
    buttonMostrar = tk.Button(root, text="Mostrar Produtos")
    buttonMostrar['command'] = mostrarBanco
    buttonMostrar.place(x = 100, y = 300) 

    # Configuração pra janela sempre abrir
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

menuPrincipal()