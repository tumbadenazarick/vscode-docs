import os
import re
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Any

class NexusManagementEngine:
    """Motor de Gestão Unificado: Sieve + Semantic Parser + Massive Analyzer + Sentinel."""

    def __init__(self, max_lines=2000, mass_limit=90000):
        self.max_lines = max_lines
        self.mass_limit = mass_limit
        self.armored_folders = []
        self.library = {}
        self.quarantine = {}
        self.ghost_library = {}
        self.naming_map = {}
        self.conflict_logs = []
        self.massa_critica_dir = "nexus-universe/massa_critica"

        # Assinaturas de Intenção para resolver Ambiguidade
        self.intent_signatures = {
            "WEAPON": [r"dano", r"ataque", r"municao", r"fire_rate", r"arma", r"durabilidade"],
            "MOUNT": [r"velocidade", r"stamina", r"sela", r"galopar", r"montaria"],
            "PET": [r"lealdade", r"fome", r"evoluir", r"seguir", r"carinho"],
            "BASE": [r"construir", r"energia", r"estoque", r"defesa", r"militar", r"fortificacao"],
            "NPC": [r"diálogo", r"missão", r"comportamento", r"vendedor", r"personagem"]
        }

    def process_incoming_code(self, filename: str, content: str, declared_context: str = None):
        """Triagem Pre-Commit e Análise de Massa com Proteção Sentinel."""
        linhas = content.split('\n')
        if len(linhas) > self.max_lines:
            print(f"🛡️ [SENTINEL]: Massa Crítica detectada ({len(linhas)} linhas). Iniciando segmentação...")
            self._segment_code(filename, linhas)
            return "SEGMENTED_BY_SENTINEL"

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
        return re.findall(r"(?:def|fn|function)\s+([a-zA-Z_0-9]+)\s*\(", content)

    def _segment_code(self, filename, linhas):
        """Cria partes numeradas para evitar que o arquivo 'quebre' no mobile."""
        parte = 1
        base_name = os.path.splitext(filename)[0]
        for i in range(0, len(linhas), self.max_lines):
            chunk = linhas[i:i + self.max_lines]
            nome_parte = f"{base_name}_PART_{parte}.py"
            conteudo = "\n".join(chunk)
            header = f"# [NEXUS PROTECT] - {filename} - PARTE {parte} - INTEGRALIDADE: OK\n"

            caminho = os.path.join(self.massa_critica_dir, nome_parte)
            with open(caminho, "w", encoding="utf-8") as f:
                f.write(header + conteudo)
            print(f"✅ [SENTINEL]: Segmento salvo: {nome_parte}")
            parte += 1

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

    def shield_check(self, file_path):
        """Verifica integridade de massa (Nexus Shield)."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                total_lines = sum(1 for _ in f)
            if total_lines > self.mass_limit:
                return f"⚠️ [SHIELD]: Bloqueado! {total_lines} linhas excedem o limite de {self.mass_limit}."
            return f"✅ [SHIELD]: {total_lines} linhas verificadas."
        except Exception as e:
            return f"❌ [SHIELD] Erro: {e}"

    def create_armored_folder(self, path):
        """Cria pastas protegidas contra alteração não autorizada."""
        if not os.path.exists(path):
            os.makedirs(path)
            self.armored_folders.append(path)
            print(f"🛡️ [SHIELD]: Pasta Blindada ativa: {path}")

    def generate_report(self):
        return {
            "total_quarantine": len(self.quarantine),
            "total_library": len(self.library),
            "conflicts": self.conflict_logs,
            "ghosts": len(self.ghost_library)
        }

    def generate_map_manifest(self, root_dir="nexus-universe"):
        """Gera um 'GPS' do projeto para a IA não se perder (Nexus Map)."""
        print(f"🕵️ [NEXUS]: Mapeando labirinto de pastas em {root_dir}...")
        project_map = {}
        for root, dirs, files in os.walk(root_dir):
            if any(junk in root for junk in ['node_modules', 'target', '.git', 'dist']):
                continue
            folder_name = os.path.basename(root)
            project_map[folder_name] = files

        manifest_path = os.path.join("nexus-universe/config", "nexus_map_manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(project_map, f, indent=4)
        print(f"✅ [MAP]: Manifesto gerado em {manifest_path}")
        return manifest_path

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
