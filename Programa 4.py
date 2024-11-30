"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 4. Faça um Programa que leia uma lista de 10 caracteres, e
diga quantas consoantes foram lidas. Imprima as consoantes.
Data: 13/11/21
"""
#Entrada e Processamento de dados
consoantes = []#Cria a lista que vai receber as consoantes
w = 0#Variável que controla quantas vezes o while se repete
print("==================================")
print("PROGRAMA QUE IDENTIFICA CONSOANTES")
print("==================================")
print(" ")
print("-Insira os caracteres abaixo-")
print(" ")
while(w<10):#Comando que pede para o usuário inserir 10 caracteres e adiciona as consoantes a lista
    if(w==0):#Define o caractere como primeiro quando a variável w é 0
        ordem = "primeiro"
    elif(w==1):#Define o caractere como segundo quando a variável w é 1
        ordem = "segundo"
    elif(w==2):#Define o caractere como terceiro quando a variável w é 2
        ordem = "terceiro"
    elif(w==3):#Define o caractere como quarto quando a variável w é 3
        ordem = "quarto"
    elif(w==4):#Define o caractere como quinto quando a variável w é 4
        ordem = "quinto"
    elif(w==5):#Define o caractere como sexto quando a variável w é 5
        ordem = "sexto"
    elif(w==6):#Define o caractere como sétimo quando a variável w é 6
        ordem = "sétimo"
    elif(w==7):#Define o caractere como oitavo quando a variável w é 7
        ordem = "oitavo"
    elif(w==8):#Define o caractere como nono quando a variável w é 8
        ordem = "nono"
    elif(w==9):#Define o caractere como décimo quando a variável w é 9
        ordem = "décimo"
    letra = str(input("Informe o %s caractere: " %(ordem)))#Pede para o usuário inserir um caractere
    if(len(letra)>1):#Pula uma linha quando digita mais de um caractere
        print(" ")
    while(len(letra)>1):#Comando que exige que apenas um caractere seja digitado de cada vez
        print("Caractere inválido!")
        letra = str(input("Digite apenas um caractere por vez: "))#Pede para o usuário inserir um caractere
        print(" ")
    if(letra=="B")or(letra=="C")or(letra=="D")or(letra=="F")or(letra=="G")or\
    (letra=="H")or(letra=="J")or(letra=="K")or(letra=="L")or(letra=="M")or\
    (letra=="N")or(letra=="P")or(letra=="Q")or(letra=="R")or(letra=="S")or\
    (letra=="T")or(letra=="V")or(letra=="W")or(letra=="X")or(letra=="Y")or\
    (letra=="Z")or(letra=="b")or(letra=="c")or(letra=="d")or(letra=="f")or\
    (letra=="g")or(letra=="h")or(letra=="j")or(letra=="k")or(letra=="l")or\
    (letra=="m")or(letra=="n")or(letra=="p")or(letra=="q")or(letra=="r")or\
    (letra=="s")or(letra=="t")or(letra=="v")or(letra=="w")or(letra=="x")or\
    (letra=="y")or(letra=="z")or(letra=="ç")or(letra=="Ç"):#Comando que define quando a letra digitada é consoante
        consoantes.append(letra)#Adiciona a letra à lista "consoantes"
    w += 1#Soma 1 à variável w

#Saída de dados
print(" ")
if(len(consoantes)==0):#Gera o resultado quando nenhum caractere digitado é consoante
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Nenhum dos caracteres digitados é consoante!")

else:#Gera o resultado quando um ou mais caracteres digitados são consoantes
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Número de consoantes digitadas: %d." %(len(consoantes)))#Mostra o número de consoantes digitadas
    print("Consoantes digitadas: %s." %(consoantes))#Mostra as consoantes digitadas
