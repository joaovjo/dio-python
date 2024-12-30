# def salvar_carro(ano, modelo, marca, placa):
#     print(f"Carro salvo com sucesso! {marca, modelo, ano, placa}" )
    
# salvar_carro(2020, "Civic", "Honda", "ABC1234")

# salvar_carro(marca="Honda", modelo="Civic", ano=2022, placa="ABC1234")

# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 2019, "placa": "tgk1234"})

# *args e **kwargs são utilizados para passar argumentos variáveis para uma função
# *args é utilizado para passar argumentos variáveis posicionais - tupla
# **kwargs é utilizado para passar argumentos variáveis nomeados - dicionário

# def exibir_poema(data_extenso, *args, **kwargs):
#     # Junta todos os argumentos posicionais em uma única string, separada por quebras de linha
#     texto = "\n".join(args)
    
#     # Cria uma string com os metadados, formatando cada chave-valor e separando por quebras de linha
#     meta_dados = "\n".join(
#         [f"{chave.title()}: {valor}" 
#          for chave, 
#          valor in 
#          kwargs.items()])
    
#     # Formata a mensagem final com a data, o texto do poema e os metadados
#     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
#     # Exibe a mensagem formatada
#     print(mensagem)
    
# # Chama a função exibir_poema com a data, versos do poema e metadados do autor e título
# exibir_poema("São Paulo, 10 de janeiro de 2022", "Verso 1", "Verso 2", "Verso 3", autor="Carlos Drummond de Andrade", titulo="Poema de Amor")

# Parâmetros posicionais são passados como argumentos posicionais
# Parâmetros nomeados são passados como argumentos nomeados

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        posicional ou keyword   |
#         |                                - keyword-only
#          -- posicional-only

# def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#     print(f"Carro criado com sucesso! {marca, modelo, ano, placa, motor, combustivel}")
    
# criar_carro("Civic", 2020, "ABC1234", marca="Honda", motor="2.0", combustivel="Flex") 
# criar_carro(modelo="Palio", ano=2019, placa="tgk1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Objetos de primeira classe
# Funções são objetos de primeira classe em Python
# Isso significa que funções podem ser passadas como argumentos para outras funções
# E podem ser atribuídas a variáveis

# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "Divisão por zero!"
#     return a / b

# def exibir_resultado(funcao, a, b):
#     resultado = funcao(a, b)
#     print(f"Resultado da operação: {resultado}")

# exibir_resultado(somar, 10, 20)
# exibir_resultado(subtrair, 10, 20)
# exibir_resultado(multiplicar, 10, 20)
# exibir_resultado(dividir, 10, 20)

salario = 1000

def aumentar_salario():
    global salario
    salario += 500
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista auxiliar: {lista_aux}")
    

lista = [1]

print(f"Salário antes do aumento: {salario}")
print("Aumentando salário...")
aumentar_salario()
print(f"Salário após o aumento: {salario}")

print(lista)