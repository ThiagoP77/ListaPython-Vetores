"""
Nome do programador: Thiago Piffer Lauro
Nome do programa:  2. Faça um Programa que leia uma lista de 10 números reais
e mostre-os na ordem inversa.
Data: 13/11/21
"""
#Entrada de dados
numerosreais = []#Comando que cria a lista para receber os número reais digitados
w = 0#Variável que controla quantas vezes o while se repete
print("==================================================")
print("PROGRAMA QUE MOSTRA NÚMEROS REAIS NA ORDEM INVERSA")
print("==================================================")
print(" ")
print("-Informe os números abaixo-")
print(" ")
while(w<10):#Comando que pede para o usuário inserir um número dez vezes e os adiciona a lista "numerosreais"
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
    numero = float(input("Informe o %s número: " %(ordem)))#Comando que pede para o usuário inserir um número
    numerosreais.append(numero)#Adiciona o número digitado à lista "numerosreais"
    w += 1#Adiciona 1 à variável w
    
#Processamento de dados
reversoreal = list(reversed(numerosreais))#Comando que cria outra lista, como inversa da segunda

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Lista com os números na ordem em que foram digitados: %s." %(numerosreais))#Mostra a lista de números digitados
print("Ordem inversa: %s." %(reversoreal))#Mostra a lista de números digitados na ordem inversa
