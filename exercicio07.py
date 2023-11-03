n = float(input('numero: '))
print(f'Seu sucessor é {n + 1}')
print(f'Seu antecessor é {n - 1}')
print(f'Seu dobro é {n * 2}')
print(f'Seu triplo é {n * 3}')
print(f'Sua raiz quadrada {n ** (1 / 2)}')
nota1 = float(input('nota1: '))
nota2 = float(input('nota2: '))
print(f'media final {(nota1 + nota2) / 2}')
print(f'n em centímetros {n * 100}, n em milímetros {n * 1000}')
for i in range(11):
    resultado = n * i
    print(resultado)
print(f'voce pode comprar {n / 3.27}')

l: float = float(input('largura: '))
a = float(input('altura: '))
area = a * l
print(f'A área é {area} e quantos litros são necessários para pintar {area}L')

preco = float(input('Preço produto: '))
conta = preco - (preco * 0.05)
print(f'O preço com 5% de desconto é: {conta}')

salario = float(input('Insira seu salário: '))
conta = salario + (salario * 0.15)
print(f'Com o aumento seu salário passará a ser: {conta}')
