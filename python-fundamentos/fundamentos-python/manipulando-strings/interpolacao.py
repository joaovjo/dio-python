# Estilo antigo de formatação de strings utilizando %

nome = 'João'
idade = 28
profissao = 'Desenvolvedor Fullstack'
linguagem = 'Python'

# %s - String
# %d - Inteiro
# %f - Float
# %r - Boolean
# %x - Hexadecimal

print('Formatação com %')
print('Nome: %s, Idade: %d, Profissão: %s, Linguagem: %s' % (nome, idade, profissao, linguagem))
print('\n')

# Formatação de strings utilizando o método format

print('Formatação com format')
print('Nome: {}, Idade: {}, Profissão: {}, Linguagem: {}'.format(nome, idade, profissao, linguagem))
print('\n')

# Formatação passandos os índices das variáveis
print('Formatação com format e índices')
print('Nome: {0}, Idade: {1}, Profissão: {2}, Linguagem: {3}'.format(nome, idade, profissao, linguagem))
print('\n')

# Formatação passando as variáveis nomeadas
print('Formatação com format e variáveis nomeadas')
print('Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print('\n')

# Formatação passando diciónario
print('Formatação com format e dicionário')
dados = {'nome': nome, 'idade': idade, 'profissao': profissao, 'linguagem': linguagem}
print('Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}'.format(**dados))
print('\n')

# Formatação com f-string
print('Formatação com f-string')
print(f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}, Linguagem: {linguagem}')
print('\n')

# Formatação com f-string e strings
PI = 3.14159265359
print(f'Valor de PI: {PI:.2f}') # Limitando o número de casas decimais em 2
print(f'Valor de PI: {PI:.4f}') # Limitando o número de casas decimais em 4
print(f'Valor de PI: {PI:.6f}') # Limitando o número de casas decimais em 6
print(f'Valor de PI: {PI:.8f}') # Limitando o número de casas decimais em 8
print(f'Valor de PI: {PI:.10f}') # Limitando o número de casas decimais em 10
print(f'Valor de PI: {PI:10.2f}') # Limitando o número de casas decimais em 2 e adicionando 10 espaços a esquerda