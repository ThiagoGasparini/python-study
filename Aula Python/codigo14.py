def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')


def somarPar(list):
    soma = 0
    for num in list:
        if num % 2 == 0:
            soma += num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somarPar(lista)
print(f'o somatorio dos elementos pares é: {soma}')
