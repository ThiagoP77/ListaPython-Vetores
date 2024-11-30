"""
Nome do programador: Thiago Piffer Lauro
Nome do programa:  7. Faça um Programa que leia uma lista de 5 números
inteiros, mostre a soma, a multiplicação e os números.
Data: 13/11/21
"""
#Entrada de dados
inteiros = []#Lista que recebe os números inteiros digitados
w = 0#Variável que controla quantas vezes o while se repete
multiplicacao = 0#Variável que vai receber a multiplicação dos números digitados
print("==========================================")
print("SOMA E MULTIPLICAÇÃO DE 5 NÚMEROS INTEIROS")
print("==========================================")
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
    inteiros.append(numero)#Comando que adiciona o número inteiro a lista "inteiros"
    if(w==0):#Define as variáveis "numero" e "prod" como o primeiro número digitado
        multiplicacao = numero
    else:#Comando que realiza as multiplicações do números digitados
        multiplicacao = multiplicacao*numero
    w += 1#Comando que adiciona 1 à variável w
    
#Processamento de dados
soma = sum(inteiros)#Calcula a soma dos números digitados

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Números digitados: %s." %(inteiros))#Mostra todos os números digitados
print("Soma dos números: %d." %(soma))#Mostra a soma dos números digitados
print("Multiplicação dos números: %d." %(multiplicacao))#Mostra a multiplicação dos números digitados
