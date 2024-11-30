"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 3. Faça um Programa que leia 4 notas, mostre as notas e
a média na tela (utilizando lista).
Data: 13/11/21
"""
#Entrada de dados
notas = []#Comando que cria a lista para receber as notas
w = 0#Variável que controla quantas vezes o while se repete
print("=====================================")
print("PROGRAMA QUE CALCULA A MÉDIA DE NOTAS")
print("=====================================")
print(" ")
print("-Insira as notas abaixo-")
print(" ")
while(w<4):#Comando que pede para o usuário inserir quatro notas e adiciona elas à lista
    if(w==0):#Define a nota como primeira caso w seja igual a 0
        ordem = "primeira"
    elif(w==1):#Define a nota como segunda caso w seja igual a 1
        ordem = "segunda"
    elif(w==2):#Define a nota como terceira caso w seja igual a 2
        ordem = "terceira"
    elif(w==3):#Define a nota como quarta caso w seja igual a 3
        ordem = "quarta"
    nota = float(input("Informe sua %s nota: " %(ordem)))#Comando que pede para o usuário inserir uma nota
    if(nota<0):#Pula uma linha se a nota for menor que 0
        print(" ")
    while(nota<0):#Comando que exige uma nota positiva
        print("Nota inválida!")
        nota = float(input("Digite uma nota positiva: "))
        print(" ")
    if(nota>0):#Quando a nota for positiva, adiciona ela à lista e soma 1 à variável w
        notas.append(nota)
        w += 1
                 
#Processamento de dados
media_notas = (sum(notas)/len(notas))#Calcula a média das notas 

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Notas: %s." %(notas))#Mostra a lista contendo as notas
print("Média das notas: %.2f." %(media_notas))#Mostra a média das notas
