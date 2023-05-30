#Fase 1 da avaliação


averageTemperature = 0  
mostHotMonth = -90
referenceMostHotMonth = 0
mostColdMonth = 60
referenceMostcoldMonth = 0
numberWarmMonths = 0
 
for month in range(1, 13):
    temperature = float(input(f"Informe uma temperatura para o mês {month}: ")) 

    while temperature < -90 or temperature > 60:
        print("Temperatura inválida.\nPor favor, informe um valor entre -90 a 60 graus")
        temperature = int(input(f"Informe uma temperatura para o mês {month}: "))

    averageTemperature =  averageTemperature + temperature

    if temperature > 40: numberWarmMonths = numberWarmMonths + 1
    
    if temperature > mostHotMonth: 
        mostHotMonth =  temperature
        referenceMostHotMonth = month

    if temperature < mostColdMonth: 
        mostColdMonth =  temperature
        referenceMostColdMonth = month

print("\n ---------------------------")
print("\nTemperatura média máxima anual: ", averageTemperature / 12)
print("---------------------------")
print("\nQuantidade de meses escaldante do ano: ", numberWarmMonths)
print("---------------------------")

if referenceMostHotMonth == 1: print("\nJaneiro foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 2: print("\nFevereiro foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 3: print("\nMarço foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 4: print("\nAbril foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 5: print("\nMaio foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 6: print("\nJunho foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 7: print("\nJulho foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 8: print("\nAgosto foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 9: print("\nSetembro foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 10: print("\nOutubro foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 11: print("\nNovembro foi o mês mais quente: ", mostHotMonth)
if referenceMostHotMonth == 12: print("\nDezembro foi o mês mais quente: ", mostHotMonth)
print("---------------------------")

if referenceMostColdMonth == 1: print("\nJaneiro foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 2: print("\nFevereiro foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 3: print("\nMarço foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 4: print("\nAbril foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 5: print("\nMaio foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 6: print("\nJunho foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 7: print("\nJulho foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 8: print("\nAgosto foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 9: print("\nSetembro foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 10: print("\nOutubro foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 11: print("\nNovembro foi o mês mais frio: ", mostColdMonth)
if referenceMostColdMonth == 12: print("\nDezembro foi o mês mais frio: ", mostColdMonth)
print("\n ---------------------------")