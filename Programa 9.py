"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 9. Faça um Programa que leia uma lista A com 10 números
inteiros, calcule e mostre a soma dos quadrados dos elementos da lista.
Data: 13/11/21
"""
#Entrada de dados
inteiros = []#Lista que recebe os números digitados
quadrados = []#Lista que recebe o quadrado dos números digitados
w = 0#Variável que controla quantas vezes o comando while se repete
print("=======================================")
print("CALCULA SOMA DO QUADRADO DE DEZ NÚMEROS")
print("=======================================")
print(" ")
print("-Insira os números abaixo-")
print(" ")
while(w<10):#Comando que pede para o usuário inserir um número dez vezes
    if(w==0):#Define o número como primeiro quando a variável w é 0
        ordem = "primeiro"
    elif(w==1):#Define o número como segundo quando a variável w é 1
        ordem = "segundo"
    elif(w==2):#Define o número como terceiro quando a variável w é 2
        ordem = "terceiro"
    elif(w==3):#Define o número como quarto quando a variável w é 3
        ordem = "quarto"
    elif(w==4):#Define o número como quinto quando a variável w é 4
        ordem = "quinto"
    elif(w==5):#Define o número como sexto quando a variável w é 5
        ordem = "sexto"
    elif(w==6):#Define o número como sétimo quando a variável w é 6
        ordem = "sétimo"
    elif(w==7):#Define o número como oitavo quando a variável w é 7
        ordem = "oitavo"
    elif(w==8):#Define o número como nono quando a variável w é 8
        ordem = "nono"
    elif(w==9):#Define o número como décimo quando a variável w é 9
        ordem = "décimo"
    numero = int(input("Informe o %s número: " %(ordem)))#Pede para o usuário inserir um número inteiro
    quadrado = (numero*numero)#Calcula o quadrado do número inteiro digitado
    inteiros.append(numero)#Adiciona o número digitado à lista "inteiros"
    quadrados.append(quadrado)#Adiciona o quadrado do número digitado à lista "quadrados"
    w += 1#Adiciona 1 à variável w
    
#Processamento de dados
soma = (sum(inteiros))#Calcula a soma dos números digitados
soma_quadrados = (sum(quadrados))#Calcula a soma dos quadrados dos números digitados

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Números digitados: %s." %(inteiros))#Mostra os números digitados
print("Soma dos números digitados: %d." %(soma))#Mostra a soma dos números digitados
print("Quadrados dos números digitados: %s." %(quadrados))#Mostra os quadrados dos números digitados
print("Soma dos quadrados dos números digitados: %d." %(soma_quadrados))#Mostra a soma dos quadrados dos números digitados
