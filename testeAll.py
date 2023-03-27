from tkinter import *
from tkinter import ttk, Tk
from tkinter import messagebox
import sqlite3

class funCadastro():
    def limpaTela(self):

        self.entry_cod.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_nick.delete(0, END)
        self.entry_idade.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_cadSenha.delete(0, END)
        self.entry_confSenha.delete(0, END)

    def salvarDados(self):
        self.codigo = self.entry_cod.get()
        self.nome = self.entry_nome.get()
        self.nick = self.entry_nick.get()
        self.idade = self.entry_idade.get()
        self.email = self.entry_email.get()
        self.trilha = "Capitulo 1"
        self.ataque = 10
        self.senha = self.entry_cadSenha.get()
        for i in self.codigo:
            print(i)
        
        self.conecta()
        self.cursor.execute("""
            INSERT INTO CadastroUsu(Nome, Nickname, Idade, Email, Trilha, Ataque, senha) VALUES(?, ?, ?, ?, ?, ?, ?)
            """, (self.nome, self.nick, self.idade, self.email, self.trilha, self.ataque, self.senha))
        self.db.commit()
        self.desconecta()

        self.limpaTela()


    def deletaUsu(self):
        self.variaveis()
        self.conecta()

        self.cursor.execute("""DELETE FROM CadastroUsu WHERE Id = ?""", (self.codigo))
        self.db.commit()

        self.desconecta()
        self.limpaTela()
        self.selecionarDados()

    def alteraUsu(self):
        self.variaveis()
        self.conecta()

        self.cursor.execute("""UPDATE CadastroUsu SET Nome = ?, Nickname = ?, Idade = ?, Email = ?, Trilha = ?, Ataque= ?, Senha = ?
        WHERE Id = ?""", (self.nome, self.nick, self.idade, self.email, self.trilha, self.ataque,self.senha, self.codigo))
        self.db.commit()

        self.desconecta()
        self.limpaTela()

    def variaveis(self):
        self.codigo = self.entry_cod.get()
        self.nome = self.entry_nome.get()
        self.nick = self.entry_nick.get()
        self.idade = self.entry_idade.get()
        self.email = self.entry_email.get()
        self.senha = self.entry_cadSenha.get()


    def criarTabela(self):
        self.conecta()
        print("Conectado!!!")
        #criação tabela:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS CadastroUsu (
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                Nome CHAR(30) NOT NULL,
                Nickname CHAR(10) NOT NULL,
                Idade INTEGER(2) NOT NULL,
                email CHAR(25) NOT NULL,
                Trilha CHAR(20),
                Ataque INTEGER,
                Senha CHAR(15) NOT NULL
            );
        """)
        self.db.commit()
        self.desconecta()

class Cadastro(funCadastro):
    def telacadastro(self):
        root = Tk()
        self.root = root
        self.tela3()
        self.frames3()
        self.criandoBotoes()
        self.criarTabela()

        root.mainloop()
        
    def tela3(self):
        self.root.title("Cadastro")
        self.root.configure(bg="black")
        self.root.geometry("700x250")
        self.root.resizable(width=True, height=True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
    def frames3(self):
        self.frameCima = Frame(self.root, bd=4, bg="black", highlightbackground="gray", highlightthickness=3)
        self.frameCima.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)


    def criandoBotoes(self):
        #Criação do botão limpar:
        self.bt_limpar = Button(self.frameCima, text="Limpar", bd=3, bg="black", fg="white", font=("Century Gothic", 9, 'bold'), command=self.limpaTela)
        self.bt_limpar.place(relx=0.2, rely=0.15, relwidth=0.1, relheight=0.15)
        #Criação do botão buscar:
        self.bt_buscar = Button(self.frameCima, text="Buscar", bd=3, bg="black", fg="white", font=("Century Gothic", 9, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.15, relwidth=0.1, relheight=0.15)

        #Criação do botão novo:
        self.bt_novo = Button(self.frameCima, text="Novo", bd=3, bg="black", fg="white", font=("Century Gothic", 9, 'bold'), command=self.salvarDados)
        self.bt_novo.place(relx=0.5, rely=0.15, relwidth=0.1, relheight=0.15)

        #Criação do botão alterar:
        self.bt_alterar = Button(self.frameCima, text="Alterar", bd=3, bg="black", fg="white", font=("Century Gothic", 9, 'bold'), command=self.alteraUsu)
        self.bt_alterar.place(relx=0.6, rely=0.15, relwidth=0.1, relheight=0.15)
        
        #Criação do botão apagar:
        self.bt_apagar = Button(self.frameCima, text="Apagar", bd=3, bg="black", fg="white", font=("Century Gothic", 9, 'bold'), command=self.deletaUsu)
        self.bt_apagar.place(relx=0.7, rely=0.15, relwidth=0.1, relheight=0.15)


        #Criação de Labels da tela, codigo:
        self.lb_txt00 = Label(self.frameCima, text="Código:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_txt00.place(relx=0.05, rely=0.05)
        
        self.entry_cod = ttk.Entry(self.frameCima)
        self.entry_cod.place(relx=0.05, rely=0.15, relwidth=0.15, relheight=0.15)


        #Criação de Labels da tela,nome:
        self.lb_nome = Label(self.frameCima, text="Nome:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.entry_nome = ttk.Entry(self.frameCima)
        self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.40, relheight=0.15)


        #Criação de Labels da Nickname:
        self.lb_nick = Label(self.frameCima, text="Nickname:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_nick.place(relx=0.5, rely=0.35)
        
        self.entry_nick = ttk.Entry(self.frameCima)
        self.entry_nick.place(relx=0.5, rely=0.45, relwidth=0.2, relheight=0.15)

        #Criação de Labels da Idade:
        self.lb_idade = Label(self.frameCima, text="Idade:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_idade.place(relx=0.75 , rely=0.35)
        
        self.entry_idade = ttk.Entry(self.frameCima)
        self.entry_idade.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.15)


        #Criação de Labels da Email:
        self.lb_email = Label(self.frameCima, text="Email:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_email.place(relx=0.05 , rely=0.65)
        
        self.entry_email = ttk.Entry(self.frameCima)
        self.entry_email.place(relx=0.05, rely=0.75, relwidth=0.40, relheight=0.15)


        #Criação de Labels da Trilha:
        self.lb_senha = Label(self.frameCima, text="Senha:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue")
        self.lb_senha.place(relx=0.5 , rely=0.65)
        
        self.entry_cadSenha = ttk.Entry(self.frameCima)
        self.entry_cadSenha.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.15)


        #Criação de Labels da Ataque:
        self.lb_confSenha = Label(self.frameCima, text="Confirme sua senha:", bg="black", font=("Arial Black", 10, 'bold'), fg="lightblue" )
        self.lb_confSenha.place(relx=0.75 , rely=0.65)
        
        self.entry_confSenha = ttk.Entry(self.frameCima)
        self.entry_confSenha.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.15)

class Funcoes(Cadastro):
    def conecta(self):
        self.db = sqlite3.connect('dbJogoteste.db')
        self.cursor = self.db.cursor()
        print("Conectado")

    def desconecta(self):
        self.db.close()
        print("Desconectado")

    def apagaLogin(self):
        self.janela.destroy()

    def loginBD(self):
        self.Nome = self.entryNome.get()
        self.Password = self.entrypass.get()

        self.conecta()

        self.cursor.execute("SELECT Nickname FROM CadastroUsu WHERE Nickname = '"+self.Nome+"'")
        self.x1 = self.cursor.fetchall()[0]
        self.x1 = str(self.x1[0])
        self.cursor.execute("SELECT Senha FROM CadastroUsu WHERE Nickname = '"+self.Nome+"'")
        self.y1 = self.cursor.fetchall()[0]
        self.y1 = str(self.y1[0])
        if self.Nome == self.x1 and self.Password == self.y1:
            messagebox.showinfo(title="Login", message="Acesso confirmado, bem vindo!") 
            self.main()
            self.apagaLogin()

        else:
            messagebox.showerror(title="Login", message="Acesso negado, verificar dados ou efetuar o cadastro") 

        self.desconecta()


    def login(self):
        self.conexaoLogin()
        self.janela = Tk()
        self.janela.title("Login")
        self.janela.geometry('300x400')
        self.janela.configure(background="Black")
        self.janela.resizable(width=False, height=False)
        self.janela.attributes("-alpha", 0.9)

            #Dividindo Janela:
        self.frameCima = Frame(self.janela, width=310, height=50, bg="MIDNIGHTBLUE", relief='flat')
        self.frameCima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        self.frameBaixo = Frame(self.janela, width=310, height=350, bg="BLACK", relief='flat')
        self.frameBaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

            #Configurando frame de cima:

        self.tetoq = Label(self.frameCima, text="LOGIN", anchor=NE, font=("Ivy", 25), bg = "Midnightblue", fg="White")
        self.tetoq.place(x=5, y=5)

        self.tetolinha = Label(self.frameCima, text='', width=275, anchor=NW, font=("Ivy", 1), bg = "Gray", fg="White")
        self.tetolinha.place(x=10, y=45)



            #Configurando frame de baixo:

        self.tetoq = Label(self.frameBaixo, text="Nome: ", anchor=NW, font=("Ivy", 13), bg = "Black", fg="White")
        self.tetoq.place(x=10, y=20)
        self.entryNome = ttk.Entry(self.frameBaixo, width=25, justify='left', font=("", 13))
        self.entryNome.place(x= 16, y=50)

        self.tetoa = Label(self.frameBaixo, text="Senha: ", anchor=NW, font=("Ivy", 13), bg = "Black", fg="White")
        self.tetoa.place(x=10, y=95)
        self.entrypass = ttk.Entry(self.frameBaixo, width=25, justify='left', font=("", 13))
        self.entrypass.place(x= 16, y=130)



        self.botaoEntrar = ttk.Button(self.frameBaixo, text="Confirmar", width=30, command=self.loginBD)
        self.botaoEntrar.place(x=37, y=170)

        self.texto = Label(self.frameBaixo, text="Ainda não tem cadastro?", anchor=NW, font=("Ivy", 13), bg="Black", fg="White")
        self.texto.place(x=10, y=220)
        self.botaoContinuar = ttk.Button(self.frameBaixo, text="Cadastrar", width=30,command=self.telacadastro)
        self.botaoContinuar.place(x=37, y=270)

        self.janela.mainloop()

    def conexaoLogin(self):
        self.conecta()
    
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Usuario TEXT NOT NULL,
        Senha TEXT NOT NULL
        );
        """)
        print("Conectado!")
        self.desconecta()

    def atencao(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Abaixei-me um pouco, por instinto. Equanto eu fazia meu movimento o monstro aos poucos ele parou sua pata no ar, observando-me também...\nE aos poucos as formas iam e iam tomando forma. Havia um buraco em seu peito e sua espinha tinha espinhos longos e afiados... sua cabeca ainda era um borrão", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.33)

        self.bt_novo2 = Button(self.frameCima, text="Abra os olhos", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.abrirOlhos)
        self.bt_novo2.place(relx=0.05, rely=0.51, relwidth=0.9, relheight=0.05)

        self.bt_novo3 = Button(self.frameCima, text="Calma", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'),command=self.Calma)
        self.bt_novo3.place(relx=0.05, rely=0.57, relwidth=0.9, relheight=0.05)

    def abrirOlhos(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Quando abri os olhos, sua mente não era mais um borrão, ele tinha um focinho longo cheio de dentes como um tubaurso, focinho de urso e dentes de tubarão.\nPensar nisso me fez dar uma pequena risada e então seus olhos começaram a brilhar em vermelho.", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.63)

        self.bt_novo2 = Button(self.frameCima, text="Batalha!", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'))
        self.bt_novo2.place(relx=0.05, rely=0.87, relwidth=0.9, relheight=0.05)

    def Calma(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Respirei fundo, o que estava acontecendo? aquilo era inacreditável...\nLogo eu abri meus olhos e então vi aquela bocarra cheia de dentes já se preparando para pular em mim!", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.63)
        self.bt_novo2 = Button(self.frameCima, text="Começar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'))
        self.bt_novo2.place(relx=0.05, rely=0.87, relwidth=0.9, relheight=0.05)

    def preparar(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Abaixei-me um pouco, por instinto. E todos os meus neuronios pareciam estar querendo se voltar àquele beixo, então abri meus olhos e agora ainda com breo podia ver a forma que tinha montado à minha frente. \nAos poucos vi sua pata pousar logo a frente de seu corpo, e então fazer o mesmo movimento com a segunda pata fronteira também, só que essa era forte e pesada como as detrás.", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.31)
        self.bt_novo2 = Button(self.frameCima, text="Prepare-se", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.MaisPreIm)
        self.bt_novo2.place(relx=0.05, rely=0.52, relwidth=0.9, relheight=0.05)
        self.bt_novo3 = Button(self.frameCima, text="Ele vai te Atacar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.Cuidado)
        self.bt_novo3.place(relx=0.05, rely=0.58, relwidth=0.9, relheight=0.05)

    def Cuidado(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Ele realmente iria me atacar. Já conseguia projetar o trajeto que ele iria fazer, mas agora pela primeira vez consegui ter um vislumbre de sua face... Ele tinha um focinho muito largo, como um urso e inumeros dentes, como um tubarão.", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.63)
        self.bt_novo2 = Button(self.frameCima, text="Contra-atacar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'))
        self.bt_novo2.place(relx=0.05, rely=0.87, relwidth=0.9, relheight=0.05)

    def MaisPreIm(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Contrai todos os meus musculos e senti minha pressão sobre o chão aumentar.\nEle recuou um pouco, mas naquele momento ele pareceu muito irritado e começou a ranger os dentes uns nos outros, gerando um barulho amendrontador e preparou-se para atacar: ", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.63)
        self.bt_novo2 = Button(self.frameCima, text="Finalizar!", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'))
        self.bt_novo2.place(relx=0.05, rely=0.87, relwidth=0.9, relheight=0.05)
    def apagaFrame(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.segundaTela()

    def criaFrame(self):
        self.frameCima = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=3)
        self.frameCima.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.win_width = 650

    def prim(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.Oque()

    def prim0(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.prosseguir()

    def prim0_1(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.eIsso()

    def prim0_2(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.avancar()
        
    def seg(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.levanta()

    def seg0(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.queIsso()

    def seg1(self):
        self.frameCima.destroy()
        self.criaFrame()
        self.correr()

    def preBatalha(self):
        self.tela.destroy()
        self.novaTela()
    
    def teladois(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Após notar a respiração atípica, minha mente rapidamente começou a criar fromas e um medo começou a acelear meus batimentos.\nAs formas logo se transformaram numa fera canídea e deformada, uma de suas patas frontais que era ossuda diferente das outras que eram pesadas e com massas de carne caindo pelos lados, começou a se mover.", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.01)

        self.bt_novo2 = Button(self.frameCima, text="Atenção", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'),command=self.atencao)
        self.bt_novo2.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.05)

        self.bt_novo3 = Button(self.frameCima, text="Preparar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'),command=self.preparar)
        self.bt_novo3.place(relx=0.05, rely=0.26, relwidth=0.9, relheight=0.05)

    def novaTela(self):
        tela2 = Tk()
        self.tela2 = tela2
        self.tela2.title("Teste")
        self.tela2.geometry("700x750")
        self.tela2.resizable(width=True, height=True)
        self.tela2.maxsize(width=900, height=700)
        self.tela2.minsize(width=400, height=300)
        self.tela2.configure(background="black")

        self.frameCima = Frame(self.tela2, bd=4, bg="black", highlightbackground="gray", highlightthickness=4)
        self.frameCima.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.win_width = 650
        self.teladois()
        tela2.mainloop()



class App(Funcoes):
    def __init__(self):


        #self.telaIni()
        self.login()
        self.conexaoLogin()

        #tela.mainloop()
    def main(self):
        tela = Tk()
        self.tela = tela
        self.telaIni()
        self.frames()
        self.labels()
        tela.mainloop()
    def telaIni(self):
        self.tela.title("Inicializando...")
        self.tela.geometry("700x300")
        self.tela.resizable(width=True, height=True)
        self.tela.maxsize(width=900, height=700)
        self.tela.minsize(width=400, height=300)
        self.tela.configure(background="black")


    def frames(self):
        self.frameCima = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=3)
        self.frameCima.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.win_width = 650
        self.labels()

    def labels(self):
        self.lb_txt01 = Label(self.frameCima,wraplength=self.win_width, text="Tudo está desmoronando... Vejo lentamente um gande e pesado tijolo de cimento cair sobre meu peito.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt01.place(relx=0.01, rely=0.05)

        self.lb_txt11 = Label(self.frameCima, text="A força do impacto fez-me despencar ainda mais ferozmente...", bg="black", font=("Arial Black", 10, 'bold'), fg="white")
        self.lb_txt11.place(relx=0.17, rely=0.28)

        self.lb_txt21 = Label(self.frameCima, text="Minha mente girava, como o embaralho de cores que se retorcia no alto.", bg="black", font=("Arial Black", 10, 'bold'), fg="white")
        self.lb_txt21.place(relx=0.1, rely=0.45)

         #Criação do botão novo:
        self.bt_novo = Button(self.frameCima, text="Iniciar?", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.apagaFrame)
        self.bt_novo.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.25)

    def segundaTela(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Quando recobrei a consciência não estava mais caindo, mas a primeira impressão que tive ao abrir os olhos é de que eu estava morto.\nEstava tudo um breu, uma escuridão completa. Sequer consegui enxergar minha mão na frente dos olhos. \nEu estava deitado no chão, numa terra dura e fria e comecei a apalpar pelo terreno tentando encontrar algo, mas era somente a terra perfeitamente plana e gelada.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.lb_txt1 = Label(self.frameCima, text="O que está acontecendo? O que é isso? onde eu estou?", bg="black", font=("Arial Black", 10, 'bold'), fg="white")
        self.lb_txt1.place(relx=0.17, rely=0.5)

        self.bt_novo2 = Button(self.frameCima, text="O que está acontecendo?", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim)
        self.bt_novo2.place(relx=0.15, rely=0.63, relwidth=0.3, relheight=0.25)

        self.bt_novo3 = Button(self.frameCima, text="Pular", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim)
        self.bt_novo3.place(relx=0.55, rely=0.63, relwidth=0.3, relheight=0.25)

    def Oque(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Depois que a tensão deixou meu corpo eu tive forças para me levantar e como não conseguia ver nada eu tomei todo cuidado para não tropeçar ou cair em nenhum lugar.\nNo entanto, todo esse cuidado não me impediu de chutar algo. Um grunido estremeceu em meus ouvidos, tempo o suficiente para quase camuflar passos ferozes se afastando.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.bt_novo2 = Button(self.frameCima, text="Prosseguir", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim0)
        self.bt_novo2.place(relx=0.15, rely=0.63, relwidth=0.3, relheight=0.25)

        self.bt_novo3 = Button(self.frameCima, text="Levantar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.seg)
        self.bt_novo3.place(relx=0.55, rely=0.63, relwidth=0.3, relheight=0.25)

    def prosseguir(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Quando recobrei a consciência não estava mais caindo, mas a primeira impressão que tive ao abrir os olhos é de que eu estava morto.\nEstava tudo um breu, uma escuridão completa. Sequer consegui enxergar minha mão na frente dos olhos. \nEu estava deitado no chão, numa terra dura e fria e comecei a apalpar pelo terreno tentando encontrar algo, mas era somente a terra perfeitamente plana e gelada.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)


        self.bt_novo2 = Button(self.frameCima, text="O que é isso?", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim0_1)
        self.bt_novo2.place(relx=0.15, rely=0.63, relwidth=0.3, relheight=0.25)

        self.bt_novo3 = Button(self.frameCima, text="Avançar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim0_2)
        self.bt_novo3.place(relx=0.55, rely=0.63, relwidth=0.3, relheight=0.25)

    def eIsso(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="'O que é isso?'\nFechei os olhos, o que era aquilo? Nunca tinha ouvido nada do tipo, talvez numa cirene... Um alerta. Respirei fundo e estabilizei minha postura.\nSabia que não iria adiantar abrir os olhos para procurar aquilo, o breu não iria sumir. Concentrei minha audição e logo notei uma respiração estranha vindo de trás.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)


        self.bt_novo2 = Button(self.frameCima, text="Esquivar!", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.preBatalha)
        self.bt_novo2.place(relx=0.35, rely=0.63, relwidth=0.3, relheight=0.25)

    def avancar(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Segui o instinto e avançei na direção que sentia uma presença e quando me aproximava fui dominado por uma aura de fedor. Algo de putefração a ódio, aquilo fez-me perder o foco e abrir os olhos.\nHavia um vulto preto em minha frente e movia um membro em minha direção, em contra-ataque. Não havia mais como desviar, coloquei os braços em frente do rosto.\nA força fez meus braços doerem e o impacto me jogou no mesmo lugar que eu estava", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)


        self.bt_novo2 = Button(self.frameCima, text="Contra-atacar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.prim)
        self.bt_novo2.place(relx=0.35, rely=0.63, relwidth=0.3, relheight=0.25)

    def levanta(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Meus musculos estavam tensos, ainda assim era preciso me levantar então me esforcei ao máximo para isso. O esforço durou pouco tempo, pois perdi o equilibrio e cambaleei até bater em algo rigido. Mas não era algo preso no chão ou rigido o suficiente para aguentar meu impacto, pois com a força da batida ele foi empurrado para alguns metros", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.bt_novo2 = Button(self.frameCima, text="O que é isso?", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.seg0)
        self.bt_novo2.place(relx=0.15, rely=0.63, relwidth=0.3, relheight=0.25)

        self.bt_novo3 = Button(self.frameCima, text="Correr", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.seg1)
        self.bt_novo3.place(relx=0.55, rely=0.63, relwidth=0.3, relheight=0.25)

    def queIsso (self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="'O que é isso?'\nFechei os olhos, o que era aquilo? Respirei fundo e estabilizei minha postura.\nSabia que não iria adiantar abrir os olhos, continuaria um breu. Mas um fedor inebriante se impregnou em meu nariz, aquilo alertou meus instintos o que quer que fosse fedia a maldade! ", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.bt_novo2 = Button(self.frameCima, text="Defesa", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'), command=self.preBatalha)
        self.bt_novo2.place(relx=0.35, rely=0.63, relwidth=0.3, relheight=0.25)
 
    def correr(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Não sabia exatamente o que era aquilo, mas a energia que emanava era horrível e assustadora, a melhor alternativa naquele moemnto, seria correr.\nNo movimento mais rapido que conseguia eu me virei e corri o mais rapido que pude, tentando me afastar do local. Entretanto em poucos intantes ouvi passos rapidos atrás de mim, correndo para me alcançar. A essa altura correr no escuro já não parecia uma ideia boa, pois estava correndo a mercê da sorte, sem enchegar onde daria o proximo salto.\n Não demorou ate que me alcancesse, vi o vulto preto enquanto aquilo aumentava a velocidade, aos poucos, para me contornar.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.bt_novo2 = Button(self.frameCima, text="Cadê?", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'))
        self.bt_novo2.place(relx=0.15, rely=0.67, relwidth=0.3, relheight=0.25)






App()