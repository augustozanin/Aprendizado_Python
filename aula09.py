# Manipulando cadeias de Texto

frase = 'Curso em video Python'

# Fatiamento
print(frase[9:21])
print(frase[9:21:2])  # Pulando de dois em dois do indice 9 ao 20

# Análise

print(len(frase))
print(frase.count('o'))  # Contar as ocorrencias de o na frase
print(frase.find('deo'))  # Mostra a posição onde começa
var = 'Curso' in frase
print(var)
frase2 = frase.replace('Python', 'Android')
print(frase2)

# Remover espaços antes e depois das palavras
print(frase.strip())
# Outro caso, se eu quiser remover os espaços somente da direira uso r rigth e l de left
print(frase.lstrip())

# DIVISÃO DE STRINGS
# usamos o split(), onde cada elemento vai ser separado por o separador setado como split(',')
dividido = frase.split()
print(dividido)
# PODEMOS JUNTAR TUDO COM JOIN '-'.join(frase)
juntado = ' '.join(dividido)
print(juntado)
# DESAFIOS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
"""
nome = input('Nome: ')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nome.split()[0]))
"""
# 2
"""
numero = float(input('Numero: '))
milhar = int(numero // 1000)
centena = int((numero % 1000) // 100)
dezena = int((numero % 100) // 10)
unidade = int((numero % 10) // 1)

print(f'Milhar: {milhar}, Centena: {centena}, Dezena: {dezena}, Unidade: {unidade}')
"""
"""
# 3
cidade = str(input('Cidade: '))
print(cidade[0:5] == 'SANTO')
# 4
nome = input('Nome: ')
print('SILVA' in nome)
"""
# 5
frase3 = input('frase: ')
print(frase3.count('A'))
print(frase3.find('A'))
print(frase3.find('A'))