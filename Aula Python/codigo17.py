def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)

regressiva(eval(input('digite um numero para regredir ')))