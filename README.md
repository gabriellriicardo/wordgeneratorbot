# 🌟 Gerador de Palavras Aleatórias 🌟

Este projeto é uma aplicação em Python com interface gráfica feita usando **Tkinter**. Ele gera uma lista de palavras aleatórias de diferentes idiomas (inglês, português e espanhol) com base no número de palavras e tamanho mínimo que você especificar.

## 📋 Funcionalidades

- 🔤 Geração de palavras a partir dos idiomas:
  - Inglês 🇺🇸
  - Português 🇧🇷
  - Espanhol 🇪🇸
- 📊 Barra de progresso para acompanhar a geração
- 💾 Salvamento das palavras geradas em um arquivo `.txt`
- 👀 Opção para visualizar as palavras geradas em uma janela separada
- 🔀 Execução em threads para evitar congelamento da interface

## 🚀 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/gabriellriicardo/wordgeneratorbot.git

2. Instale as dependências:
   ```bash
   pip install nltk tkinter

3. Execute o script principal:
   ```bash
   python gerador_palavras.py

4. Escolha o número de palavras, o tamanho mínimo, os idiomas e clique em Gerar. Você também pode optar por exibir as palavras geradas diretamente na interface.

🔧 Requisitos
- Python 3.x
- Bibliotecas: nltk, tkinter

🔗 Instalação das Corpora Necessárias
Este programa utiliza corpora do nltk, então você precisa baixar as corpora necessárias ao executar pela primeira vez:
   ```bash
   import nltk
   nltk.download('words')
   nltk.download('mac_morpho')
   nltk.download('cess_esp')
   ```
🎨 Interface Gráfica
A interface gráfica foi construída com Tkinter e inclui:

- Campos de Entrada: para especificar o número de palavras e tamanho mínimo.
- Checkboxes: para escolher os idiomas de geração.
- Botão de Geração: que inicia o processo e salva o arquivo com as palavras.
- Barra de Progresso: para mostrar o andamento da geração.

📂 Estrutura de Arquivos
   ```bash
   gerador-palavras/
   │
   ├── gerador_palavras.py    # Script principal
   ├── README.md              # Este arquivo!
   └── palavras.txt           # Arquivo gerado após a execução
