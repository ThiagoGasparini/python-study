idade = eval(input('Informe a idade da criança: \n'))

if idade < 5:
    print('A criança deve ser vacinada contra a gripe.')
    print('Procure o posto de saúde mais próximo.')
elif idade == 5:
    print('A vacina estará disponível em breve.')
    print('Aguarde as próximas informações.')
else:
    print('A vacinação só ocorrerá daqui a 3 meses.')
    print('Informe-se novamente neste prazo.')
print('Cuide da saúde sempre. Até a próxima.')

""" Exercicio 1 """
num = eval(input('digite um numero: \n'))

if num % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')


""" Exercicio 2 """

nota = eval(input('digite a nota: \n'))

if (nota >= 7):
    print('Aluno Aprovado')
elif (nota >= 5):
    print('Aluno em Recuperação')
else:
    print('Aluno Reprovado')


""" Exercicio 3 """

lista = [10, 2, 5, 7, 6, 2]

soma = 0

for item in lista:
    if item % 2 == 0:
        soma += item

print(soma)
