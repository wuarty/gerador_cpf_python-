import sys
import random


print(random.randint(0, 999999999))

nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador = 10


resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador
    contador -= 1
digito_1 = 11 - (resultado_1 % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11

resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1
digito_2 = 11 - (resultado_2 % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

print(f"CPF gerado: {cpf_gerado}")
