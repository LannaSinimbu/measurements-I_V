# measurements-I_V

Aplicativo com interface gráfica (GUI) para visualização de curvas **I–V** (corrente _vs._ tensão) a partir de arquivos de medição. O programa permite selecionar múltiplos arquivos, plotar a **densidade de corrente** (A/cm²) em função da tensão, comparar várias medições no mesmo gráfico e exportar os dados processados para CSV.

Desenvolvido em Python com `tkinter` (interface) e `matplotlib` (gráficos), o projeto é útil para análise de medidas elétricas — por exemplo, caracterização de dispositivos como células solares, diodos ou junções semicondutoras.

---

## Funcionalidades

- Seleção de múltiplos arquivos de medição via janela de diálogo.
- Organização dos arquivos em duas listas: **disponíveis** e **selecionados**.
- Plotagem de várias curvas no mesmo gráfico, com legenda por nome de arquivo.
- Conversão automática da corrente para **mA** e cálculo da **densidade de corrente** (A/cm²).
- Limpeza do gráfico com um clique.
- Exportação dos dados plotados (tensão, corrente e densidade de corrente) para arquivo `.csv`.

---

## Estrutura do projeto

```
measurements-I_V/
│
├── main.py        # Ponto de entrada: cria a janela, inicializa o gráfico e monta a interface
├── tela.py        # Cria e configura a janela principal
├── botoes.py      # Cria botões, listas de arquivos e suas interações
├── graficos.py    # Funções para inicializar, plotar, limpar e exportar gráficos
└── teste.py       # Versão monolítica (tudo em um único arquivo) — útil para testes rápidos
```

| Arquivo | Responsabilidade |
|---------|------------------|
| `main.py` | Coordena tudo: cria a janela, inicializa o gráfico e adiciona os botões e listas. |
| `tela.py` | Contém a função que cria a janela principal. |
| `botoes.py` | Gera e configura os botões, as listas de arquivos e suas interações. |
| `graficos.py` | Contém as funções para inicializar, plotar, limpar e exportar gráficos. |
| `teste.py` | Versão independente que reúne toda a lógica em um único script. |

> **Observação:** o README anterior citava um arquivo `util.py`, que não existe no projeto atual. Se você pretende adicionar funções utilitárias comuns no futuro, esse seria o lugar indicado.

---

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - `matplotlib`
  - `pandas`
  - `tkinter` (geralmente já incluído na instalação padrão do Python; em algumas distribuições Linux pode ser preciso instalar à parte, por exemplo `sudo apt install python3-tk`)

### Instalação das dependências

```bash
pip install matplotlib pandas
```

---

## Como executar

A partir da raiz do projeto, execute a versão modular:

```bash
python main.py
```

Ou, para testar a versão monolítica:

```bash
python teste.py
```

---

## Formato dos arquivos de entrada

Os arquivos de medição devem ser **texto separado por espaços/tabulações**, com **duas colunas** e **sem cabeçalho**:

```
<corrente>   <tensão>
```

- **Coluna 1 — corrente** (em ampères): convertida para mA e usada no cálculo da densidade de corrente.
- **Coluna 2 — tensão** (em volts): usada como eixo X.

> A **primeira linha** de cada arquivo é descartada automaticamente (assume-se que seja uma linha de cabeçalho ou de aquecimento).

A densidade de corrente é calculada como:

```
densidade_de_corrente = corrente / AREA_CM2
```

onde `AREA_CM2` é a área do dispositivo, definida no código (valor padrão: **0,58 cm²**). Ajuste essa constante em `graficos.py` (e em `teste.py`) conforme a sua amostra.

---

## Como usar a interface

1. Clique em **"Escolher Arquivos"** e selecione os arquivos de medição.
2. Selecione os arquivos desejados na lista da esquerda e use **`>>`** para movê-los para a lista de selecionados.
3. Use **`<<`** para remover arquivos da lista de selecionados.
4. Clique em **"Plotar Gráfico"** para gerar as curvas.
5. Clique em **"Limpar Gráfico"** para apagar o gráfico atual.
6. Clique em **"Exportar Dados"** para salvar os dados plotados em um arquivo `.csv`.

---

## Possíveis melhorias futuras

- Tornar a área (`AREA_CM2`) configurável pela interface, sem editar o código.
- Permitir personalizar rótulos dos eixos, título e unidades.
- Suportar outros formatos de arquivo (CSV com vírgula, separadores variados, etc.).
- Adicionar tratamento e validação mais robustos para arquivos mal formatados.

---

## Licença

Defina aqui a licença do projeto (por exemplo, MIT). Caso ainda não tenha uma, considere adicionar um arquivo `LICENSE`.
