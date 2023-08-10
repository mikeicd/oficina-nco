import argparse

def copiar_numeros(origem, destino):
    """Encontra os números e copia para o novo arquivo
    """

    with open(origem, 'r') as arquivo_entrada:
        # Ler arquivo por linhas
        conteudo = arquivo_entrada.readlines()
        encontrou_numarator = False
        numeros = []
        # Varre arquivo, se encontrar a linha 'Numerator:' começa a adicionar na lista os números
        for linha in conteudo:
            if encontrou_numarator:
                aux = linha.strip()
                if aux:
                    numeros.append(aux.strip())

            if 'Numerator:' in linha:
                encontrou_numarator = True

        numeros_formatados = ','.join(numeros)

        with open(destino, 'w') as arquivo_saida:
            arquivo_saida.write(numeros_formatados)
        
        print('Processo concluido com sucesso!')


if __name__ == '__main__':        
    parser = argparse.ArgumentParser(description='Processa filtro', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('origem', type=str, help='Arquivo fcf gerado pelo MatLab')
    parser.add_argument('destino', type=str, help='Arquivo de destino dos parâmetros do filtro')
    args = parser.parse_args()
    
    if args.origem and args.destino:
        copiar_numeros(args.origem, args.destino)
    