import tkinter as tk

# Variáveis globais
largura = 800
altura = 600
raio = 20
x = largura // 2
y = altura // 2
velocidade_x = 0
velocidade_y = 0
forca_aplicada = 5.0  # Aumenta a força aplicada
massa = 2.0  # Massa padrão inicial
gravidade = 9.8  # Gravidade padrão inicial

# Função para atualizar a posição do objeto
def atualizar():
    global x, y, velocidade_x, velocidade_y
    forca_gravidade = massa * gravidade  # F = m * g
    # Aplicando a força gravitacional
    velocidade_y += forca_gravidade / massa * 0.1  # Aplica a gravidade (ajustado para um valor mais manejável)
    x += velocidade_x
    y += velocidade_y

    # Lógica de colisão com as bordas
    if x < raio or x > largura - raio:
        x = max(raio, min(largura - raio, x))
        velocidade_x = -velocidade_x * 0.8

    if y < raio:
        y = raio  # Impede que o objeto saia da tela pelo topo
        velocidade_y = 0  # Para a velocidade vertical quando atinge o topo

    if y > altura - raio:
        y = altura - raio
        velocidade_y = -velocidade_y * 0.8  # Inverte a direção e reduz a velocidade

    canvas.delete("all")  # Limpa o canvas
    # Desenha o objeto com contorno e cor vibrante
    canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill='cyan', outline='blue', width=3)
    
    # Atualiza a força gravitacional na interface
    forca_gravidade_label.config(text=f'Força Gravitacional: {forca_gravidade:.1f} N')
    
    janela.after(20, atualizar)  # Atualiza a posição a cada 20 milissegundos

# Função para pressionar teclas
def pressionar_tecla(evento):
    global velocidade_x, velocidade_y
    if evento.keysym == 'Left':
        velocidade_x -= forca_aplicada
    elif evento.keysym == 'Right':
        velocidade_x += forca_aplicada
    elif evento.keysym == 'Up':
        velocidade_y -= forca_aplicada  # Aumenta a velocidade para cima
    elif evento.keysym == 'Down':
        velocidade_y += forca_aplicada  # Aumenta a velocidade para baixo

# Função para ajustar a gravidade
def ajustar_gravidade():
    global gravidade
    try:
        gravidade = float(entry_gravidade.get())  # Atualiza a gravidade com o valor do usuário
    except ValueError:
        gravidade_label.config(text='Valor inválido para gravidade!')

# Função para ajustar a massa
def ajustar_massa():
    global massa
    try:
        massa = float(entry_massa.get())  # Atualiza a massa com o valor do usuário
    except ValueError:
        massa_label.config(text='Valor inválido para massa!')

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação de Movimento")

# Criando o canvas
canvas = tk.Canvas(janela, width=largura, height=altura, bg='black')
canvas.pack()

# Caixas de entrada para gravidade e massa
frame_controles = tk.Frame(janela)
frame_controles.pack()

# Entrada para gravidade
gravidade_label = tk.Label(frame_controles, text='Gravidade (m/s²):')
gravidade_label.pack(side='left')
entry_gravidade = tk.Entry(frame_controles)
entry_gravidade.insert(0, str(gravidade))  # Valor inicial
entry_gravidade.pack(side='left')

# Botão para definir gravidade
botao_gravidade = tk.Button(frame_controles, text='Definir Gravidade', command=ajustar_gravidade)
botao_gravidade.pack(side='left')

# Entrada para massa
massa_label = tk.Label(frame_controles, text='Massa (kg):')
massa_label.pack(side='left')
entry_massa = tk.Entry(frame_controles)
entry_massa.insert(0, str(massa))  # Valor inicial
entry_massa.pack(side='left')

# Botão para definir massa
botao_massa = tk.Button(frame_controles, text='Definir Massa', command=ajustar_massa)
botao_massa.pack(side='left')

# Rótulo para exibir a força gravitacional
forca_gravidade_label = tk.Label(janela, text='', font=('Arial', 12))
forca_gravidade_label.pack()

# Botão para reiniciar a simulação
botao_reiniciar = tk.Button(janela, text='Reiniciar', command=lambda: (resetar_simulacao(), atualizar()))
botao_reiniciar.pack()

# Função para reiniciar a simulação
def resetar_simulacao():
    global x, y, velocidade_x, velocidade_y
    x = largura // 2
    y = altura // 2
    velocidade_x = 0
    velocidade_y = 0

# Bind de teclas
janela.bind('<KeyPress>', pressionar_tecla)

# Inicia a atualização da simulação
atualizar()

# Inicia o loop da interface gráfica
janela.mainloop()
