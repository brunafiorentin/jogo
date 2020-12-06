import os
import random
import string
import time
import pygame

def limparTela():
    os.system("cls")
def registro(nome,email):
    arquivo = open("file.txt","a")
    arquivo.write(" Nome: ")
    arquivo.write(nome)
    arquivo.write(" |E-mail: ")
    arquivo.write(email)
    arquivo.write("\n")
    arquivo.close()
    