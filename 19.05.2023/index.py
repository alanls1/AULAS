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


somaRenda = 0
somaIdades = 0
qtdHomenosMenor30 = 0
qtdFilhos = 0
qtdMais3filhos = 0
rendaHomenMaisVelhos = 0
idadeHomenMaisVelho = 0
idadeMulherMaiorRenda = 0
mulherMaiorRenda = 0
habitantes = 2000

for cont in range( 2000):
    idade = random.randint(18,80)
    renda =  random.randint(200,5000)
    genero = random.choice(["m" , "f"])
    qtdFilhos = random.randint(0,5)

    somaRenda += renda

    if qtdFilhos >= 3 :
        somaIdades += idade
        qtdMais3filhos += 1
    
    if genero == "m" and idade < 30 :
        qtdHomenosMenor30 += 1

    qtdFilhos += qtdFilhos

    if genero == "m" and idade > idadeHomenMaisVelho :
        idadeHomenMaisVelho = idade
        rendaHomenMaisVelhos = renda

    if genero == "f" and renda > idadeMulherMaiorRenda :
        idadeMulherMaiorRenda = idade
        mulherMaiorRenda = renda 

mediaRenda = somaRenda / habitantes
mediaMais3Filhos = somaIdades / qtdMais3filhos 
mediaFilhos = qtdFilhos / habitantes
print("Média de renda: ", mediaRenda)
print(f"Média de idade com mais de 3 filhos: {mediaMais3Filhos}")     
print(f"Total homens com menos de 30 anos: {qtdHomenosMenor30}")
print(f"Média de filhos: {mediaFilhos} ")
print(f"Renda do homem mais velho: {rendaHomenMaisVelhos}")
print(f"Idade da mulher com maior renda: {idadeMulherMaiorRenda}")