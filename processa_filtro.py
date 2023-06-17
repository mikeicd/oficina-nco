import tkinter as tk
from tkinter import filedialog


def ler_arquivo():
    """Abrir janela de seleção de arquivo
    """
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos de Texto", ["*.txt", "*.fcf"])])
    entry_arquivo_entrada.delete(0, tk.END)
    entry_arquivo_entrada.insert(tk.END, arquivo)


def copiar_numeros():
    """Encontra os números e copia para o novo arquivo
    """
    arquivo_origem = entry_arquivo_entrada.get()
    arquivo_destino = entry_arquivo_saida.get()

    with open(arquivo_origem, 'r') as arquivo_entrada:
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

        with open(arquivo_destino, 'w') as arquivo_saida:
            arquivo_saida.write(numeros_formatados)

    janela.quit()
    janela.destroy()


# Criação da janela principal
janela = tk.Tk()
janela.title("Copiar Números")
janela.geometry("400x200")

# Variáveis para armazenar os nomes dos arquivos
arquivo_entrada = tk.StringVar()
arquivo_saida = tk.StringVar()

# Label e campo de entrada para o arquivo de entrada
lbl_arquivo_entrada = tk.Label(janela, text="Arquivo de Entrada:")
lbl_arquivo_entrada.pack()

# Variável que guarda os dados do arquivo de entrada
entry_arquivo_entrada = tk.Entry(janela, textvariable=arquivo_entrada)
entry_arquivo_entrada.pack()

# Botão para selecionar o arquivo de entrada
btn_selecionar_arquivo = tk.Button(
    janela, text="Selecionar Arquivo", command=ler_arquivo)
btn_selecionar_arquivo.pack()

# Label e campo de entrada para o arquivo de saída
lbl_arquivo_saida = tk.Label(janela, text="Novo Arquivo:")
lbl_arquivo_saida.pack()

# Variável que guarda os dados do arquivo de saida
entry_arquivo_saida = tk.Entry(janela, textvariable=arquivo_saida)
entry_arquivo_saida.pack()

# Botão para copiar os números
btn_copiar_numeros = tk.Button(
    janela, text="Copiar Números", command=copiar_numeros)
btn_copiar_numeros.pack()

# Executar a interface gráfica
janela.mainloop()
