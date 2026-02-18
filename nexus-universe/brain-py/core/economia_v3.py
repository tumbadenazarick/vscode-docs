import random

class EconomySystem:
    def __init__(self, initial_resources: float = 1000.0):
        self.resources = initial_resources
        self.efficiency = 1.0
        self.entropy = 0.0
        self.shield_active = False

    def update_cycle(self, production_base: float):
        actual_production = production_base * self.efficiency * (1 - self.entropy)
        self.resources += actual_production
        return self.resources

    def inject_entropy(self, amount: float):
        if self.shield_active:
            amount *= 0.5
        self.entropy = min(1.0, self.entropy + amount)
