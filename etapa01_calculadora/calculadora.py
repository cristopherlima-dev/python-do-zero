# Parte 1 - Título da calculadora

# TODO: crie uma variável chamada titulo que receba o texto === CALCULADORA ===
titulo = '=== CALCULADORA ==='

# TODO: use o print() para mostrar o conteúdo da variável titulo
print(titulo)

# Parte 2 - Entrada de dados

# TODO: crie a variável numero1 recebendo o que o usuário digitar,
#       com a mensagem "Digite o primeiro número: "
numero1 = input('Digite o primeiro número: ')

# TODO: converta numero1 para decimal
#       (por que decimal e não inteiro? responda num comentário)
numero1 = float(numero1) # Decimal, porque o usuário pode digitar números com casas decimais

# TODO: faça o mesmo para numero2 (ler E converter),
#       com a mensagem "Digite o segundo número: "
numero2 = input('Digite o segundo número: ')
numero2 = float(numero2) # Decimal, porque o usuário pode digitar números com casas decimais

# TODO: crie a variável operacao recebendo a mensagem "Escolha a operação (+ - * /): "
#       (ela precisa de conversão? por quê? responda num comentário)
operacao = input('Escolha a operação (+ - * /): ') # não precisa de conversão porque não são números

# TODO: mostre numero1, numero2 e operacao num único print() para conferir
print(f'Primeiro Numero é {numero1}. Segundo Numero é {numero2}. Operação Escolhida: {operacao}')