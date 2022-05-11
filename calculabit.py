from decimal import Decimal
from tkinter import *
import os
import tkinter.messagebox as tkMessageBox
from conversorbit import  Conversorbit

class TelaInicial:
    def __init__(self ):
        self.criarTela()
    
    def criarTela(self):
        #criar tela
        self.root = Tk()
        self.root.title('Calculadora de Decimal para Binário')
        self.root.geometry('600x350+0+0')
        self.root['bg'] = 'LightSkyBlue'
        self.root.iconphoto(True, PhotoImage(file=r'.\\arquivos\\MB.png'))


        self.fPosicao = LabelFrame(self.root,width=20 , text="Calculadora de Decimal para Binário", bg="DodgerBlue", fg="black",font=('arial',14,'bold'))
        self.fPosicao.grid(column=0, row=0, padx=20, pady=20)

        texto = Label(self.fPosicao,text="Decimal",width=10 , bg="DeepSkyBlue", fg="black",font=('arial',14,'bold'))
        texto.grid(column=0, row=0, padx=20, pady=20)
        self.decimal = Entry(self.fPosicao,width=20 , bg="DeepSkyBlue",justify='center', fg="black",font=('arial',14,'bold'))
        self.decimal.grid(column=1, row=0, padx=20, pady=20)

        texto = Label(self.fPosicao,text="Binário",width=10 , bg="DeepSkyBlue", fg="black",font=('arial',14,'bold'))
        texto.grid(column=0, row=1, padx=20, pady=20)
        self.bits = Entry(self.fPosicao,width=20 , bg="DeepSkyBlue",justify='center', fg="black",font=('arial',14,'bold'))
        self.bits.grid(column=1, row=1, padx=20, pady=20)
        self.bits.config(state =DISABLED)

        texto = Label(self.fPosicao,text="Hexadecimal",width=10 , bg="DeepSkyBlue", fg="black",font=('arial',14,'bold'))
        texto.grid(column=0, row=2, padx=20, pady=20)
        self.hexad = Entry(self.fPosicao,width=20 , bg="DeepSkyBlue",justify='center', fg="black",font=('arial',14,'bold'))
        self.hexad.grid(column=1, row=2, padx=20, pady=20)
        self.hexad.config(state =DISABLED)

        #cria botões
        self.botaoAbre = Button(self.fPosicao, text="Calcular", bg="DeepSkyBlue", fg="black",font=('arial',14,'bold'),command=self.funcaoConverte)
        self.botaoAbre.grid(column=0, row=3, padx=20, pady=20)
        self.limpar = Button(self.fPosicao, text="Limpar", bg="DeepSkyBlue", fg="black",font=('arial',14,'bold'),command=self.funcaoLimpar)
        self.limpar.grid(column=1, row=3, padx=20, pady=20)
        self.botaosalva = Button(self.fPosicao, text="Sair", bg="DeepSkyBlue", fg="red",font=('arial',14,'bold'),command=self.funcaoSair)
        self.botaosalva.grid(column=2, row=3, padx=20, pady=20)


       
        #ativa a tela
        self.root.mainloop()

    def funcaoConverte(self):
        try:
            valconvert =int(self.decimal.get())
            inica = Conversorbit()
            inica.resultado=valconvert
            meuresult = inica.convertBit()
            hexresult = inica.hexaconvt
            self.bits.config(state =NORMAL)
            self.bits.delete(0, 'end')
            self.bits.insert(0,meuresult)
            self.bits.config(width=len(meuresult)+5)
            self.hexad.config(state =NORMAL)
            self.hexad.delete(0, 'end')
            self.hexad.insert(0,hexresult)
            
            
        except:
            self.decimal.delete(0, 'end')
            tkMessageBox.showinfo("Erro","Verifique o  valor informado!")

    def funcaoSair(self):
       self.root.destroy()

    def funcaoLimpar(self):
        self.decimal.delete(0, 'end')
        self.bits.delete(0, 'end')
        self.bits.config(width=20)
        self.bits.config(state =DISABLED)
        self.hexad.delete(0, 'end')
        self.hexad.config(state =DISABLED)


    
   
TelaInicial()