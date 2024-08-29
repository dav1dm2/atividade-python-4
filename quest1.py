''' o codigo usa do princinpio de Fibonacci de somar os 2 termos anteriores de uma sequencia e exibe
dentro do loop de while enquanto a soma não atingir 500'''

print("série de Fibonacci até que o valor seja maior que 500:")

a, b = 0, 1

while a <= 500:
    print(a, end=' ')
    a, b = b, a + b
