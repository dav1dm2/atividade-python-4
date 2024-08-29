#o codigo permite que o usuario faça 2 operações matematicas o quanto quiser ou encerrar o programa 

def soma(a, b):
    resultado = a + b
    return resultado

def subtracao(a, b):
    resultado = a - b
    return resultado

while True:
    print("\nescolha a operação que deseja:")
    print("1. somar")
    print("2. subtrair")
    print("3. encerrar o programa")
    
    opcao = input("digite 1, 2 ou 3: ")

    if opcao == '1':
        try:
            a = float(input('digite o primeiro valor: '))
            b = float(input('digite o segundo valor: '))
            resultado = soma(a, b)
            print(f" resultado da soma é: {resultado:.2f}")
        except ValueError:
            print("entrada inválida. digite um NUMERO.")

    elif opcao == '2':
        try:
            a = float(input('digite o primeiro valor: '))
            b = float(input('digite o segundo valor: '))
            resultado = subtracao(a, b)
            print(f"o resultado da subtração é: {resultado:.2f}")
        except ValueError:
            print("entrada inválida. digite um NUMEROOOO.")

    elif opcao == '3':
        print("encerrando o programa.")
        break

    else:
        print("Opção inválida!escolha 1, 2 ou 3.")
