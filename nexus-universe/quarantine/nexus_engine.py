import os
import re
import hashlib
import json
from datetime import datetime

class NexusManagementEngine:
    """Motor de Gestão Unificado para Códigos de Massa e Hot-Reload."""

    def __init__(self):
        self.library = {}
        self.quarantine = {}
        self.ghost_functions = {}
        self.naming_map = {} # Antigo -> Novo
        self.intent_signatures = {
            "WEAPON": [r"dano", r"ataque", r"municao", r"fire_rate", r"arma"],
            "MOUNT": [r"velocidade", r"stamina", r"sela", r"galopar", r"montaria"],
            "PET": [r"lealdade", r"fome", r"evoluir", r"seguir", r"estimação"],
            "BASE": [r"construir", r"energia", r"estoque", r"defesa", r"militar"],
            "NPC": [r"diálogo", r"missão", r"comportamento", r"vendedor"]
        }

    def process_mass_code(self, filename, content):
        """Analisa, classifica e registra um fragmento de código."""
        intent = self._detect_intent(content)
        version_hash = hashlib.sha256(content.encode()).hexdigest()[:12]

        # ID Único baseado em Contexto + Nome + Hash
        unique_id = f"{intent}_{filename}_{version_hash}"

        entry = {
            "id": unique_id,
            "original_name": filename,
            "intent": intent,
            "content": content,
            "status": "QUARANTINE",
            "timestamp": datetime.now().isoformat()
        }

        self.quarantine[unique_id] = entry
        print(f"📥 [NEXUS]: {unique_id} registrado em QUARENTENA. (Intenção: {intent})")
        return unique_id

    def _detect_intent(self, content):
        """Resolve ambiguidade de nomes iguais via palavras-chave."""
        content_lower = content.lower()
        scores = {intent: 0 for intent in self.intent_signatures}

        for intent, patterns in self.intent_signatures.items():
            for p in patterns:
                if re.search(p, content_lower):
                    scores[intent] += 1

        best_intent = max(scores, key=scores.get)
        if scores[best_intent] == 0:
            return "UNKNOWN_CONTEXT"
        return best_intent

    def global_rename(self, old_name, new_name):
        """Renomeação protegida que evita quebras no sistema."""
        self.naming_map[old_name] = new_name
        print(f"🔄 [HOT-RENAME]: '{old_name}' mapeado para '{new_name}'.")

    def get_effective_name(self, name):
        """Retorna o nome atualizado via Registry."""
        return self.naming_map.get(name, name)

    def generate_ghost_report(self):
        """Relatório de funções que existem apenas como nome."""
        return self.ghost_functions

if __name__ == "__main__":
    engine = NexusManagementEngine()

    # Teste de Ambiguidade
    code_1 = "def atacar(alvo): self.fome -= 10; print('Mordida!')" # Intenção PET
    code_2 = "def atacar(alvo): self.municao -= 1; print('Disparo!')" # Intenção ARMA

    id1 = engine.process_mass_code("npc_logic.py", code_1)
    id2 = engine.process_mass_code("npc_logic.py", code_2)

    print("\n--- Verificação de Isolação ---")
    print(f"Código 1 ({id1}) -> Intenção: {engine.quarantine[id1]['intent']}")
    print(f"Código 2 ({id2}) -> Intenção: {engine.quarantine[id2]['intent']}")
