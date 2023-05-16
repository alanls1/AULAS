import math

#exem
 
# #numero = int(input("Digite um valor: "))
# resultado = 4/3 * math.pi * math.pow(numero, 3)

# print("resultado:", resultado )
# #Fórmula com o módulo e o numero



# #exer 2

# esfera = 4 * math.pi * math.pow(numero, 2)

# print ("esfera: ",esfera)

# #exer 3 


# print(math.pow(numero, 2), math.pow(numero, 3), math.pow(numero, 4))


#exer 4

# fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# celsius = 5/9 * (fahrenheit - 32)

# print("A temperatura de fahrenheit em graus celsius é ", celsius)

#exer 5

# valor1 = int(input("Digite o valor 1: "))


# valor2 = int(input("Digite o valor 2: "))


# print("Soma dos valores", valor1 , " + " , valor2 ," é = ", valor1 + valor2)

# print("A diferença dos valores", valor1 , " - " , valor2 ," é = ", valor1 - valor2)

# print("A média dos valores", valor1 , " + " , valor2 ," é = ", (valor1 + valor2)/2)

# print("A distância dos valores", valor1 , " + " , valor2 ," é = ", math.fabs(valor1 - valor2))

# print("Maior dos valores", valor1 , " + " , valor2 ," é = ", (valor1 + valor2 + math.fabs(valor1 - valor2))/2)


# print("Menor dos valores", valor1 , " + " , valor2 ," é = ", (valor1 + valor2 - math.fabs(valor1 - valor2))/2)


#exer 6

# valorInteiro = int(input("Valor: "))

# horas = valorInteiro // 3600

# resto = valorInteiro%3600

# minutos = resto // 60

# segundos = resto % 60


# print("Horas: ", horas,":",minutos,":",segundos)



valorInteiro = int(input("Valor: "))

milhar = valorInteiro // 1000

centena = (valorInteiro % 1000)// 100

dezena = ((valorInteiro % 1000)% 100) // 10

unidade = (((valorInteiro % 1000)% 100) % 10) // 1

print("Valor invertido: ", unidade, dezena, centena, milhar)