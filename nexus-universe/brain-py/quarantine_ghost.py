import os
import shutil
import logging
from datetime import datetime

class GhostFunctionManager:
    """Gerencia funções abstratas que ainda não possuem corpo físico."""

    def __init__(self):
        self.ghosts = {} # Nome -> {calls: int, context: str}

    def register_ghost_call(self, name, context):
        if name not in self.ghosts:
            self.ghosts[name] = {"calls": 0, "context": context, "first_seen": datetime.now().isoformat()}
        self.ghosts[name]["calls"] += 1
        self.ghosts[name]["last_call"] = datetime.now().isoformat()
        print(f"👻 [GHOST]: Função fantasma '{name}' invocada no contexto {context}.")

    def get_priority_list(self):
        """Retorna lista de funções fantasmas mais chamadas (prioridade de dev)."""
        return sorted(self.ghosts.items(), key=lambda x: x[1]["calls"], reverse=True)

class QuarantineManager:
    """Isola códigos defeituosos ou não verificados."""

    def __init__(self, q_dir="quarantine"):
        self.q_dir = q_dir
        os.makedirs(os.path.join(q_dir, "infected"), exist_ok=True)
        os.makedirs(os.path.join(q_dir, "logs"), exist_ok=True)

    def isolate_infected(self, file_path, error_msg):
        filename = os.path.basename(file_path)
        dest = os.path.join(self.q_dir, "infected", filename)
        shutil.move(file_path, dest)

        log_file = os.path.join(self.q_dir, "logs", f"{filename}.error")
        with open(log_file, "w") as f:
            f.write(f"Timestamp: {datetime.now()}\nError: {error_msg}")

        print(f"☣️ [QUARENTENA]: Arquivo '{filename}' isolado. Verifique os logs.")

if __name__ == "__main__":
    gm = GhostFunctionManager()
    gm.register_ghost_call("sistema_de_voo", "Militar")
    gm.register_ghost_call("sistema_de_voo", "Militar")
    print(f"Prioridade: {gm.get_priority_list()}")
