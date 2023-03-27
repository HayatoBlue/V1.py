# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:23:29 2023

@author: altem
"""
import capUm
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk




#Ataque básico
def ataqueBasico(ataque, critico, perfArmadura, cortaCura):
    atriTotais = ((ataque + critico + perfArmadura) * cortaCura) * 100
    atriTotais = "{:.1f}".format(atriTotais)
    return atriTotais
 
#Ataque critico   
def ataqueCritico(ataque, critico, perfArmadura, cortaCura):
    dano = ((ataque + perfArmadura + cortaCura)* critico**(critico)) * 100
    dano = "{:.1f}".format(dano)
    return dano
    
#ataque final, 
def ataqueDefinitivo(ataque, critico, perfArmadura, cortaCura):
    aux = ((ataque) * (critico) * (perfArmadura ** perfArmadura) * (cortaCura ** cortaCura) * 100)
    aux = "{:.1f}".format(aux)
    
    return aux

def linha():
    print("=======================================================")



inicial = Tk()
inicial.title("Inicializando...")
inicial.geometry("600x300")
inicial.configure(background="White")

inicial.resizable(width=False, height=False)
inicial.attributes("-alpha", 0.9)

tela= Frame(inicial, width=600, height=600, bg="BLACK", relief="raise")
tela.pack(side=RIGHT)


#Atributos
ataque = 1
critico = 0.3
perfArmadura = 3
cortaCura = 0.3

Basico = ataqueBasico(ataque, critico, perfArmadura, cortaCura)
Critico = ataqueCritico(ataque, critico, perfArmadura, cortaCura)
Finalizador = ataqueDefinitivo(ataque, critico, perfArmadura, cortaCura)

win_width, winheight = 600, 300
textOne = Label(tela, wraplength=win_width, text="Tudo está desmoronando... Vejo lentamente um gande e pesado tijolo de cimento cair sobre meu peito.", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
textOne.place(x=0, y=5)


textTwo = Label(tela, wraplength=win_width, text="A força do impacto fez-me cair ainda mais ferozmente...", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
textTwo.place(x=40, y=55)

textTree = Label(tela, wraplength=win_width, text="Minha mente girava, como o embaralho de cores que se retorcia no alto", font=("Century Gothic", 13), bg="BLACK", fg="WHITE")
textTree.place(x=0, y=105)

textinicia = Label(tela, wraplength=win_width, text="Iniciar?", font=("Arial", 15), bg="BLACK", fg="WHITE")
textinicia.place(x=260, y=160)

#chamada = capUm.capituloUm()
def chamada():
    inicial.destroy()
    capUm.capituloUm()

botaosim = ttk.Button(tela, text="Sim!", width=13, command=chamada)
botaosim.place(x=210, y=190)

botaoVamos = ttk.Button(tela, text="Vamos lá!", width=13, command=chamada)
botaoVamos.place(x=304, y=190)

inicial.mainloop()