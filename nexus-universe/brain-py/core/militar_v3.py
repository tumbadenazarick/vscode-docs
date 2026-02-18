import random

class MilitaryBaseV3:
    RANKS = ["Soldado", "Comandante", "General", "GodMode"]
    BEHAVIORS = {
        "Soldado": ["Sim, senhor!", "Recarregando!"],
        "Comandante": ["Avançar posição!", "Solicito reforços!"],
        "General": ["Estratégia Aurora ativa.", "Bombardeio autorizado."],
    }

    def __init__(self, name: str, rank: str = "Soldado"):
        self.name = name
        self.rank = rank if rank in self.RANKS else "Soldado"
        self.efficiency_bonus = 1.0

    def execute_order(self, order: str, validated: bool):
        if not validated:
            return False, False

        success_rate = min(1.0, 0.8 * self.efficiency_bonus)
        action_success = random.random() <= success_rate
        return True, action_success
