import json
import os
import time

class HotReloadEngine:
    """Sistema de recarga em tempo real e renomeação global."""

    def __init__(self, registry_path="nexus-universe/config/registry.json"):
        self.registry_path = registry_path
        self.last_mtime = 0
        self.config = {}

    def check_and_reload(self):
        """Verifica se o arquivo de registro mudou e recarrega."""
        if not os.path.exists(self.registry_path):
            return False

        current_mtime = os.path.getmtime(self.registry_path)
        if current_mtime > self.last_mtime:
            self.last_mtime = current_mtime
            return self.reload()
        return False

    def reload(self):
        try:
            with open(self.registry_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
            print(f"🔄 [HOT-RELOAD]: Registro de Multiverso atualizado!")
            print(f"   Nome do Jogo: {self.get_meta('name')}")
            return True
        except Exception as e:
            print(f"❌ [HOT-RELOAD] Erro: {e}")
            return False

    def get_meta(self, key):
        return self.config.get("game_metadata", {}).get(key, "Desconhecido")

    def get_display_name(self, internal_id):
        return self.config.get("entities", {}).get(internal_id, {}).get("display_name", internal_id)

if __name__ == "__main__":
    hr = HotReloadEngine()
    if hr.reload():
        print(f"Protagonista: {hr.get_display_name('PROTAGONISTA_001')}")
