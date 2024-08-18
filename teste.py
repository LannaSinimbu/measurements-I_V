import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import os

# Constantes para a área e espessura
AREA_CM2 = 0.58  # Área em cm^2
ESPESSURA_MM = 0.5  # Espessura em mm (não utilizada diretamente para densidade de corrente)

def escolher_arquivos():
    arquivos = filedialog.askopenfilenames(title="Escolher arquivos")
    if arquivos:
        lista_disponiveis.delete(0, tk.END)  # Limpa a lista antes de adicionar novos arquivos
        for arquivo in arquivos:
            lista_disponiveis.insert(tk.END, arquivo)

def mover_para_selecionados():
    arquivos_selecionados = lista_disponiveis.curselection()
    for i in arquivos_selecionados:
        arquivo = lista_disponiveis.get(i)
        lista_selecionados.insert(tk.END, arquivo)
    remover_selecionados_disponiveis()

def remover_selecionados_disponiveis():
    for i in reversed(lista_disponiveis.curselection()):
        lista_disponiveis.delete(i)

def remover_selecionados_selecionados():
    for i in reversed(lista_selecionados.curselection()):
        lista_selecionados.delete(i)

def plotar_grafico():
    global dados_grafico  # Variável global para armazenar os dados plotados
    arquivos = lista_selecionados.get(0, tk.END)
    dados_grafico = pd.DataFrame()  # Inicializa um DataFrame para armazenar os dados para exportação
    
    if arquivos:
        try:
            ax.clear()  # Limpa o gráfico atual

            for arquivo in arquivos:
                try:
                    dados = pd.read_csv(arquivo, delim_whitespace=True, header=None)
                    
                    # Eliminar o primeiro valor de cada coluna
                    dados = dados.iloc[1:]
                    
                    # Converter corrente (Y) para mA
                    dados[0] = dados[0] * 1000  # Multiplica por 1000 para converter de A para mA
                    
                    y = dados[0]
                    x = dados[1]
                    
                    # Calcular a densidade de corrente (A/cm^2)
                    densidade_corrente = y / AREA_CM2
                    
                    # Extrair apenas o nome do arquivo para a legenda
                    nome_arquivo = os.path.basename(arquivo)
                    ax.plot(x, densidade_corrente, label=nome_arquivo)
                    
                    # Adiciona os dados ao DataFrame, incluindo a densidade de corrente
                    dados_grafico[f"Voltagem ({nome_arquivo})"] = x.values
                    dados_grafico[f"Corrente (mA) ({nome_arquivo})"] = y.values
                    dados_grafico[f"Densidade de Corrente (A/cm^2) ({nome_arquivo})"] = densidade_corrente.values
                except Exception as e:
                    messagebox.showerror("Erro ao Ler Arquivo", f"Erro ao processar o arquivo {arquivo}: {e}")
                    continue

            # Ajusta o tamanho da fonte das legendas dos eixos
            ax.set_xlabel("Voltagem (V)", fontsize=8)
            ax.set_ylabel("Densidade de Corrente (A/cm^2)", fontsize=8)
            
            # Configura a legenda para ficar dentro do gráfico, no canto superior direito
            ax.legend(loc='upper right', prop={'size': 8})
            
            canvas.draw()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao plotar os gráficos: {e}")
    else:
        messagebox.showwarning("Atenção", "Nenhum arquivo foi selecionado para plotagem.")

def limpar_grafico():
    ax.clear()  # Limpa o gráfico atual
    canvas.draw()

def exportar_dados():
    if dados_grafico.empty:
        messagebox.showwarning("Atenção", "Não há dados para exportar.")
        return
    
    arquivo_exportacao = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if arquivo_exportacao:
        try:
            dados_grafico.to_csv(arquivo_exportacao, index=False)
            messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para {arquivo_exportacao}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar os dados: {e}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Seleção de Arquivos para Gráfico")

# Configurando o tamanho da janela
janela.geometry("800x600")

# Criando o botão para escolha de arquivos
botao_escolher_arquivos = tk.Button(janela, text="Escolher Arquivos", command=escolher_arquivos)
botao_escolher_arquivos.pack(pady=10)

# Criando frames para organizar as listas
frame_listas = tk.Frame(janela)
frame_listas.pack(pady=10)

# Criando a lista de arquivos disponíveis
lista_disponiveis = tk.Listbox(frame_listas, selectmode=tk.MULTIPLE, width=50, height=15)
lista_disponiveis.pack(side=tk.LEFT, padx=5)

# Criando botões de mover arquivos
frame_botoes = tk.Frame(frame_listas)
frame_botoes.pack(side=tk.LEFT, padx=10)

botao_mover_para_selecionados = tk.Button(frame_botoes, text=">>", command=mover_para_selecionados)
botao_mover_para_selecionados.pack(pady=5)

botao_remover_selecionados = tk.Button(frame_botoes, text="<<", command=remover_selecionados_selecionados)
botao_remover_selecionados.pack(pady=5)

# Criando a lista de arquivos selecionados
lista_selecionados = tk.Listbox(frame_listas, selectmode=tk.MULTIPLE, width=50, height=15)
lista_selecionados.pack(side=tk.RIGHT, padx=5)

# Criando os botões para plotar e limpar o gráfico
botao_plotar = tk.Button(janela, text="Plotar Gráfico", command=plotar_grafico)
botao_plotar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar Gráfico", command=limpar_grafico)
botao_limpar.pack(pady=10)

# Criando o botão para exportar os dados do gráfico
botao_exportar = tk.Button(janela, text="Exportar Dados", command=exportar_dados)
botao_exportar.pack(pady=10)

# Criando o espaço para o gráfico com tamanho fixo
fig, ax = plt.subplots(figsize=(12, 4))  # Define o tamanho fixo da figura em polegadas
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(side=tk.TOP)

# Variável global para armazenar os dados do gráfico
dados_grafico = pd.DataFrame()

# Executando a aplicação
janela.mainloop()
