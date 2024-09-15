import random
import tkinter as tk
from tkinter import messagebox, ttk
from nltk.corpus import words, mac_morpho, cess_esp
import threading

def generate_word_list(num_words, languages, min_length, progress, status_label, word_count_label):
    """Gera uma lista de palavras aleatórias reais e únicas a partir dos idiomas selecionados."""
    word_list = []
    all_words = []

    status_label.config(text="Gerando palavras...")

    if 'English' in languages:
        all_words.extend(words.words())
    if 'Portuguese (Brazil)' in languages:
        all_words.extend(mac_morpho.words())
    if 'Spanish' in languages:
        all_words.extend(cess_esp.words())

    all_words = list(set(all_words))  # Garante que todas as palavras sejam únicas

    # Filtra palavras que sejam reais, com base no tamanho mínimo
    filtered_words = [word.lower() for word in all_words if word.isalpha() and len(word) >= min_length]

    status_label.config(text="Gerando palavras...")
    total_steps = num_words
    for i in range(num_words):
        word = random.choice(filtered_words)
        if word not in word_list:
            word_list.append(word)
        progress['value'] = (i + 1) / total_steps * 100
        word_count_label.config(text=f"Palavras geradas: {i + 1}/{num_words}")
        root.update_idletasks()  # Atualiza a interface gráfica durante o loop

    return sorted(word_list)

def save_to_txt(word_list, filename):
    """Salva a lista de palavras em um arquivo TXT."""
    with open(filename, 'w') as f:
        for word in word_list:
            f.write(word + '\n')

def on_generate():
    """Função chamada ao clicar no botão de gerar."""
    try:
        num_words = int(num_words_entry.get())
        min_length = int(min_length_entry.get())
    except ValueError:
        messagebox.showwarning("Aviso", "Por favor, insira números válidos.")
        return

    filename = filename_entry.get()
    languages = []
    if english_var.get():
        languages.append('English')
    if portuguese_var.get():
        languages.append('Portuguese (Brazil)')
    if spanish_var.get():
        languages.append('Spanish')
    
    if not languages:
        messagebox.showwarning("Aviso", "Selecione pelo menos um idioma.")
        return

    progress['value'] = 0
    status_label.config(text="Iniciando processo...")
    
    # Executar a geração das palavras em uma nova thread
    threading.Thread(target=generate_and_save, args=(num_words, languages, min_length, filename)).start()

def generate_and_save(num_words, languages, min_length, filename):
    word_list = generate_word_list(num_words, languages, min_length, progress, status_label, word_count_label)
    save_to_txt(word_list, filename)
    status_label.config(text="Processo concluído!")
    
    # Exibir palavras geradas se o usuário quiser
    if display_words_var.get():
        display_words(word_list)

    messagebox.showinfo("Sucesso", f'Arquivo "{filename}" criado com sucesso!')

def display_words(word_list):
    """Exibe as palavras geradas em uma nova janela."""
    words_window = tk.Toplevel(root)
    words_window.title("Palavras Geradas")
    text_widget = tk.Text(words_window)
    text_widget.pack(expand=True, fill='both')
    for word in word_list:
        text_widget.insert('end', word + '\n')

# Interface gráfica
root = tk.Tk()
root.title("Gerador de Palavras Aleatórias")

tk.Label(root, text="Número de palavras:").grid(row=0, column=0, sticky="w")
num_words_entry = tk.Entry(root)
num_words_entry.grid(row=0, column=1)

tk.Label(root, text="Tamanho mínimo da palavra:").grid(row=1, column=0, sticky="w")
min_length_entry = tk.Entry(root)
min_length_entry.grid(row=1, column=1)
min_length_entry.insert(0, "3")

tk.Label(root, text="Nome do arquivo:").grid(row=2, column=0, sticky="w")
filename_entry = tk.Entry(root)
filename_entry.grid(row=2, column=1)
filename_entry.insert(0, "palavras.txt")

tk.Label(root, text="Escolha os idiomas:").grid(row=3, column=0, sticky="w")

english_var = tk.BooleanVar()
tk.Checkbutton(root, text="Inglês", variable=english_var).grid(row=4, column=0, sticky="w")

portuguese_var = tk.BooleanVar()
tk.Checkbutton(root, text="Português (Brasil)", variable=portuguese_var).grid(row=5, column=0, sticky="w")

spanish_var = tk.BooleanVar()
tk.Checkbutton(root, text="Espanhol", variable=spanish_var).grid(row=6, column=0, sticky="w")

display_words_var = tk.BooleanVar()
tk.Checkbutton(root, text="Exibir palavras geradas", variable=display_words_var).grid(row=7, column=0, sticky="w")

generate_button = tk.Button(root, text="Gerar", command=on_generate)
generate_button.grid(row=8, column=0, columnspan=2, pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=9, column=0, columnspan=2, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=10, column=0, columnspan=2, sticky="w")

word_count_label = tk.Label(root, text="Palavras geradas: 0/0")
word_count_label.grid(row=11, column=0, columnspan=2, sticky="w")

exit_button = tk.Button(root, text="Sair", command=root.quit)
exit_button.grid(row=12, column=0, columnspan=2, pady=10)

# Baixar corpora necessários
import nltk
nltk.download('words')
nltk.download('mac_morpho')
nltk.download('cess_esp')

root.mainloop()
