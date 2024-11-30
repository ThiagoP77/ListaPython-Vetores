"""
Nome do programador: Thiago Piffer Lauro
Nome do programa:  6. Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
Data: 13/11/21
"""
#Entrada e Processamento de dados
medias = []#Cria a lista para receber as médias
aprovacao = []#Cria a lista para receber as médias a cima de 7
w = 0#Variável que controla quantas vezes o primeiro while se repete
wh = 0#Variável que controla quantas vezes o segundo while se repete
soma = 0#Variável que vai receber a soma das notas de cada aluno
print("==============================")
print("PROGRAMA QUE CALCULA APROVAÇÃO")
print("==============================")
print(" ")
while(w<10):#Comando que pede para inserir as quatro notas de 10 alunos
    if(w==0):#Define o aluno como primeiro quando a variável w é 0
        ordem = "primeiro"
    elif(w==1):#Define o aluno como segundo quando a variável w é 1
        ordem = "segundo"
    elif(w==2):#Define o aluno como terceiro quando a variável w é 2
        ordem = "terceiro"
    elif(w==3):#Define o aluno como quarto quando a variável w é 3
        ordem = "quarto"
    elif(w==4):#Define o aluno como quinto quando a variável w é 4
        ordem = "quinto"
    elif(w==5):#Define o aluno como sexto quando a variável w é 5
        ordem = "sexto"
    elif(w==6):#Define o aluno como sétimo quando a variável w é 6
        ordem = "sétimo"
    elif(w==7):#Define o aluno como oitavo quando a variável w é 7
        ordem = "oitavo"
    elif(w==8):#Define o aluno como nono quando a variável w é 8
        ordem = "nono"
    elif(w==9):#Define o aluno como décimo quando a variável w é 9
        ordem = "décimo"
    print("-Preencha com os dados do %s aluno-"%(ordem))
    print(" ")
    while(wh<4):##Comando que pede para inserir as quatro notas
        if(wh==0):#Define a nota como primeira quando a variável wh é 0
            ordem2 = "primeira"
        elif(wh==1):#Define a nota como segunda quando a variável wh é 1
            ordem2 = "segunda"
        elif(wh==2):#Define a nota como terceira quando a variável wh é 2
            ordem2 = "terceira"
        elif(wh==3):#Define a nota como quarta quando a variável wh é 3
            ordem2 = "quarta"
        nota = float(input("Informe a %s nota: "%(ordem2)))#Pede para o usuário inserir a nota
        if(nota<0)or(nota>10):#Pula espaço quando a nota é inválida
            print(" ")
        while(nota<0)or(nota>10):#Exige que o usuário insira uma nota entre 0 e 10
            print("Nota inválida!")
            nota = float(input("Digite uma nota entre zero e dez: "))#Pede para o usuário reinserir a nota
            print(" ")
        soma += nota#Adiciona a nota à variável soma
        wh += 1#Adiciona 1 à variável wh
    media = (soma/4)#Calcula a média
    medias.append(media)#Adiciona a média à lista "medias"
    if(media>=7):#Adiciona a média a lista "aprovação" quando é maior ou igual a 7
        aprovacao.append(media)
    print(" ")
    soma = 0#Zera a variável soma
    media = 0#Zera a variável media
    wh = 0#Zera a variável wh
    w += 1#Adiciona 1 à variável w
        
#Saída de dados
print("=========")
print("RESULTADO")
print("=========")
print(" ")
print("Média de cada aluno: %s." %(medias))#Mostra a lista "medias"
print("Médias a cima ou igual a sete: %s." %(aprovacao))#Mostra a lista "aprovacao"
print("Número de alunos aprovados: %d." %(len(aprovacao)))#Mostra o número de alunos aprovados
