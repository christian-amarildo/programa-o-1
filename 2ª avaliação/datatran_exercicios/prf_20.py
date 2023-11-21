# 1- Quais os valores distintos existente na coluna fase dia?

# 2- Qual a frequência de acidentes por fase do dia?

# 3- Qual a frequência de acidentes por UF?

# 4- Quantas mortes houveram no estado do Pará?

# 5- Qual as três UF com maior número de acidentes em rodovia de mão dupla?

# 6- Qual a quantidade de acidentes em que o número de feridos é maior que o número de ilesos?

# 7- Salve em um arquivo csv todos os acidentes que ocorreram na região norte.

# 8- Qual a quantidade de registros que possui algum dado nulo?

# 9- Qual a coluna com maior quantidade de dados nulo?

# 10- Em qual UF ou quais UF, ocorre o acidente com o maior número de feridos?

# 11- Qual a quantidade média de mortos, feridos e ilesos por UF?

# 12- Excluindo MG, qual a UF em aconteceu o maior número de acidentes em rodovia simples?

# 13- Formate a coluna data_inversa para o padrão dia mês e ano e salve os registros dos acidentes em
# um arquivo csv.

# 14- Qual a frequência de acidentes por dia da semana?

# 15- Qual a distribuição da frequência acumulada de feridos para todos os acidentes?

# 16- Salve em um arquivo csv os 5 primeiros acidentes que ocorreram em SP e no RJ.

# 17- Para cada UF, qual a frequência de acidentes por condição metereológica?

# 18- Por tipo de pista, qual a frequência de acidentes por fase do dia?

# 19- Considerando as UF da região sul, qual a quantidade de ilesos, feridos e mortos, por tipo de
# pista?

# 20- Salve em um arquivo csv a quantidade de mortos por UF.


def ler_datatran2020():
    """
    Função para ler um arquivo CSV ('datatran2020.csv') e organizar os dados em um dicionário.

    Retorna:
    Um dicionário onde as chaves são os nomes das colunas e os valores são listas com os dados correspondentes.
    """
    with open('./av 2/datatran2020.csv', 'r', encoding='utf-8') as f:
        # Lê o arquivo CSV e cria uma lista de listas, onde cada lista representa uma linha do CSV.
        data = [linha.split(',') for linha in f]

        # A primeira linha contém os nomes das colunas.
        colunas = data[0]

        # Inicializa um dicionário para armazenar os dados.
        bd = dict()

        # Itera sobre as colunas e adiciona uma lista vazia correspondente a cada coluna no dicionário.
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in data]

    return bd

def colunas():
    with open('./av 2/datatran2020.csv', 'r', encoding='utf-8') as f:
        data = [linha.split(',') for linha in f]
        # Imprime os nomes das colunas em linhas separadas.
        print(*data[0], sep='\n')

def questao_1():
    """
    Questão 1: Imprime os valores únicos na coluna 'fase_dia'.
    """
    base = ler_datatran2020()
    lista = base['fase_dia']
    valores = set(lista)
    print(valores)

# Chama as funções para resolver as questões 1 e 2.
questao_1()

def questao_2():
    """
    Questão 2: Conta a frequência de cada valor na coluna 'fase_dia' e imprime os resultados.
    """
    # Obtém o dicionário com os dados do CSV.
    base = ler_datatran2020()

    # Obtém a lista de valores da coluna 'fase_dia'.
    lista = base['fase_dia']

    # Cria um conjunto (set) de chaves únicas presentes na lista.
    chaves = set(lista)

    # Inicializa um dicionário para armazenar a contagem de cada valor.
    bd = dict()

    # Itera sobre as chaves (valores únicos) e inicializa a contagem como zero.
    for ch in chaves:
        bd[ch] = 0

        # Itera sobre a lista original.
        for item in lista:
            # Se o valor na lista é igual à chave, incrementa a contagem.
            if item == ch:
                bd[ch] += 1

# Chama a função para resolver a Questão 2.
questao_2()


def questao_3():
    """
    Calcula a frequência de acidentes por UF e imprime os resultados.
    """
    # Obtém o dicionário com os dados do CSV.
    base = ler_datatran2020()

    # Obtém a lista de UFs da coluna 'uf'.
    lista_uf = base['uf']

    # Inicializa um dicionário para armazenar a contagem de acidentes por UF.
    frequencia_uf = dict()

    # Itera sobre a lista de UFs.
    for uf in lista_uf:
        # Se a UF já estiver no dicionário, incrementa a contagem.
        if uf in frequencia_uf:
            frequencia_uf[uf] += 1
        # Se a UF não estiver no dicionário, adiciona com contagem 1.
        else:
            frequencia_uf[uf] = 1

    # Imprime os resultados.
    print("Frequência de Acidentes por UF:")
    for uf, frequencia in frequencia_uf.items():
        print(f"{uf}: {frequencia} acidentes")
    return 
# Chama a função para calcular a frequência de acidentes por UF.
questao_3()


# Chama a função para imprimir os nomes das colunas.
colunas()
print()


# Chama a função para executar o código.
base = ler_datatran2020()
for chave in base:
    # Imprime as três primeiras linhas de cada coluna.
    print(base[chave][:3])
