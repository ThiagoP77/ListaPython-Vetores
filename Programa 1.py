"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 1. Faça um programa que leia uma lista com 5 números
inteiros e mostre-os.
Data: 13/11/21
"""
#Entrada e Processamento de dados
inteiros = [] #Comando que cria a lista para os números inteiros
w = 0 #Variável responsável por definir quantas vezes o comando while se repete
print("==============================================")
print("PROGRAMA QUE GERA LISTA COM 5 NÚMEROS INTEIROS")
print("==============================================")
print(" ")
print("-Insira os números abaixo-")
print(" ")
while(w<5):#Comando que pede para o usuário inserir um número cinco vezes
    if(w==0):#Define o número como primeiro se a variável w for igual a 0
        ordem = "primeiro"
    elif(w==1):#Define o número como segundo se a variável w for igual a 1
        ordem = "segundo"
    elif(w==2):#Define o número como terceiro se a variável w for igual a 2
        ordem = "terceiro"
    elif(w==3):#Define o número como quarto se a variável w for igual a 3
        ordem = "quarto"
    elif(w==4):#Define o número como quinto se a variável w for igual a 4
        ordem = "quinto"
    numero = int(input("Informe o %s número inteiro: " %(ordem)))#Comando que pede para o usuário inserir um número inteiro
    inteiros.append(numero)#Comando que adiciona o número inteiro à lista "inteiros"
    w += 1#Comando que adiciona 1 à variável w

#Saída de dados
print(" ")
print("=========")
print("RESULTADO")
print("=========")
print(" ")
print("Lista com os números inteiros digitados: %s." %(inteiros))#Comando que mostra a lista de inteiros para o usuário
