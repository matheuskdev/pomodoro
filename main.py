from tkinter import *
import ttkbootstrap as ttk
from Pomodoro import PomodoroModule

class AplicativoPomodoro(PomodoroModule):
    
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.geometry("600x300")
        self.master.configure(background="white")
        self.master.resizable(width=False, height=False)
        self.master.attributes("-alpha", 0.9)

        # Inicializar a interface
        self.inicializar_interface()

    def inicializar_interface(self):
        self.inicializar_janela()
        self.inicializar_widgets()

    def inicializar_janela(self):
        self.janela = self.master
        self.janela.title("Aplicativo Pomodoro")

    def inicializar_widgets(self):
        self.inicializar_lado_esquerdo()
        self.inicializar_lado_direito()

    def inicializar_lado_esquerdo(self):
        frame_esquerdo = Frame(self.janela, width=200, height=400, bg="AZURE3", relief="raise")
        frame_esquerdo.pack(side=LEFT)

        rotulo_logo = Label(frame_esquerdo, bg="AZURE3", width=181, height=100)
        rotulo_logo.place(x=10, y=10)

        rotulo_mensagem = Label(frame_esquerdo, bg="AZURE3", text="Versão: 1.0.0\nDev: @MatheusKDev", justify='center')
        rotulo_mensagem.place(x=40, y=250)

    def inicializar_lado_direito(self):

        frame_direito = Frame(self.janela, width=397, height=400, bg="AZURE3", relief="raise")
        frame_direito.pack(side=RIGHT)

        rotulo_logo = Label(frame_direito, bg="RED", width=381, height=70)
        rotulo_logo.place(x=10, y=10)

        rotulo_mensagem = Label(frame_direito, bg="AZURE3", justify='center', 
                                text="Aplicativo Pomodoro",font=("Helvetica", 20), fg="gray")
        rotulo_mensagem.place(x=100, y=10)

        self.rotulo_temporizador = Label(frame_direito, text="25:00", font=("Helvetica", 50))
        self.rotulo_temporizador.place(x=130, y=65)

        self.botao_iniciar = ttk.Button(frame_direito, text="Iniciar", width=38, command=self.iniciar_temporizador)
        self.botao_iniciar.place(x=90, y=150)

        self.botao_parar = ttk.Button(frame_direito, text="Parar", width=38, command=self.parar_temporizador)
        self.botao_parar.place(x=90, y=250)

        self.botao_reset = ttk.Button(frame_direito, text="Reiniciar", width=38, command=self.resetar_temporizador)
        self.botao_reset.place(x=90, y=200)



if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    app = AplicativoPomodoro(root)
    root.mainloop()
