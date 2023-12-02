# Inicializa as listas de remédios vazias
antibioticos = ['Antibiótico 1', 'Antibiótico 2', 'Antibiótico 3']
analgesicos = ['Analgésico 1', 'Analgésico 2', 'Analgésico 3']
antiinflamatorios = ['Anti-inflamatório 1', 'Anti-inflamatório 2', 'Anti-inflamatório 3']

# Inicializa a lista de remédios na sacola
sacola = []

# Loop principal para adicionar remédios à sacola
while True:
    print("\nEscolha o tipo de remédio:")
    print("1. Antibióticos")
    print("2. Analgésicos")
    print("3. Anti-inflamatórios")
    print("4. Encerrar")

    opcao_tipo = input("Digite o número correspondente ao tipo de remédio desejado: ")

    if opcao_tipo == '4':
        # Mostra a lista de remédios na sacola
        print("\nLista de remédios na sacola:")
        for item in sacola:
            print(item)

        # Escolhe o local de retirada
        print("\nEscolha o local para retirada:")
        print("1. Unidade da Zona Sul")
        print("2. Unidade da Zona Norte")
        print("3. Unidade da Zona Leste")
        print("4. Unidade da Zona Oeste")
        print("5. Unidade do Centro")

        opcao_local = input("Digite o número correspondente ao local desejado: ")

        if opcao_local == '1':
            print("\nVocê escolheu retirar os remédios na Unidade da Zona Sul.")
        elif opcao_local == '2':
            print("\nVocê escolheu retirar os remédios na Unidade da Zona Norte.")
        elif opcao_local == '3':
            print("\nVocê escolheu retirar os remédios na Unidade da Zona Leste.")
        elif opcao_local == '4':
            print("\nVocê escolheu retirar os remédios na Unidade da Zona Oeste.")
        elif opcao_local == '5':
            print("\nVocê escolheu retirar os remédios na Unidade do Centro.")
        else:
            print("\nOpção inválida. Tente novamente.")

        break

    tipo_remedio = None
    if opcao_tipo == '1':
        tipo_remedio = antibioticos
    elif opcao_tipo == '2':
        tipo_remedio = analgesicos
    elif opcao_tipo == '3':
        tipo_remedio = antiinflamatorios
    else:
        print("\nOpção inválida. Tente novamente.")
        continue

    print(f"\nEscolha o remédio {', '.join(tipo_remedio)}:")
    opcao_remedio = input("Digite o número correspondente ao remédio desejado: ")

    if opcao_remedio.isdigit() and 1 <= int(opcao_remedio) <= 3:
        remedio_escolhido = tipo_remedio[int(opcao_remedio) - 1]
        sacola.append(remedio_escolhido)
        print(f"O remédio {remedio_escolhido} foi adicionado à sacola.")
    else:
        print("\nOpção inválida. Tente novamente.")
