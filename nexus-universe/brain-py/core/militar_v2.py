class BaseMilitar:
    def __init__(self, nome, nivel_tech, sistema_economico):
        self.nome = nome
        self.nivel_tech = nivel_tech
        self.economia = sistema_economico # Integração direta
        self.tropas = []

    def adicionar_tropa(self, unidade):
        self.tropas.append(unidade)
        # O custo operacional aumenta conforme o exército cresce
        self.economia.custo_manutencao += (unidade.forca_belica * 0.1)

    def status_geral(self):
        print(f"--- Relatório de {self.nome} ---")
        for t in self.tropas:
            print(t.relatorio_status())
        print(f"Saldo Restante: {self.economia.saldo}")
