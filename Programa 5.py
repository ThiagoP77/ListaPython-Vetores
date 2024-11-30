"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 5. Faça um Programa que leia 20 números inteiros e armazene-os
numa lista. Armazene os números pares no vetor PAR e
os números IMPARES no vetor impar. Imprima as três listas.
Data: 13/11/21
"""
#Entrada e Processamento de dados
numeros = []#Cria a lista para receber todos os números digitados
par = []#Cria a lista para receber todos os números pares digitados
impar = []#Cria a lista para receber todos os números ímpares digitados
w = 0#Variável que controla quantas vezes o while se repete
print("===============================================")
print("PROGRAMA QUE IDENTIFICA NÚMEROS PARES E ÍMPARES")
print("===============================================")
print(" ")
print("-Insira os números abaixo")
print(" ")
while(w<20):#Comando que pede para o usuário inserir um número vinte vezes
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
    elif(w==10):#Define o número como décimo primeiro quando a variável w é 10
        ordem = "décimo primeiro"
    elif(w==11):#Define o número como décimo segundo quando a variável w é 11
        ordem = "décimo segundo"
    elif(w==12):#Define o número como décimo terceiro quando a variável w é 12
        ordem = "décimo terceiro"
    elif(w==13):#Define o número como décimo quarto quando a variável w é 13
        ordem = "décimo quarto"
    elif(w==14):#Define o número como décimo quinto quando a variável w é 14
        ordem = "décimo quinto"
    elif(w==15):#Define o número como décimo sexto quando a variável w é 15
        ordem = "décimo sexto"
    elif(w==16):#Define o número como décimo sétimo quando a variável w é 16
        ordem = "décimo sétimo"
    elif(w==17):#Define o número como décimo oitavo quando a variável w é 17
        ordem = "décimo oitavo"
    elif(w==18):#Define o número como décimo nono quando a variável w é 18
        ordem = "décimo nono"
    elif(w==19):#Define o número como vigésimo quando a variável w é 19
        ordem = "vigésimo"
    numero = int(input("Insira o %s número: " %(ordem)))#Pede para o usuário inserir um número
    numeros.append(numero)#Adiciona o número à lista "numeros"
    if((numero%2)==0):#Adiciona o número a lista "par" quando não sobra resto ao ser dividido por 2
        par.append(numero)
    else:#Adiciona o número a lista "impar" quando sobra resto ao ser dividido por 2
        impar.append(numero)
    w += 1#Adiciona um à variável w

#Saída de dados
print(" ")
print("=========")
print("RESULTADO")
print("=========")
print(" ")
print("Números inteiros digitados: %s." %(numeros))#Mostra a lista com os números digitados
print("Números pares digitados: %s." %(par))#Mostra a lista com os números pares digitados
print("Números ímpares digitados: %s." %(impar))#Mostra a lista com os números ímpares digitados
