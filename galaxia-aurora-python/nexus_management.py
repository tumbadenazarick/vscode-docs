import os
import re
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Any

class NexusManagementEngine:
    """Motor de Gestão Unificado: Sieve + Semantic Parser + Massive Analyzer."""

    def __init__(self):
        self.library = {}
        self.quarantine = {}
        self.ghost_library = {}
        self.naming_map = {}
        self.conflict_logs = []

        # Assinaturas de Intenção para resolver Ambiguidade
        self.intent_signatures = {
            "WEAPON": [r"dano", r"ataque", r"municao", r"fire_rate", r"arma", r"durabilidade"],
            "MOUNT": [r"velocidade", r"stamina", r"sela", r"galopar", r"montaria"],
            "PET": [r"lealdade", r"fome", r"evoluir", r"seguir", r"carinho"],
            "BASE": [r"construir", r"energia", r"estoque", r"defesa", r"militar", r"fortificacao"],
            "NPC": [r"diálogo", r"missão", r"comportamento", r"vendedor", r"personagem"]
        }

    def process_incoming_code(self, filename: str, content: str, declared_context: str = None):
        """Triagem Pre-Commit e Análise de Massa."""
        detected_intent = self._detect_intent(content)
        context = declared_context or detected_intent

        # Gerar Assinatura de Alma (Hash)
        version_hash = hashlib.sha256(content.encode()).hexdigest()[:12]
        unique_id = f"{context}_{filename}_{version_hash}"

        # Verificar Conflitos de Massa
        self._check_conflicts(filename, context)

        entry = {
            "id": unique_id,
            "original_name": filename,
            "intent": detected_intent,
            "context": context,
            "hash": version_hash,
            "content": content,
            "status": "QUARANTINE",
            "timestamp": datetime.now().isoformat(),
            "functions": self._extract_functions(content)
        }

        self.quarantine[unique_id] = entry
        print(f"📥 [NEXUS]: Código {filename} registrado em QUARENTENA. ID: {unique_id}")
        return unique_id

    def _detect_intent(self, content: str) -> str:
        """Resolve nomes iguais diferenciando a mecânica abstrata."""
        content_lower = content.lower()
        scores = {intent: 0 for intent in self.intent_signatures}

        for intent, patterns in self.intent_signatures.items():
            for p in patterns:
                if re.search(p, content_lower):
                    scores[intent] += 1

        best_intent = max(scores, key=scores.get)
        return best_intent if scores[best_intent] > 0 else "UNKNOWN_CONTEXT"

    def _extract_functions(self, content: str) -> List[str]:
        return re.findall(r"def\s+(\w+)\s*\(", content)

    def _check_conflicts(self, name: str, context: str):
        for uid, data in self.library.items():
            if data["original_name"] == name and data["context"] != context:
                msg = f"⚠️ CONFLITO DETECTADO: '{name}' existe em {data['context']} e {context}."
                self.conflict_logs.append(msg)
                print(msg)

    def hot_rename(self, old_name: str, new_name: str):
        """Altera nomes globalmente sem quebrar o sistema."""
        self.naming_map[old_name] = new_name
        print(f"🔄 [HOT-RENAME]: '{old_name}' agora é mapeado como '{new_name}'.")

    def generate_report(self):
        return {
            "total_quarantine": len(self.quarantine),
            "total_library": len(self.library),
            "conflicts": self.conflict_logs,
            "ghosts": len(self.ghost_library)
        }

class NexusAutopilot:
    """Sistema de automação para análise e melhoria."""
    def analyze_project(self, root_dir: str):
        print(f"🧠 [AUTOPILOT]: Analisando {root_dir}...")
        # Lógica de análise baseada no script fornecido
        return {"quality": 85, "issues": 0}

if __name__ == "__main__":
    nexus = NexusManagementEngine()

    # Teste de Ambiguidade de Ampla Escala (Mass Code)
    scenarios = [
        ("arma_laser.py", "def fogo_rapido(): self.dano = 50; self.municao -= 1"),
        ("cavalo_estelar.py", "def galopar(): self.velocidade += 10; self.stamina -= 5"),
        ("dog_robot.py", "def seguir(): self.lealdade = 100; self.fome = 0"),
        ("fortaleza.py", "def levantar_escudos(): self.defesa += 500; self.energia -= 100")
    ]

    for filename, code in scenarios:
        id_gen = nexus.process_incoming_code(filename, code)
        print(f"✅ Classificado: {filename} -> {nexus.quarantine[id_gen]['intent']}")

    print(f"\n📊 Relatório de Integridade: {nexus.generate_report()}")
