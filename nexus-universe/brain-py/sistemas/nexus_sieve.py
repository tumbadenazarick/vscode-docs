import os
import json
from datetime import datetime

class NexusSieve:
    def __init__(self):
        self.biblioteca_fantasmas = {}
        self.mapa_de_identidade = {
            "MILITAR": {},
            "ECONOMIA": {},
            "ENTIDADES": {"NPC": {}, "PLAYER": {}, "PET": {}, "MOUNT": {}},
            "TECNOLOGIA": {}
        }
        self.logs_de_conflito = []

    def triagem_pre_commit(self, nome, codigo, contexto):
        for ctx, modelos in self.mapa_de_identidade.items():
            if isinstance(modelos, dict) and nome in modelos and ctx != contexto:
                self.logs_de_conflito.append(f"⚠️ CONFLITO: '{nome}' detectado em {ctx} e {contexto}.")

        registro = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hash_versao": hash(codigo),
            "status": "QUARENTENA",
            "corpo": codigo
        }

        if contexto in self.mapa_de_identidade:
            if isinstance(self.mapa_de_identidade[contexto], dict):
                self.mapa_de_identidade[contexto][nome] = registro
        else:
            self.biblioteca_fantasmas[nome] = registro

    def gerar_resumo_analise(self):
        print("📊 RELATÓRIO DE PRÉ-ANÁLISE (SISTEMA NEXUS)")
        print(f"Total de Conflitos de Nome: {len(self.logs_de_conflito)}")
        for log in self.logs_de_conflito:
            print(log)
        print("-" * 50)
