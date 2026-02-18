import hashlib
import time
import uuid
import ast
import random
import re
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

# ============================================================================
# NÚCLEO DE SEGURANÇA NEXUS (SENTINEL & CARDINAL)
# ============================================================================

class SistemaMestre:
    """Núcleo de Comando Nexus Universal Cardinal (N.U.C.)."""
    def __init__(self, comandante="Lord Eclipse"):
        self.id_sessao = str(uuid.uuid4())
        self.comandante = comandante
        self.nivel_autoridade = 10
        self.logs = []

    def gerar_token_autorizacao(self, acao: str) -> str:
        """Gera um token de blindagem para cada ordem militar."""
        timestamp = str(time.time())
        seed = f"{self.id_sessao}-{acao}-{timestamp}"
        token = hashlib.sha256(seed.encode()).hexdigest()[:16].upper()
        return f"NEXUS-AUTH-{token}"

    def registrar_log(self, mensagem: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entrada = f"[{timestamp}] {mensagem}"
        self.logs.append(entrada)
        print(entrada)

class SecurityGuardian:
    """Valida códigos de confirmação e integridade sistêmica."""
    @staticmethod
    def validate_command(command_code: str) -> bool:
        pattern = r"^CMD-\d{6}$"
        if re.match(pattern, command_code):
            return True
        return False

# ============================================================================
# ESPELHO INVERSOR (ABYSS MIRROR)
# ============================================================================

class EspelhoInversor(ast.NodeTransformer):
    """Inverte a lógica Aurora (Ordem) para Abyss (Caos) via AST."""
    def __init__(self):
        self.substituicoes = {
            'ataque': 'defesa',
            'invasao': 'protecao',
            'destruir': 'preservar',
            'ofensivo': 'blindado',
            'dano': 'resiliencia',
            'inimigo': 'ameaca_bloqueada'
        }

    def visit_Name(self, node):
        if node.id in self.substituicoes:
            return ast.copy_location(ast.Name(id=self.substituicoes[node.id], ctx=node.ctx), node)
        return node

    def visit_FunctionDef(self, node):
        if node.name in self.substituicoes:
            node.name = self.substituicoes[node.name]
        return self.generic_visit(node)

# ============================================================================
# ENTIDADES E PSICOLOGIA (LÓGICA DE FRICÇÃO)
# ============================================================================

class NPC:
    def __init__(self, nome: str, role: str):
        self.nome = nome
        self.role = role
        self.stress_level = 0.0
        self.moral = 100
        self.saude = 100
        self.maslow_tier = "Segurança"
        self.semantic_signature = f"SIG-{nome.upper()}-{random.randint(1000, 9999)}"

    def update_psychology(self, entropy: float):
        self.stress_level = min(1.0, self.stress_level + (entropy * 1.5))
        if self.stress_level > 0.7:
            return "INSURREIÇÃO"
        return "NOMINAL"

# ============================================================================
# BASE MILITAR E ECONOMIA UNIFICADA
# ============================================================================

class EconomySystem:
    def __init__(self, initial_gold: float = 10000.0):
        self.ouro = initial_gold
        self.eficiencia = 1.0
        self.entropia = 0.0
        self.custo_manutencao = 500.0

    def processar_ciclo(self, production_base: float):
        receita = production_base * self.eficiencia * (1 - self.entropia)
        self.ouro += (receita - self.custo_manutencao)
        return self.ouro > 0

class MilitaryBase:
    RANKS = ["Soldado", "Comandante", "General", "GodMode"]
    BEHAVIORS = {
        "Soldado": "Patrulhando Perímetro.",
        "Comandante": "Iniciando manobra de defesa.",
        "General": "A vitória é nossa única opção.",
        "GodMode": "Realidade reescrita."
    }

    def __init__(self, nome: str, rank: str, mestre: SistemaMestre):
        self.nome = nome
        self.rank = rank if rank in self.RANKS else "Soldado"
        self.mestre = mestre

    def emitir_ordem(self, comando: str, codigo: str):
        self.mestre.registrar_log(f"Setor {self.nome}: {comando}! Movimentação detectada.")
        if SecurityGuardian.validate_command(codigo):
            token = self.mestre.gerar_token_autorizacao(comando)
            frase = self.BEHAVIORS.get(self.rank, "...")
            print(f"[BEHAVIOR] {frase} (Token: {token})")
            return True
        print(f"🚫 [BEHAVIOR] Negativo! Sem código CMD válido.")
        return False

# ============================================================================
# GALAXIA AURORA: O JOGO
# ============================================================================

class GalaxiaAurora:
    def __init__(self, protagonista="Caíque"):
        self.mestre = SistemaMestre(protagonista)
        self.economia = EconomySystem()
        self.base = MilitaryBase("Nave-Mãe SUCATA", "General", self.mestre)
        self.npcs = [NPC("Basara", "Apoio Musical"), NPC("Luna", "Protetora")]
        self.turno = 1

    def executar_turno(self, ordem_militar: str, codigo: str):
        print(f"\n{'='*20} GALAXIA AURORA - TURNO {self.turno} {'='*20}")
        self.economia.processar_ciclo(1500)
        self.base.emitir_ordem(ordem_militar, codigo)

        # Simulação de instabilidade
        entropia = random.uniform(0, 0.1)
        for npc in self.npcs:
            if npc.update_psychology(entropia) == "INSURREIÇÃO":
                self.mestre.registrar_log(f"ALERTA: Insurreição de {npc.nome}!")

        self.turno += 1

if __name__ == "__main__":
    jogo = GalaxiaAurora()
    jogo.executar_turno("Patrulhar Perímetro", "CMD-123456")

    # Demonstração de Inversão AST
    codigo_original = "def ataque_inimigo(): pass"
    tree = ast.parse(codigo_original)
    transformer = EspelhoInversor()
    nova_tree = transformer.visit(tree)
    print(f"\nOriginal: {codigo_original}")
    print(f"Espelhado: {ast.unparse(nova_tree)}")
