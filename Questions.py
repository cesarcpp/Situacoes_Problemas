def situ_problema_1 ():
    Soma = 0
    Indice = 13
    K = 0

    # Condição que atinge o indice solicitado
    while K < Indice:
        K = K + 1
        Soma = Soma + K

    # Demonstrando o Resultado
    print(f"O Resultado deste Soma é {Soma}")

def situ_problema_2():
    # Função que localiza o número na sequência de Fibonacci
    def check_fibonacci(numero):
        # Definindo como base os dois primeiros números da sequência
        a, b = 0, 1
        while a <= numero:
            if a == numero:
                return True
            # Acrescentando os números nas variáveis A e B
            a, b = b, a + b
        return False

    # Input que permite definir o número para verificação
    numero = int(
        input("Digite o número para que você consiga verificar se o mesmo pertence a sequência de Fibonacci: "))

    # Checagem do número na sequência
    if check_fibonacci(numero):
        print(f"O número {numero} pertence a sequência de Fibonacci")
    else:
        print(f"O número {numero} não pertence a sequência de Fibonacci")

def situ_problema_3():
    #Importando a biblioteca Json
    import json

    # Função que define a leitura do arquivo Json
    def ler_dados(caminho_arquivo):
        with open(caminho_arquivo, 'r') as file:
            dados = json.load(file)
        return dados

    # Função que permite analisar o faturamento da empresa
    def analisando_faturamento(dados):
        faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
        menor = min(faturamento)
        maior = max(faturamento)
        media = sum(faturamento) / len(faturamento)
        acima_media = sum(1 for valor in faturamento if valor > media)

        return menor, maior, media, acima_media

    # Definindo o caminho do arquivo utilizado (Json)
    caminho_arquivo = 'dados.json'

    # Realizando a leitura dos dados presente no arquivo
    dados = ler_dados(caminho_arquivo)

    # Passando as análises para variáveis
    menor, maior, media, acima_media = analisando_faturamento(dados)

    # Demonstrando os resultados
    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Média de faturamento: R${media:.2f}")
    print(f"Número de dias com faturamento acima da média: {acima_media}")


def situ_problema_4 ():
    # Criando um dicionário que define o faturamento
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    # Calculando o Faturamento Total dos Estados
    Total_Faturamento = sum(faturamento.values())

    # Calculando o percentual de cada estado
    Per_Estado = {estado: (valor / Total_Faturamento) * 100 for estado, valor in faturamento.items()}

    # Demonstrando os percentuais
    for estado, percentual in Per_Estado.items():
        print(f"{estado}: {percentual:.2f}%")

def situ_problema_5 ():
    # Função que inverte o texto
    def invert_text(texto):
        invert = ""
        for letra in texto:
            invert = letra + invert
        return invert

    # Definindo a palavra que será invertida
    texto = str(input("Coloque a Palavra que será invertida: "))

    # Comando que realiza a inversão do Texto
    resultado = invert_text(texto)

    # Demonstrando o Texto Invertido
    print(f"Palavra Invertida: {resultado}")

def Menu():
    while True:
        print("Resolução dos Problemas")
        print()
        print("1 - Resolução Problema 1")
        print("2 - Resolução Problema 2")
        print("3 - Resolução Problema 3")
        print("4 - Resolução Problema 4")
        print("5 - Resolução Problema 5")
        print("6 - Sair do Programa")
        print()
        opção = int(input("Escolha a uma opção (1|2|3|4|5|6): "))

        if opção == 1:
            print()
            situ_problema_1()
            print()
        elif opção == 2:
            print()
            situ_problema_2()
            print()
        elif opção == 3:
            print()
            situ_problema_3()
            print()
        elif opção == 4:
            print()
            situ_problema_4()
            print()
        elif opção == 5:
            print()
            situ_problema_5()
            print()
        elif opção == 6:
            print("Saindo do Programa, obrigado por acessar")
            break
        else:
            print("A opção escolhida é inválida. Tente novamente")

Menu()
