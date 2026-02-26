import tkinter as tk
from tkinter import messagebox
import psutil
import time
import threading


def bloqueador():
    app = entrada_app.get()
    try:
        tempo_min = int(entrada_tempo.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tempo!")
        return

    tempo_bloqueio = tempo_min * 60
    fim = time.time() + tempo_bloqueio

    def executar_bloqueio():
        while time.time() < fim:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'].lower() == app.lower():
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            time.sleep(2)
        messagebox.showinfo("Fim!", f"O tempo de bloqueio do {app} terminou!")

    threading.Thread(target=executar_bloqueio, daemon=True).start()
    messagebox.showinfo("Iniciado", f"Bloqueio do {app} iniciado por {tempo_min} minutos!")



janela = tk.Tk()
janela.title("Bloqueador de Aplicativos")
janela.geometry("420x280")
janela.config(bg="#2c3e50")


janela.update_idletasks()
largura = 420
altura = 280
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{x}+{y}")


titulo = tk.Label(
    janela,
    text="Bloqueador de Aplicativos",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#2c3e50"
)
titulo.pack(pady=15)


tk.Label(janela, text="Nome do aplicativo:", font=("Arial", 12), fg="white", bg="#2c3e50").pack()
entrada_app = tk.Entry(janela, font=("Arial", 12), width=25, justify="center")
entrada_app.pack(pady=8)


tk.Label(janela, text="Tempo do bloqueio (minutos):", font=("Arial", 12), fg="white", bg="#2c3e50").pack()
entrada_tempo = tk.Entry(janela, font=("Arial", 12), width=10, justify="center")
entrada_tempo.pack(pady=8)


btn_bloquear = tk.Button(
    janela,
    text="Bloquear",
    command=bloqueador,
    font=("Arial", 12, "bold"),
    bg="#e74c3c",
    fg="white",
    relief="flat",
    width=15,
    height=2
)
btn_bloquear.pack(pady=20)

janela.mainloop()
