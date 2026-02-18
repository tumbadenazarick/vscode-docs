import random

class NeuralLink:
    def __init__(self):
        self.log_eventos = []
        self.entities = []

    def broadcast(self, sender: str, message: str):
        event = f"[{sender}]: {message}"
        self.log_eventos.append(event)
        print(f"[BROADCAST] {event}")

    def simulate_conflict(self, economy, military):
        chance = random.random()
        if chance < 0.3:
            self.broadcast("ABYSS", "Instabilidade detectada!")
            economy.inject_entropy(0.15)
        elif chance > 0.7:
            self.broadcast("AURORA", "Ordem restaurada.")
            economy.efficiency += 0.05
