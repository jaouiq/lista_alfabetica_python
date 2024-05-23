# lista
nomes = ['Alex', 'Simone', 'Bernardo', 'César', 'Alexandra.']

# exibe a lista na tela
print(nomes)

# exibe os valores da lista individualmente
print(nomes [0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])

# exibe os valores da lista de forma organizada
for nome in nomes:
    print(nome)

# exibe os valores da lista de forma organizada (escolhendo quantos valores serão exibidos (ex.: [0,1,2,3,4,5]) ou todos (len)) com um contador ao lado
for i in range(len(nomes)):
    print(f'{i + 1} nome da lista: {nomes[i]}.')

# ordena a lista em ordem alfabética
nomes.sort()

# exibe a lista em ordem alfabética
for nome in nomes:
    print(nome)

# ordena a lista em ordem contrária
nomes.sort(reverse=True)

# exibe a lista em ordem contrária
for nome in nomes:
    print(nome)