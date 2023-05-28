import customtkinter as Ctk
from tkinter import *

Ctk.set_appearance_mode('white')
Ctk.set_default_color_theme('white')

janela=Ctk.Ctk()

janela.geometry('1000x700')

janela.title('Jogo da Forca')



def jogar_forca():
    palavra_secreta = input("Digite a palavra secreta: ").upper()
    letras_certas = []
    letras_erradas = []
    tentativas = 6

    while True:
        for letra in palavra_secreta:
            if letra in letras_certas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        if len(letras_erradas) > 0:
            print("Letras erradas:", " ".join(letras_erradas))

        letra_palpite = input("Digite uma letra: ").upper()

        if letra_palpite in palavra_secreta:
            letras_certas.append(letra_palpite)
        else:
            letras_erradas.append(letra_palpite)
            tentativas -= 1

        if tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

        if all(letra in letras_certas for letra in palavra_secreta):
            print("Parabéns! Você venceu!")
            break

jogar_forca()
