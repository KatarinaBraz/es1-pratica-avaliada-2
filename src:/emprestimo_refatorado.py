class CalculadoraMulta:
    def calcular(self, dias):
        return dias * 2


class ServicoNotificacao:
    def enviar(self, mensagem):
        print("Email enviado:", mensagem)


class GerenciadorEmprestimo:
    def __init__(self, calculadora, notificacao):
        self.calculadora = calculadora
        self.notificacao = notificacao

    def realizar_emprestimo(self):
        print("Empréstimo realizado")

    def calcular_multa(self, dias):
        multa = self.calculadora.calcular(dias)
        self.notificacao.enviar(f"Multa: {multa}")
        return multa