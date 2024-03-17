def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado:", soma(num1, num2))
elif opcao == '2':
    print("Resultado:", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Opção inválida")











#Este código permite ao usuário escolher a operação desejada (soma, subtração, multiplicação ou divisão) e, em seguida, inserir os números nos quais a operação será realizada. Em seguida, o código executa a operação selecionada e exibe o resultado