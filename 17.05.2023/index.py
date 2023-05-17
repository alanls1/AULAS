#exercicios sobre condições if else


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

