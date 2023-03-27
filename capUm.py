# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 01:58:54 2023

@author: altem
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def capituloUm():
    janela = Tk()
    janela.title("Capítulo I - No Inicio")
    janela.geometry("1200x680")
    janela.configure(background="Black")
    
    janela.resizable(width=False, height=False)
    janela.attributes("-alpha", 0.9)
    
    tela = Frame(janela, width=1200, height=680, bg="BLACK", relief="raise")
    tela.pack(side=RIGHT)
    win_width, win_height = 1200, 680
    
    ola = Label(tela,wraplength=win_width, text="Digite seu nome: ", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
    ola.place(x=5, y=5)
    personagem = ttk.Entry(tela, width=15)
    personagem.place(x=155, y=9)
    nome = personagem.get()
    print(nome)
    
    apresentacao = Label(tela, wraplength=win_width, text="Olá, ", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
    #apresentacao.place(x=40, y=5)
    
    forca = 0
    Carisma = 0
    def continuação():
        proxText = Label(tela, wraplength=win_width, text="Quando recobrei a consciência não estava mais caindo, mas a primeira impressão que tive ao abrir os olhos é de que eu estava morto.\nEstava tudo um breu, uma escuridão completa. Sequer consegui enxergar minha mão na frente dos olhos. \nEu estava deitado no chão, numa terra dura e fria e comecei a apalpar pelo terreno tentando encontrar algo, mas era somente a terra perfeitamente plana e gelada.", font=("CenturyGothic", 13), bg="BLACK", fg= "WHITE")
        proxText.place(x=5, y=35)
        def oQue():
            acon = Label(tela, wraplength=win_height, text="O que está acontecendo? O que é isso? onde eu estou?", font=("Century Gothic", 13), bg="BLACK", fg ="WHITE")
            acon.place(x=5, y=170)
            return
            
        acontecendo = ttk.Button(tela, text="O que está acontecendo?", width=20, command=oQue)
        acontecendo.place(x=5, y=120)
        print(forca)
        def pular():
            acon = Label(tela, wraplength=win_height, text="O que está acontecendo? O que é isso? onde eu estou?", font=("Century Gothic", 13), bg="BLACK", fg ="WHITE")
            acon.place(x=5, y=170)
        pula = ttk.Button(tela, text="Pular", width=20, command=pular)
        pula.place(x=139, y=120)
        a =0
        if a == 1:
            textOne = Label(tela, wraplength=win_height, text="Depois que a tensão deixou meu corpo eu tive forças para me levantar e como não conseguia ver nada eu tomei todo cuidado para não tropeçar ou cair em nenhum lugar.\nNo entanto, todo esse cuidado não me impediu de chutar algo. A primeiro momento pensei ser um entulho talvez um animal adormecido, entretanto, quando ouvi um gemido de dor e um xingamento, vi que se tratava de uma pessoa.", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
            textOne.place(x=5, y=210)
    okay = ttk.Button(tela, text="OK", width=6, command=continuação)
    okay.place(x=260, y=8)
    
    janela.mainloop()
    
    
capituloUm()