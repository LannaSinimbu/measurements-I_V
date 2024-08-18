import tkinter as tk
from tkinter import filedialog, messagebox
from graficos import plotar_grafico, limpar_grafico, exportar_dados

def adicionar_botoes(frame_botoes, ax, canvas):
    # Criando frames para listas de arquivos
    frame_listas = tk.Frame(frame_botoes)
    frame_listas.pack(side=tk.TOP, pady=10)

    # Criando a lista de arquivos disponíveis
    lista_disponiveis = tk.Listbox(frame_listas, selectmode=tk.MULTIPLE, width=50, height=10)
    lista_disponiveis.pack(side=tk.LEFT, padx=5)

    # Criando botões de mover arquivos
    frame_botoes_lista = tk.Frame(frame_listas)
    frame_botoes_lista.pack(side=tk.LEFT, padx=10)

    botao_mover_para_selecionados = tk.Button(frame_botoes_lista, text=">>", command=lambda: mover_para_selecionados(lista_disponiveis, lista_selecionados))
    botao_mover_para_selecionados.pack(pady=5)

    botao_remover_selecionados = tk.Button(frame_botoes_lista, text="<<", command=lambda: remover_selecionados_selecionados(lista_selecionados))
    botao_remover_selecionados.pack(pady=5)

    # Criando a lista de arquivos selecionados
    lista_selecionados = tk.Listbox(frame_listas, selectmode=tk.MULTIPLE, width=50, height=10)
    lista_selecionados.pack(side=tk.RIGHT, padx=5)

    # Variável para armazenar os dados do gráfico
    dados_grafico = {}

    # Criando botões para as ações principais
    botao_escolher_arquivos = tk.Button(frame_botoes, text="Escolher Arquivos", command=lambda: escolher_arquivos(lista_disponiveis))
    botao_escolher_arquivos.pack(side=tk.LEFT, padx=5)

    botao_plotar = tk.Button(frame_botoes, text="Plotar Gráfico", command=lambda: plotar_grafico(lista_selecionados, ax, canvas, dados_grafico))
    botao_plotar.pack(side=tk.LEFT, padx=5)

    botao_limpar = tk.Button(frame_botoes, text="Limpar Gráfico", command=lambda: limpar_grafico(ax, canvas))
    botao_limpar.pack(side=tk.LEFT, padx=5)

    botao_exportar = tk.Button(frame_botoes, text="Exportar Dados", command=lambda: exportar_dados(dados_grafico))
    botao_exportar.pack(side=tk.LEFT, padx=5)

    return lista_disponiveis, lista_selecionados

def escolher_arquivos(lista_disponiveis):
    arquivos = filedialog.askopenfilenames(title="Escolher arquivos")
    if arquivos:
        lista_disponiveis.delete(0, tk.END)  # Limpa a lista antes de adicionar novos arquivos
        for arquivo in arquivos:
            lista_disponiveis.insert(tk.END, arquivo)

def mover_para_selecionados(lista_disponiveis, lista_selecionados):
    arquivos_selecionados = lista_disponiveis.curselection()
    for i in arquivos_selecionados:
        arquivo = lista_disponiveis.get(i)
        lista_selecionados.insert(tk.END, arquivo)
    remover_selecionados_disponiveis(lista_disponiveis)

def remover_selecionados_disponiveis(lista_disponiveis):
    for i in reversed(lista_disponiveis.curselection()):
        lista_disponiveis.delete(i)

def remover_selecionados_selecionados(lista_selecionados):
    for i in reversed(lista_selecionados.curselection()):
        lista_selecionados.delete(i)
