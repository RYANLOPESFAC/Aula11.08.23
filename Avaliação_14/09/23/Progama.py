import tkinter as tk
from tkinter import messagebox

def enviar_mensagem():
    nome = str (arroz_nome.get())
    mensagem = str (enviar_mensagem.get()) 
    if nome and mensagem:
        nova_janela = tk.Toplevel(root)
        nova_janela.title("Mensagem Enviada")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

root = tk.Tk()
root.title("Envio de Mensagem")  

label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
arroz_nome = tk.Entry(root)
arroz_nome.pack()


botao_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

root.mainloop()
# Ryan alves de oliveira lopes tentei bunquei infomações na internet 