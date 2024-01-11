from tkinter import messagebox


class PomodoroModule:
    
    def __init__(self) -> None:
        self.tempo_restante = 1500  # 25 minutos em segundos
        self.temporizador_em_execucao = False

    def configurar_temporizador(self):
        self.janela.after(1000, self.contagem_regressiva)

    def iniciar_temporizador(self):
        self.temporizador_em_execucao = True
        self.botao_iniciar["state"] = "disabled"
        self.botao_reset["state"] = "normal"
        self.configurar_temporizador()

    def contagem_regressiva(self):
        if self.temporizador_em_execucao and self.tempo_restante > 0:
            minutos, segundos = divmod(self.tempo_restante, 60)
            tempo_str = "{:02d}:{:02d}".format(minutos, segundos)
            self.rotulo_temporizador.config(text=tempo_str)
            self.tempo_restante -= 1
            self.janela.after(1000, self.contagem_regressiva)
        elif self.temporizador_em_execucao and self.tempo_restante == 0:
            messagebox.showinfo("Pomodoro Concluído", "Pare um pouco e descanse!")
            self.resetar_temporizador()

    def resetar_temporizador(self):
        self.tempo_restante = 1500
        self.rotulo_temporizador.config(text="25:00")
        self.temporizador_em_execucao = False
        self.botao_iniciar["state"] = "normal"
        self.botao_reset["state"] = "disabled"

    def parar_temporizador(self):
        self.temporizador_em_execucao = False
        self.botao_iniciar["state"] = "normal"
        self.botao_reset["state"] = "disabled"

