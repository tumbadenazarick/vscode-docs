import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.entidades import Protagonista, EntidadeJogo
from core.militar_v1 import SistemaEconomico, BaseMilitar as BaseMilitarV1, UnidadeMilitar
from core.militar_v2 import BaseMilitar as BaseMilitarV2
from sistemas.nexus_sieve import NexusSieve
from sistemas.abyss_mirror import AbyssEntropia
from sistemas.paradox_engine import ParadoxEngine

class GalaxiaAurora:
    def __init__(self, nome_protagonista="Caíque"):
        self.turno_atual = 1
        self.protagonista = Protagonista(nome=nome_protagonista)
        self.sieve = NexusSieve()
        self.abyss = AbyssEntropia()
        self.paradox = ParadoxEngine()

        # Isola as duas versões da Base Militar
        self.economia = SistemaEconomico(saldo_inicial=10000, custo_operacional=500)
        self.base_v1 = BaseMilitarV1("Fronteira Norte", "Alpha-1")
        self.base_v2 = BaseMilitarV2("Fronteira Sul", "Beta-2", self.economia)

        print(f"✅ GALAXIA AURORA v3.0 Inicializada - Protagonista: {nome_protagonista}")

    def executar_turno(self):
        print(f"\n--- TURNO {self.turno_atual} ---")
        # Teste de isolamento: Ambas as bases operam sem conflito de nome
        print(self.base_v1.emitir_ordem("Patrulhar"))
        self.base_v2.status_geral()

        self.turno_atual += 1

if __name__ == "__main__":
    jogo = GalaxiaAurora()
    jogo.executar_turno()
