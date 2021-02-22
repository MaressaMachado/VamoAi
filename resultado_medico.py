print('\n')
print('-' * 45)
print("RESULTADO MÉDICO")
print('-' * 45)

#Funcão para o resultado do exame médico

def resultado_exame(resultado): 
    if (resultado >= 7) and (resultado <= 10):
        return 'O seu resultado está bom, continue se cuidando'
    elif (resultado < 6) and (resultado >= 4): 
        return('O seu resultado está na média, busque um acompanhamento médico.')
    elif (resultado < 4) and (resultado >= 0):
        print('O seu resultado não está nada bom, busque um auxílio o quanto antes!')

paciente_um = int(input("Digite o resultado do paciente 1: "))
paciente_dois = int(input("Digite o resultado do paciente 2: "))
paciente_tres = int(input("Digite o resultado do paciente 3: "))

print(f"Resultado paciente 1: {resultado_exame(paciente_um)}")
print(f"Resultado paciente 2: {resultado_exame(paciente_dois)}")
print(f"Resultado paciente 3: {resultado_exame(paciente_tres)}")



     


