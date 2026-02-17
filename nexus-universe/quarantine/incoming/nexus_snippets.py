# Snippets enviados pelo Lord Eclipse - Triagem Nexus
import hashlib
from datetime import datetime

class NexusSieve:
    def __init__(self):
        self.biblioteca_fantasmas = {}
        self.mapa_de_identidade = {"MILITAR": {}, "ECONOMIA": {}, "ENTIDADES": {"NPC": {}, "PLAYER": {}, "PET": {}, "MOUNT": {}}}
        self.logs_de_conflito = []

    def triagem_pre_commit(self, nome, codigo, contexto):
        registro = {"timestamp": datetime.now().isoformat(), "hash_versao": hashlib.md5(codigo.encode()).hexdigest(), "status": "QUARENTENA", "corpo": codigo}
        if contexto in self.mapa_de_identidade: self.mapa_de_identidade[contexto][nome] = registro
        else: self.biblioteca_fantasmas[nome] = registro

class NexusSemanticParser:
    def _detectar_contexto(self, conteudo):
        keywords = {
            "ARMA": [r"dano", r"ataque", r"durabilidade", r"fire_rate"],
            "MONTARIA": [r"velocidade", r"stamina", r"sela", r"galopar"],
            "PET": [r"lealdade", r"fome", r"evoluir", r"seguir"],
            "BASE": [r"construir", r"energia", r"estoque", r"defesa_torre"]
        }
        import re
        for contexto, padroes in keywords.items():
            for p in padroes:
                if re.search(p, conteudo.lower()): return contexto
        return "GENERIC_ENTITY"

class AbyssDisruptor:
    def causar_confusao_mental(self):
        print("🌀 [ABYSS]: Invertendo lógica de funções fantasma...")
