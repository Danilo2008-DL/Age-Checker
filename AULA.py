diadenascimento = int(input('Dia de nascimento'))
mesdenascimento = int(input('Mes de nascimento'))
anodenascimento = int(input('Ano de nascimento'))
ano = int(input('Em que ano estamos?'))
anosub = ano - anodenascimento
print('parabéns acesso concedido!')
print('Bom trabalho e bom dia!')
if anosub < 18:
   print('de menor...')
elif anosub > 18:
      print('acesso concedido')

