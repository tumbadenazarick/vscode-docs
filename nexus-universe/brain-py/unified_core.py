import random
import re
import json
import zlib
import pickle
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

# ============================================================================
# NÚCLEO DE SEGURANÇA E VALIDAÇÃO (NEXUS SENTINEL)
# ============================================================================

class SecurityGuardian:
    """Valida códigos de confirmação e integridade sistêmica."""

    @staticmethod
    def validate_command(command_code: str) -> bool:
        """Valida se o código segue o formato CMD-XXXXXX."""
        pattern = r"^CMD-\d{6}$"
        if re.match(pattern, command_code):
            print(f"✅ [SECURITY] Código {command_code} VALIDADO.")
            return True
        print(f"❌ [SECURITY] Código {command_code} REJEITADO. Formato inválido.")
        return False

# ============================================================================
# ENTIDADES E PSICOLOGIA (HIERARQUIA DE MASLOW)
# ============================================================================

class NPC:
    """Entidade com estados psicológicos e necessidades."""

    def __init__(self, nome: str, role: str):
        self.nome = nome
        self.role = role
        self.stress_level = 0.0
        self.moral = 100
        self.saude = 100
        self.maslow_tier = "Segurança" # Fisiologia -> Segurança -> Social -> Estima
        self.semantic_signature = f"SIG-{nome.upper()}-{random.randint(1000, 9999)}"

    def update_psychology(self, entropy: float):
        """Aplica a 'Lógica de Fricção'."""
        self.stress_level = min(1.0, self.stress_level + (entropy * 1.5))
        self.moral = max(0, self.moral - (entropy * 20))

        if self.stress_level > 0.7:
            print(f"⚠️ [PSYCHOLOGY] {self.nome} ({self.role}) em colapso moral!")
            return "INSURREIÇÃO"
        return "NOMINAL"

# ============================================================================
# SISTEMA ECONÔMICO E TECNOLÓGICO (AURORA ECONOMY)
# ============================================================================

class EconomySystem:
    """Gerencia recursos, eficiência e mitigação de entropia."""

    def __init__(self, initial_gold: float = 10000.0):
        self.ouro = initial_gold
        self.eficiencia = 1.0
        self.entropia = 0.0
        self.custo_manutencao = 0.0
        print(f"💰 [ECONOMY] Sistema iniciado com {self.ouro} créditos.")

    def processar_ciclo(self, base_production: float):
        """Calcula rendimento: R = B * Eficiencia * (1 - Entropia) - Manutenção."""
        rendimento = (base_production * self.eficiencia * (1 - self.entropia)) - self.custo_manutencao
        self.ouro += rendimento
        status = "ESTÁVEL" if self.ouro > 0 else "DÉBITO CRÍTICO"
        print(f"📊 [ECONOMY] Ciclo: {rendimento:+.2f} | Saldo: {self.ouro:.2f} | Status: {status}")
        return self.ouro > 0

class TechTree:
    """Árvore tecnológica e pesquisa."""

    def __init__(self):
        self.unlocked = set()
        self.tech_data = {
            "IA Militar": {"cost": 1500, "bonus": "Eficiência Bélica +20%"},
            "Escudo Aurora": {"cost": 3000, "bonus": "Redução de Entropia em 50%"},
            "Sintetizador de Ouro": {"cost": 5000, "bonus": "Produção Base +500"}
        }

    def research(self, tech_name: str, economy: EconomySystem):
        if tech_name in self.unlocked: return False
        cost = self.tech_data.get(tech_name, {}).get("cost", 999999)

        if economy.ouro >= cost:
            economy.ouro -= cost
            self.unlocked.add(tech_name)
            print(f"🚀 [TECH] Pesquisa concluída: {tech_name}!")
            return True
        print(f"❌ [TECH] Recursos insuficientes para {tech_name}.")
        return False

# ============================================================================
# BASE MILITAR E COMANDO (OPERACAO FRONTEIRA)
# ============================================================================

class MilitaryBase:
    """Gerencia patentes, ordens e força belica."""

    RANKS = {"Soldado": 1, "Comandante": 2, "General": 3, "Imperador": 5}

    BEHAVIORS = {
        "Soldado": ["A postos!", "Patrulhando.", "Recarregando."],
        "Comandante": ["Avançar!", "Solicito reforços!", "Manter posição!"],
        "General": ["Estratégia Aurora ativa.", "Bombardeio orbital autorizado."],
        "Imperador": ["O multiverso se curva à nossa vontade."]
    }

    def __init__(self, nome: str, rank: str = "Soldado"):
        self.nome = nome
        self.rank = rank if rank in self.RANKS else "Soldado"
        self.efficiency_bonus = 1.0
        self.tropas = []

    def execute_order(self, order: str, command_code: str):
        print(f"⚔️ [MILITARY] {self.nome} ({self.rank}) recebeu: '{order}'")

        if SecurityGuardian.validate_command(command_code):
            frase = random.choice(self.BEHAVIORS.get(self.rank, ["..."]))
            print(f"🗣️ [BEHAVIOR] {self.nome}: '{frase}'")

            # Cálculo de sucesso baseado em atrito
            success_rate = min(1.0, 0.8 * self.efficiency_bonus)
            success = random.random() <= success_rate

            if success:
                print(f"💥 [ACTION] Ordem executada com sucesso (Taxa: {success_rate:.0%}).")
            else:
                print(f"💨 [ACTION] Ordem falhou por atrito operacional.")
            return True, success

        print(f"🚫 [BEHAVIOR] {self.nome}: 'Sem código, sem ação.'")
        return False, False

# ============================================================================
# SISTEMA UNIFICADO (GALAXIA AURORA FINAL)
# ============================================================================

class GalaxiaAurora:
    """A síntese final de todos os sistemas."""

    def __init__(self, protagonista="Caíque"):
        self.protagonista = protagonista
        self.economia = EconomySystem()
        self.tecnologia = TechTree()
        self.base = MilitaryBase("Fortaleza Nexus", "General")
        self.npcs = [NPC("Kael", "Minerador"), NPC("Valkyrie", "Piloto")]
        self.turno = 1

    def rodar_turno(self, comando_militar, codigo):
        print(f"\n{'='*20} TURNO {self.turno} {'='*20}")

        # 1. Economia
        self.economia.processar_ciclo(1200)

        # 2. IA e Psicologia
        entropia_atual = random.uniform(0, 0.2)
        for npc in self.npcs:
            if npc.update_psychology(entropia_atual) == "INSURREIÇÃO":
                print(f"🚨 [AVISO] Crise interna com {npc.nome}!")
                self.economia.eficiencia *= 0.9

        # 3. Militar
        self.base.execute_order(comando_militar, codigo)

        self.turno += 1

# ============================================================================
# TESTE INTEGRADO
# ============================================================================

if __name__ == "__main__":
    jogo = GalaxiaAurora()
    jogo.rodar_turno("Reforçar fronteira do Abyss", "CMD-123456")
    jogo.rodar_turno("Pesquisar IA Militar", "INVALIDO")

    # Teste de Pesquisa
    jogo.tecnologia.research("IA Militar", jogo.economia)
    jogo.base.efficiency_bonus = 1.2
    jogo.rodar_turno("Ataque Final", "CMD-999000")
