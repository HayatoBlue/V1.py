from tkinter import *
from tkinter import ttk, Tk


tela = Tk()

class Funcoes():
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

    def labels(self):
        self.lb_txt0 = Label(self.frameCima,wraplength=self.win_width, text="Tudo está desmoronando... Vejo lentamente um gande e pesado tijolo de cimento cair sobre meu peito.", bg="black", font=("arial black", 10, 'bold'), fg="white")
        self.lb_txt0.place(relx=0.01, rely=0.05)

        self.lb_txt1 = Label(self.frameCima, text="A força do impacto fez-me despencar ainda mais ferozmente...", bg="black", font=("Arial Black", 10, 'bold'), fg="white")
        self.lb_txt1.place(relx=0.17, rely=0.28)

        self.lb_txt2 = Label(self.frameCima, text="Minha mente girava, como o embaralho de cores que se retorcia no alto.", bg="black", font=("Arial Black", 10, 'bold'), fg="white")
        self.lb_txt2.place(relx=0.1, rely=0.45)

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