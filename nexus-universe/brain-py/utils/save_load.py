import json
import zlib
import os
from datetime import datetime

class SaveSystem:
    def __init__(self, save_dir: str = "saves"):
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    def salvar(self, nome_save: str, dados: dict) -> bool:
        try:
            save_data = {
                "dados": dados,
                "meta": {"data": datetime.now().isoformat(), "ver": "3.0"}
            }
            # Use JSON instead of Pickle for security as per Analysis
            conteudo = json.dumps(save_data)
            comprimido = zlib.compress(conteudo.encode())
            with open(os.path.join(self.save_dir, f"{nome_save}.galaxia"), "wb") as f:
                f.write(comprimido)
            return True
        except Exception:
            return False
