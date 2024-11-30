"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 10. Faça um Programa que leia duas listas com 10 elementos
cada. Gere um terceiro vetor de 20 elementos, cujos valores
deverão ser compostos pelos elementos intercalados de duas outras listas.
Data: 13/11/21
"""
#Entrada de dados
lista1 = []#Lista que vai receber os 10 primeiros números
lista2 = []#Lista que vai receber os 10 últimos números
lista3 = []#Lista que vai intercalar os números das outras duas listas
w = 0#Variável que controla quantas vezes o primeiro while se repete
wh =0#Variável que controla quantas vezes o segundo while se repete
whi = 0#Variável que controla quantas vezes o terceiro while se repete
print("=============================")
print("PROGRAMA QUE INTERCALA LISTAS")
print("=============================")
print(" ")
while(w<2):#Comando que pede para o usuário inserir um número dez vezes e os adiciona à lista "numerosreais"
    if(w==0):#Define a lista como primeira quando a variável w é 0
        ordem = "primeira"
    elif(w==1):#Define a lista como segunda quando a variável w é 1
        ordem = "segunda"
    print("-Insira com os números da %s lista-" %(ordem))
    print(" ")
    while(wh<10):
        if(wh==0):#Define o número como primeiro quando a variável wh é 0
            ordem = "primeiro"
        elif(wh==1):#Define o número como segundo quando a variável wh é 1
            ordem = "segundo"
        elif(wh==2):#Define o número como terceiro quando a variável wh é 2
            ordem = "terceiro"
        elif(wh==3):#Define o número como quarto quando a variável wh é 3
            ordem = "quarto"
        elif(wh==4):#Define o número como quinto quando a variável wh é 4
            ordem = "quinto"
        elif(wh==5):#Define o número como sexto quando a variável wh é 5
            ordem = "sexto"
        elif(wh==6):#Define o número como sétimo quando a variável wh é 6
            ordem = "sétimo"
        elif(wh==7):#Define o número como oitavo quando a variável wh é 7
            ordem = "oitavo"
        elif(wh==8):#Define o número como nono quando a variável wh é 8
            ordem = "nono"
        elif(wh==9):#Define o número como décimo quando a variável wh é 9
            ordem = "décimo"
        numero = float(input("Informe o %s número: " %(ordem)))#Pede para o usuário inserir um número
        if(numero in lista1) or (numero in lista2):#Pula linha quando é inserido um valor inválido
            print(" ")
        while(numero in lista1) or (numero in lista2):#Impede que o usuário repita números
            print("Número inválido!")
            numero = float(input("Digite um número que ainda não esteja na primeira ou segunda lista: "))#Pede para o usuário reinserir um número
            print(" ")
        if(w==0):#Adiciona o número digitado à primeira lista quando w vale 0
            lista1.append(numero)
        elif(w==1):#Adiciona o número digitado à segunda lista quando w vale 1
            lista2.append(numero)
        wh += 1#Adiciona 1 à wh
    print(" ")
    wh = 0#Define wh como 0
    w += 1#Adiciona 1 à w
    
#Processamento de dados
while(whi<10):#Adiciona elementos da primeira e segunda listas à terceira de modo intercalado, até que a mesma possua 20 elementos
    lista3.append(lista1[whi])#Adiciona o elemento da lista1 que corresponde ao valor de whi à lista3
    lista3.append(lista2[whi])#Adiciona o elemento da lista2 que corresponde ao valor de whi à lista3
    whi += 1#Adiciona 1 à whi
    
#Saída de dados
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Primeira lista: %s." %(lista1))#Mostra a primeira lista 
print("Segunda lista: %s." %(lista2))#Mostra a segunda lista 
print("Terceira lista: %s." %(lista3))#Mostra a terceira lista 
