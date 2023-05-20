#exercicios sobre condições if else

import math

#exer 1

# sexo = int(input("Digite o sexo: \n1 - Feminino \n2 - Masculino\n"))
# altura = float(input("Digite sua altura: "))

# if sexo == 1 : 
#     print("Seu peso ideal é ", 62.1 * altura - 44.7)
# elif sexo == 2:
#     print("Seu peso ideal é ", 72.7 * altura - 44.7)
# else :
#     print("Número inválido")

#exer 2

# inicioH = int(input("o jogo começou que horas: "))
# inicioM = int(input("e minutos: "))
# fimH = int(input("o jogo terminou que horas: "))
# fimM = int(input("e minutos: "))

# if fimH < inicioH :
#     horaInicial = inicioH * 60 + inicioM
   
#     outroDia = 24 * 60 - horaInicial + (fimH * 60 + fimM)

#     tempoDoJogoEmHoras = outroDia // 60

#     if tempoDoJogoEmHoras < 1 : tempoDoJogoEmHoras = 0.0

#     tempoDoJogoEmMinutos = outroDia % 60


# else:
    
#     paraMinutosInicio = ( inicioH * 60 ) + inicioM

#     paraMinutosFim = ( fimH * 60 ) + fimM

#     tempoDoJogoEmMinutosTotal = paraMinutosFim - paraMinutosInicio

#     tempoDoJogoEmHoras = tempoDoJogoEmMinutosTotal // 60

#     if tempoDoJogoEmHoras < 1 : tempoDoJogoEmHoras = 0.0

#     tempoDoJogoEmMinutos = tempoDoJogoEmMinutosTotal % 60

# print("Duração do jogo foi: ", tempoDoJogoEmHoras, "hora e " , tempoDoJogoEmMinutos, " minutos")


#exer 3

# numero = int(input("Informe um número: "))
 
# if 10000 > numero > 999 :
#     milhar = numero // 1000

#     centena = (numero % 1000)// 100

#     dezena = ((numero % 1000)% 100) // 10

#     unidade = (((numero % 1000)% 100) % 10) // 1

#     numeroInvertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar 

#     if numero == numeroInvertido :
#         print("Número capicua")
#     else:
#         print("Não é capicua")

# else:
#     print("Valor inválido")



#exer 3

# valor1 = int(input("Informe o primeiro valor: "))

# valor2 = int(input("Informe o primeiro valor: "))

# valor3 = int(input("Informe o primeiro valor: "))


# maiorValor = valor1

# if valor2 > valor1 : maiorValor = valor2
# if valor3 > valor1 : maiorValor = valor3

# menorValor = valor1

# if valor2 < valor1 : menorValor = valor2
# if valor3 < valor1 : menorValor = valor3

# meio = valor1 + valor2 + valor3 - maiorValor - menorValor

# print(maiorValor, meio ,menorValor)



#exer 4 

# valor1 = int(input("Informe o primeiro valor: "))

# valor2 = int(input("Informe o primeiro valor: "))

# valor3 = int(input("Informe o primeiro valor: "))

# valor4 = int(input("Informe o primeiro valor: "))

# if  valor2 < valor1 : 
#     aux = valor1
#     valor1 = valor2
#     valor2 = aux

# if  valor3 < valor1 : 
#     aux = valor1
#     valor1 = valor3
#     valor3 = aux

# if  valor4 < valor1 : 
#     aux = valor1
#     valor1 = valor4
#     valor4 = aux

# if  valor3 < valor2 : 
#     aux = valor2
#     valor2 = valor3
#     valor3 = aux

# if  valor4 < valor2 : 
#     aux = valor2
#     valor2 = valor4
#     valor4 = aux

# if  valor4 < valor3 : 
#     aux = valor3
#     valor3 = valor4
#     valor4 = aux

# print(valor1, valor2, valor3, valor4)


#exer 5

# preco = float(input("Informe o preço: "))

# if preco <= 0 :
#     print("Valor inválido")
# elif preco >= 10 : 
#     precoFinal = preco * 1.7 
# elif 10 < preco > 30: 
#     precoFinal = preco * 1.5 
# elif 30 < preco > 50: 
#     precoFinal = preco * 1.4 
# else: 
#     precoFinal = preco * 1.3 

# print ("Valor final: ", precoFinal)


#exer 6

# diaDaSemana = int(input("Informe um numero de 1 a 7: "))


# if diaDaSemana == 1 : print("Hoje é Domingo")
# elif diaDaSemana == 2 : print("Hoje é segunda-feira")
# elif diaDaSemana == 3 : print("Hoje é terça-feira")
# elif diaDaSemana == 4 : print("Hoje é quarta-feira")
# elif diaDaSemana == 5 : print("Hoje é quinta-feira")
# elif diaDaSemana == 6 : print("Hoje é sexta-feira")
# elif diaDaSemana == 7 : print("Hoje é sábado")
# else:
#     print("Número inválido") 

#exer 7

# nota1 = int(input("Insira a nota 1: "))
# nota2 = int(input("Insira a nota 2: "))
# nota3 = int(input("Insira a nota 3: "))

# if nota1 < 0 or nota1 >10 or nota2 < 0 or nota2 >10 or nota3 < 0 or nota3 >10:
#     print("Nota inválida")
# else:
#     maior = nota1
#     if nota2 > maior: maior = nota2
#     if nota3 > maior: maior = nota3
#     media = 0.5 * maior + 0.25 * (nota1 + nota2 + nota3 - maior)


# print("Média: ", media)

#exer 8

# valora = float(input("Valor a: "))
# valorb = float(input("Valor b: "))
# valorc = float(input("Valor c: "))

# delta = math.pow(valorb, 2) - 4 * valora * valorc

# print("Delta: ",delta)

# if delta < 0 or valora == 0:
#     print("Delta é , ou divisão por zero")
# else :
#     valorX1 = (- valorb + math.sqrt(delta)) / 2 * valora

#     valorX2 = (- valorb - math.sqrt(delta)) / 2 * valora

#     print(valorX1)

#     print(valorX2)


#exer 9

# saldoMedio = float(input("Informe o saldo: "))

# if saldoMedio <= 0 :
#     print("Sem saldo")
# elif saldoMedio <= 500 : 
#     print("Não há limite")
# elif saldoMedio > 500 and saldoMedio < 1000: 
#     saldoMedioFinal = saldoMedio * 1.08 
#     print ("Saldo final: ", saldoMedioFinal)
# else: 
#     saldoMedioFinal = saldoMedio * 1.15
#     print ("Saldo final: ", saldoMedioFinal)


#exer 10

ano = int(input("Ano: "))
mes = int(input("Mês: "))


if mes == 2:
    if ( ano % 4  == 0 and ano % 100 != 0 ) or ( ano % 400 == 0 ) :
        print("è bissexto")
        dias = 29
    else:
        print("Não é bissexto... ")
        dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
    dias = 30
else:
    dias = 31
    