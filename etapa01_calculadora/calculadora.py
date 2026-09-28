# Parte 1 - Título da calculadora

# TODO: crie uma variável chamada titulo que receba o texto === CALCULADORA ===
titulo = "=== CALCULADORA ==="

# TODO: use o print() para mostrar o conteúdo da variável titulo
print(titulo)

# Parte 2 - Entrada de dados

# TODO: crie a variável numero1 recebendo o que o usuário digitar,
#       com a mensagem "Digite o primeiro número: "

# TODO: converta numero1 para decimal (por que decimal e não inteiro?)
# Resposta: Porque o usuário pode digitar valores quebrados
numero1 = float(input("Digite o primeiro número: "))

# TODO: faça o mesmo para numero2, com a mensagem "Digite o segundo número: "
numero2 = float(input("Digite o segundo número: "))

# TODO: crie a variável operacao recebendo a mensagem "Escolha a operação (+ - * /): "
#       (ela precisa de conversão? por quê?)
# Resposta: Não, pois é um texto que o usuário está digitando e permanecerá como texto.
operacao = input("Escolha a operação (+ - * /): ")

# TODO: mostre numero1, numero2 e operacao num único print() para conferir
print(f"1o número: {numero1}, 2o número: {numero2}, Operação Selecionada: {operacao}")
