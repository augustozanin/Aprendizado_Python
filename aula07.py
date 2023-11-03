# Ordem de precedencia no python
"""
() -> parenteses
** -> Potencias
* / // % -> vezes, divisao, divisao exata, divisao inteira somente, resto da divisao
+ - mais e menos
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print(f'Soma {s} \n',
      f'Divisão {d:.2f} \n',
      f'Multiplicação {m} \n',
      f'Divisão Inteira {di} \n',
      f'Exponenciação {e:.2f} \n')
