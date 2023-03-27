from tkinter import *
from tkinter import ttk, Tk


tela = Tk()



class App():
    def __init__(self):
        self.tela = tela
        self.telaIni()
        self.frames()
        self.labels()

        tela.mainloop()

    def telaIni(self):
        self.tela.title("Inicializando...")
        self.tela.geometry("700x750")
        self.tela.resizable(width=True, height=True)
        self.tela.maxsize(width=900, height=700)
        self.tela.minsize(width=400, height=300)
        self.tela.configure(background="black")

    def frames(self):
        self.frameCima = Frame(self.tela, bd=4, bg="black", highlightbackground="gray", highlightthickness=4)
        self.frameCima.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.97)

        self.win_width = 650

    def labels(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Após notar a respiração atípica, minha mente rapidamente começou a criar fromas e um medo começou a acelear meus batimentos.\nAs formas logo se transformaram numa fera canídea e deformada, uma de suas patas frontais que era ossuda diferente das outras que eram pesadas e com massas de carne caindo pelos lados, começou a se mover.", bg="black", font=("arial black", 11, 'bold'), fg="red")
        self.lb_txt0.place(relx=0.01, rely=0.01)

        self.bt_novo2 = Button(self.frameCima, text="Atenção", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'),command=self.atencao)
        self.bt_novo2.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.05)

        self.bt_novo3 = Button(self.frameCima, text="Preparar", bd=3, bg="black", fg="red", font=("Century Gothic", 9, 'bold'),command=self.preparar)
        self.bt_novo3.place(relx=0.05, rely=0.26, relwidth=0.9, relheight=0.05)


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



App()