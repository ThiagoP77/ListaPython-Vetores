"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 8. Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação em sua respectiva lista.
Imprima a idade e a altura na ordem inversa a ordem lida.
Data: 13/11/21
"""
#Entrada de dados
alturas = []#Lista que vai receber todas as alturas inseridas
idades = []#Lista que vai receber todas as idades inseridas
w = 0#Variável que controla quantas vezes o while se repete
print("===================================================")
print("PROGRAMA QUE DÁ A ORDEM INVERSA DE IDADES E ALTURAS")
print("===================================================")
print(" ")
while(w<5):#Comando que pede para inserir as informações de 5 pessoas
    if(w==0):#Define a pessoa como primeira quando a variável w é 0
        ordem = "primeira"
    elif(w==1):#Define a pessoa como segunda quando a variável w é 1
        ordem = "segunda"
    elif(w==2):#Define a pessoa como terceira quando a variável w é 2
        ordem = "terceira"
    elif(w==3):#Define a pessoa como quarta quando a variável w é 3
        ordem = "quarta"
    elif(w==4):#Define a pessoa como quinta quando a variável w é 4
        ordem = "quinta"
    print("-Preencha com os dados da %s pessoa-" %(ordem))
    print(" ")
    altura = float(input("Informe a a altura da pessoa: "))#Pede para o usuário inserir uma altura
    if(altura>3)or(altura<0):#Pula uma linha caso a altura seja inválida
        print(" ")
    while(altura>3)or(altura<0):#Exige que a altura esteja entre 0 e 3 metros
        print("Informação inválida!")
        altura = float(input("Digite uma altura entre zero e três metros: "))#Pede para o usuário reinserir uma altura
        print(" ")
    idade = int(input("Informe a a idade da pessoa: "))#Pede para o usuário inserir uma idade
    print(" ")
    while(idade>150)or(idade<0):#Exige uma altura entre 0 e 150 anos
        print("Informação inválida!")
        idade = int(input("Digite uma idade entre zero e 150 anos: "))#Pede para o usuário reinserir uma idade
        print(" ")
    alturas.append(altura)#Adiciona a altura à lista "alturas"
    idades.append(idade)#Adiciona a idade à lista "idades"
    w += 1

#Processamento de dados
alturasR = list(reversed(alturas))#Inverte a lista com as alturas
idadesR = list(reversed(idades))#Inverte a lista com as idades

#Saída de dados
print("=========")
print("RESULTADO")
print("=========")
print(" ")
print("Ordem em que foram inseridas:")
print(" ")
print("Alturas: %s." %(alturas))#Mostra a lista de alturas
print("Idades: %s." %(idades))#Mostra a lista de idades
print(" ")
print("Ordem inversa:")
print(" ")
print("Alturas: %s." %(alturasR))#Mostra a lista inversa de alturas
print("Idades: %s." %(idadesR))#Mostra a lista inversa de idades
