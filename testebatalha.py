from tkinter import *
from tkinter import ttk, Tk
import sqlite3
import random




tela = Tk()

class Funcoes():
    def limpaFrame(self):
        self.frameMeio.destroy()
        
    def atual(self):
        self.conecta()
        
        if self.valor == 1:
            self.vidaT = str(self.vidaT)
            self.cursor.execute("UPDATE Atributos SET Vida = '"+self.vidaT+"'WHERE Id = 0")
            self.db.commit()
            self.desconecta()
        elif self.valor == 2:
            self.vidaV = str(self.vidaV)
            self.cursor.execute("UPDATE AtributosVilao SET Vida = '"+self.vidaV+"'WHERE Id = 0")
            self.db.commit()
            self.desconecta()

    def conecta(self):
        self.db = sqlite3.connect('dbJogoteste.db')
        self.cursor = self.db.cursor()
        print("Conectado")

    def desconecta(self):
        self.db.close()
        print("Desconectado")

    def conexao(self):
        self.conecta()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Atributos (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Dano TEXT NOT NULL,
        Vida TEXT NOT NULL,
        Critico TEXT NOT NULL,
        Armadura TEXT NOT NULL
        );
        """)
        self.db.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS AtributosVilao (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Dano TEXT NOT NULL,
        Vida TEXT NOT NULL,
        Critico TEXT NOT NULL,
        Armadura TEXT NOT NULL
        );
        """)
        self.db.commit()
        self.desconecta()

    def atributos(self):
        self.conecta()

        #Atributos vilão
        self.cursor.execute("SELECT Dano FROM AtributosVilao WHERE Id = 0")
        self.danoV = self.cursor.fetchall()[0]
        self.danoV = (self.danoV[0])
        self.danoV = float(self.danoV)
        self.cursor.execute("SELECT Critico FROM AtributosVilao WHERE Id = 0")
        self.sangramento = self.cursor.fetchall()[0]
        self.sangramento = (self.sangramento[0])
        self.sangramento =  float(self.sangramento)
        self.cursor.execute("SELECT Vida FROM AtributosVilao WHERE Id = 0")
        self.vidaV = self.cursor.fetchall()[0]
        self.vidaV = (self.vidaV[0])
        self.vidaV = float(self.vidaV)
        #Atributos:
        self.cursor.execute("SELECT Dano FROM Atributos WHERE Id = 0")
        self.dano = self.cursor.fetchall()[0]
        self.dano = (self.dano[0])
        self.dano = int(self.dano)
        self.cursor.execute("SELECT Critico FROM Atributos WHERE Id = 0")
        self.critico = self.cursor.fetchall()[0]
        self.critico = (self.critico[0])
        self.critico = float(self.critico)
        print(self.critico)
        self.cursor.execute("SELECT Vida FROM Atributos WHERE Id = 0")
        self.vida = self.cursor.fetchall()[0]
        self.vida = (self.vida[0])
        self.vida = float(self.vida)
        
        
        self.cursor.execute("SELECT Armadura FROM Atributos WHERE Id = 0")
        self.armadura = self.cursor.fetchall()[0]
        self.armadura =(self.armadura[0])
        self.armadura = float(self.armadura)
        self.vidaT = self.vida + (self.armadura*100)

        #criar ifs para a batalha e apresentar a falas para cada um.
        self.desconecta()



    def Ataque(self):
        self.atributos()
        self.dado = self.dados()
        self.limpaFrame()
        if self.dado == 1 or self.dado ==2 or self.dado == 3:
            if self.vidaV >=350:
                self.lb_txt0 = Label(self.frameMeio,wraplength=self.win_width, text="Ele se preparou para pular e abriu a boca para me abocanhar", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                self.vidaT = self.vidaT - (self.danoV +(self.sangramento*100))
                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)
    
            elif self.vidaV >=300:
                self.lb_txt0 = Label(self.frameMeio,wraplength=self.win_width, text="Ele se preparou para pular e abriu a boca para me abocanhar", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                self.vidaT = self.vidaT - (self.danoV + self.sangramento)
                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)
            

            elif self.vidaV >=200:
                self.lb_txt0 = Label(self.frameMeio,wraplength=self.win_width, text="Ele se preparou para pular e abriu a boca para me abocanhar", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                self.vidaT = self.vidaT - self.danoV

                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)


            elif self.vidaV >=100:                
                self.danoV = self.danoV + 10
                if self.danoV > 30:
                    self.danoV = 20
                self.lb_txt0 = Label(self.frameMeio,wraplength=self.win_width, text="Ele se preparou para pular e abriu a boca para me abocanhar", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)

                self.vidaT = self.vidaT - (self.danoV + self.sangramento)


        elif self.dado == 4 or self.dado == 5 or self.dado ==6:
            if self.dado == 4:
                self.ataque = self.dano + (self.critico*100)
                self.vidaV = self.vidaV - self.ataque
                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)

                self.lb_txt0 = Label(self.frameMeio,wraplength=self.win_width, text="Fiz um movimento para o lado direito e coloquei toda a força que pude em meu braço, então saltei em sua direção e esmurrei-o duas vezes com meu braço", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                
            elif self.dado == 5 or self.dado == 6:
                self.ataque = self.dano + (self.critico**2*100)
                self.vidaV = self.vidaV - self.ataque
                self.lb_txt0 = Label(self.frameMeio, wraplength=self.win_width, text="Foquei naquela criatura e soquei-a com toda força que tinha", bg="black", font=("arial black", 11, 'bold'), fg="red")
                self.lb_txt0.place(relx=0.01, rely=0.33)
                self.bt_novo2 = Button(self.baixo, text="Jogar Dados", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Ataque)
                self.bt_novo2.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.15)

        if self.dado == 1 or self.dado == 2 or self.dado == 3:
            self.valor = 1
            self.atual()
        elif self.dado == 4 or self.dado == 5 or self.dado == 6:
            self.valor = 2
            self.atual()



    def dados(self):
        return random.randint(1,6)

class App(Funcoes):
    def __init__(self):
        self.tela = tela
        self.telaIni()
        self.frames()
        self.conexao()
        self.Ataque()

        tela.mainloop()

    def telaIni(self):
        self.tela.title("Inicializando...")
        self.tela.geometry("300x500")
        self.tela.resizable(width=True, height=True)
        self.tela.maxsize(width=900, height=700)
        self.tela.minsize(width=400, height=300)
        self.tela.configure(background="black")

    def frames(self):
        self.frameMeio = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=4)
        self.frameMeio.place(relx=0.01, rely=0.2, relwidth=0.97, relheight=0.55)

        self.win_width = 250

        self.cima = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=4)
        self.cima.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.25)

        self.baixo = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=4)
        self.baixo.place(relx=0.01, rely=0.72, relwidth=0.97, relheight=0.25)
    

     

App()