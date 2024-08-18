import tkinter as tk
from tela import criar_janela
from botoes import adicionar_botoes
from graficos import inicializar_grafico

def main():
    # Criar a janela principal
    janela = criar_janela()

    # Criar frames para organização
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(side=tk.TOP, pady=10)

    frame_grafico = tk.Frame(janela)
    frame_grafico.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Inicializar o gráfico
    fig, ax, canvas = inicializar_grafico(frame_grafico)

    # Adicionar botões e listas de arquivos
    lista_disponiveis, lista_selecionados = adicionar_botoes(frame_botoes, ax, canvas)

    # Executar a aplicação
    janela.mainloop()

if __name__ == "__main__":
    main()
