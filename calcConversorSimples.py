# Conversor simples sem interface gráfica

temperatura = float(input('Temperatura: '))
unidade = input('Unidade? (C ou F): ').upper()

if unidade == 'C':
    tempConv = (temperatura * 9 / 5) + 32
    print(f'{temperatura:.2f} C = {tempConv:.2f} F')
elif unidade == 'F':
    tempConv = (temperatura - 32) * 5 / 9
    print(f'{temperatura:.2f} F = {tempConv:.2f} C')