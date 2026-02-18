import random

class SistemaEconomico:
    def __init__(self, saldo_inicial, custo_operacional):
        self.saldo = saldo_inicial
        self.impostos = 0.15
        self.custo_manutencao = custo_operacional

    def processar_ciclo(self):
        self.saldo -= self.custo_manutencao
        return self.saldo > 0

class BaseMilitar:
    def __init__(self, nome, nivel_tech):
        self.nome = nome
        self.nivel_tech = nivel_tech
        self.tropas = []
        self.alerta_maximo = False

    def emitir_ordem(self, comando):
        frases = [
            f"Setor {self.nome}: {comando}! Movimentação detectada.",
            f"Protocolo {self.nivel_tech}: Iniciando manobra de defesa.",
            f"Atenção soldados! Ordem superior: {comando}."
        ]
        return random.choice(frases)

class UnidadeMilitar:
    def __init__(self, tipo, forca_belica, saude):
        self.tipo = tipo
        self.forca_belica = forca_belica
        self.saude = saude
        self.status = "Ativo"

    def relatorio_status(self):
        if self.saude < 30:
            return f"[{self.tipo}] Crítico! Precisamos de suporte médico!"
        return f"[{self.tipo}] Operacional. Força bélica em {self.forca_belica}."

def executar_teste_jogo():
    print("--- INICIANDO ANÁLISE DE SISTEMA ---")
    banco = SistemaEconomico(saldo_inicial=5000, custo_operacional=1200)
    base_alfa = BaseMilitar("Fortaleza Maragogipe", nivel_tech="Beta-5")
    soldado_01 = UnidadeMilitar("Infantaria Pesada", forca_belica=85, saude=100)

    if banco.processar_ciclo():
        print(base_alfa.emitir_ordem("Patrulhar Perímetro"))
        print(soldado_01.relatorio_status())
    else:
        print("ERRO DE SISTEMA: Falência econômica. Base desativada.")
