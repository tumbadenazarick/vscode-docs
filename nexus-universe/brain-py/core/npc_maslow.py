import random

class NPCMaslow:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.stress_level = 0.0
        self.maslow_tier = "Segurança"

    def update_psychology(self, entropy: float):
        self.stress_level = min(1.0, self.stress_level + (entropy * 1.5))
        if self.stress_level > 0.7:
            return "REBELIÃO"
        return "NOMINAL"
