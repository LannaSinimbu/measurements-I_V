import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox, filedialog
import os
import tkinter as tk

AREA_CM2 = 0.58  # Área em cm^2

def inicializar_grafico(frame_grafico):
    fig, ax = plt.subplots(figsize=(12, 4))  # Define o tamanho fixo da figura em polegadas
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    return fig, ax, canvas

def plotar_grafico(lista_selecionados, ax, canvas, dados_grafico):
    arquivos = lista_selecionados.get(0, tk.END)
    dados_grafico.clear()  # Limpa os dados anteriores

    if arquivos:
        try:
            ax.clear()

            for arquivo in arquivos:
                try:
                    dados = pd.read_csv(arquivo, delim_whitespace=True, header=None)
                    dados = dados.iloc[1:]
                    dados[0] = dados[0] * 1000
                    y = dados[0]
                    x = dados[1]

                    densidade_corrente = y / AREA_CM2
                    nome_arquivo = os.path.basename(arquivo)
                    ax.plot(x, densidade_corrente, label=nome_arquivo)

                    dados_grafico[f"Voltagem ({nome_arquivo})"] = x.values
                    dados_grafico[f"Corrente (mA) ({nome_arquivo})"] = y.values
                    dados_grafico[f"Densidade de Corrente (A/cm^2) ({nome_arquivo})"] = densidade_corrente.values
                except Exception as e:
                    messagebox.showerror("Erro ao Ler Arquivo", f"Erro ao processar o arquivo {arquivo}: {e}")
                    continue

            ax.set_xlabel("Voltagem (V)", fontsize=8)
            ax.set_ylabel("Densidade de Corrente (A/cm^2)", fontsize=8)
            ax.legend(loc='upper right', prop={'size': 8})

            canvas.draw()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao plotar os gráficos: {e}")
    else:
        messagebox.showwarning("Atenção", "Nenhum arquivo foi selecionado para plotagem.")

def limpar_grafico(ax, canvas):
    ax.clear()
    canvas.draw()

def exportar_dados(dados_grafico):
    if not dados_grafico:  # Verifica se o dicionário está vazio
        messagebox.showwarning("Atenção", "Não há dados para exportar.")
        return
    
    arquivo_exportacao = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if arquivo_exportacao:
        try:
            # Convertendo o dicionário para um DataFrame e salvando
            df_export = pd.DataFrame(dados_grafico)
            df_export.to_csv(arquivo_exportacao, index=False)
            messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para {arquivo_exportacao}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar os dados: {e}")
