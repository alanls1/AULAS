# laços e repetição... (for, while, while do)

#jogo da adivinhação

#1 exer
import random

# numeroAleatorio = random.randint(0,100)

# print("Você tem 10 chances para tentar adivinhar qual é o número sorteado aleatoriamente.")

# for cont in range(1,11):

#     adivinheOnumero = int(input("Insira um número:"))
#     print(f"Tentativas: {cont} ")
#     if adivinheOnumero < numeroAleatorio :
#         print("tente novamente um número maior...")
#     elif adivinheOnumero > numeroAleatorio :
#         print("tente novamente um número menor...")
#     else:
#         print("Parabéns, Você ganhou! ")
#         break


#coletando dados fictícios para calculos simples

#2 exer


# somaRenda = 0
# somaIdades = 0
# qtdHomenosMenor30 = 0
# qtdFilhos = 0
# qtdMais3filhos = 0
# rendaHomenMaisVelhos = 0
# idadeHomenMaisVelho = 0
# idadeMulherMaiorRenda = 0
# mulherMaiorRenda = 0
# habitantes = 2000

# for cont in range( 2000):
#     idade = random.randint(18,80)
#     renda =  random.randint(200,5000)
#     genero = random.choice(["m" , "f"])
#     qtdFilhos = random.randint(0,5)

#     somaRenda += renda

#     if qtdFilhos >= 3 :
#         somaIdades += idade
#         qtdMais3filhos += 1
    
#     if genero == "m" and idade < 30 :
#         qtdHomenosMenor30 += 1

#     qtdFilhos += qtdFilhos

#     if genero == "m" and idade > idadeHomenMaisVelho :
#         idadeHomenMaisVelho = idade
#         rendaHomenMaisVelhos = renda

#     if genero == "f" and renda > idadeMulherMaiorRenda :
#         idadeMulherMaiorRenda = idade
#         mulherMaiorRenda = renda 

# mediaRenda = somaRenda / habitantes
# mediaMais3Filhos = somaIdades / qtdMais3filhos 
# mediaFilhos = qtdFilhos / habitantes
# print("Média de renda: ", mediaRenda)
# print(f"Média de idade com mais de 3 filhos: {mediaMais3Filhos}")     
# print(f"Total homens com menos de 30 anos: {qtdHomenosMenor30}")
# print(f"Média de filhos: {mediaFilhos} ")
# print(f"Renda do homem mais velho: {rendaHomenMaisVelhos}")
# print(f"Idade da mulher com maior renda: {idadeMulherMaiorRenda}")


#3 exer

#utilizando WHILE

# primo = int(input("Digite um número: "))
# cont = 0
# d = 1

# while d < primo:
#     primo = int(input("Digite um número: "))
    
#     if primo % d == 0: cont = cont + 1

#     d = d + 1

#     if cont == 2: 
#         print (primo, "é primo") 
#     else: 
#         print("Não é primo")
    

#4 exer

#divisores dos 100 primeiros números
 
# for numero in range (1, 100):
#      for valor in range(1, 100):
#           if numero % valor == 0:
#                print(f"O número: {numero} é divisivel por {valor}")

#5 exer

# quantidade = int(input("Informe a quantidade de primos: "))

# while quantidade <= 0 :
#     print("Valor invalido. A quantidade deve ser positiva")
#     quant = int(input("Informe a quantidade de primos: "))

# num = 2 
# primos = 1

# while primos <= quantidade: 
#     contaDivisores = 0 
#     d = 1
#     while d <= num:
#         if num % d == 0: contaDivisores = contaDivisores + 1
#         d = d + 1

#     if contaDivisores == 2: 
#         print(f"{num} é primo")
#         primos = primos + 1
    
#     num = num + 1

#6 exer

# quant = int(input("Informe a quantidade de valores pares: "))

# while quant <= 0:
#     print("Valor invalido. A quantidade deve ser positiva")
#     quant = int(input("Informe a quantidade de valores pares: "))


# num = 4
# pares = 1

# while pares <= quant:
#     print("Numero: ", num)

#     parte1 = num//2
#     parte2 = parte1

#     while parte2 <= parte1: 
#         primosCont1 = 0
#         d = 1 
#         while d <= parte1:
#             if parte1 % d == 0: primosCont1 = primosCont1 + 1
#             d = d + 1

#         if primosCont1 == 2:
#             d = 1
#             primosCont2 = 0
#             while d <= parte2:
#                 if parte2 % d == 0: primosCont2 = primosCont2 + 1
#                 d = d + 1

#             if primosCont2 == 2:
#                 print(f"{parte1} e {parte2} são primos")
#                 pares = pares + 1
#                 break
        
#         parte1 = parte1 + 1 
#         parte2 = parte2 - 1


#     num = num + 2

#exer 7

# numero = 0 
# while numero < 100:
#     fat = 1
#     aux = 2
#     while aux <= numero:
#         fat = fat * aux
#         aux = aux + 1
    
#     print("O fatorial de ", numero, "eh  ", fat)
#     numero = numero + 1


#exer 8
# quant = int(input("Informe um numero negativo para parar a repetição: "))

# quant0a25 = 0
# quant25a51 = 0
# quant51a76 = 0
# quant76a100 = 0

# while quant >= 0:
   
    
#     if quant <= 25: quant0a25 = quant0a25 + 1
#     else: 
#         if quant <= 50: quant25a51 = quant25a51 + 1
#         else: 
#             if quant <= 75: quant51a76 = quant51a76 + 1
#             else: 
#                 if quant <= 100: quant76a100 = quant76a100 + 1
    
#     quant = int(input("Informe um numero negativo para parar a repetição: "))

    
# print(f"0 a 25: {quant0a25},\n26 a 50: {quant25a51},\n51 a 76: {quant51a76},\n76 a 100: {quant76a100}")

#exer 9

somaSalario = 0
pessoas = 0
maior = 0
menor = 120
mulheresQtt = 0
while True:
    idade = int(input("Idade: "))

    while idade <= 0  or idade > 120:  
        print("Idade invalida")
        idade = int(input("Idade: "))
        break


    sexo  = int(input("Sexo: \n1 - masculino, 2 - feminino: "))

    while sexo < 1 or sexo > 2:  
        print("sexo invalido")
        sexo = int(input("Sexo: \n1 - masculino, 2 - feminino: "))

    salario = int(input("Salario: "))

    while salario < 0:  
        print("salario invalido")
        salario = int(input("Salario: "))

    somaSalario = somaSalario + salario
    pessoas = pessoas + 1
    if idade > maior: maior = idade 
    if idade < menor: menor = idade
    if sexo == 1 and salario <= 3500: mulheresQtt = mulheresQtt + 1



if pessoas == 0: print("Dados não informados")
else:
    print("media de salario: ", somaSalario/pessoas)
    print(" maior idade do grupo ", maior)
    print(" menor idade do grupo ", menor)
    print(" Quantidade de mulheres que ganham ate R% 3500 ", mulheresQtt)