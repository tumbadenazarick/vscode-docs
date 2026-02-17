import re
import random

class SecurityGuardian:
    """Valida códigos de confirmação e permissões de segurança."""

    @staticmethod
    def validate_command(command_code: str) -> bool:
        """Valida se o código segue o formato CMD-XXXXXX."""
        pattern = r"^CMD-\d{6}$"
        if re.match(pattern, command_code):
            print(f"[SECURITY] Código {command_code} VALIDADO.")
            return True
        print(f"[SECURITY] Código {command_code} REJEITADO. Formato inválido.")
        return False

class MilitaryBase:
    """Gerencia patentes militares, ordens e comportamentos."""

    RANKS = ["Soldado", "Comandante", "General", "GodMode"]

    BEHAVIORS = {
        "Soldado": ["Sim, senhor!", "Aguardando ordens.", "Patrulhando o setor.", "Recarregando!"],
        "Comandante": ["Avançar posição!", "Solicito reforços!", "Código Vermelho detectado!", "Mantenham a formação!"],
        "General": ["A vitória é nossa única opção.", "Execute o protocolo Aurora.", "Preparem o bombardeio orbital.", "Retirada não é uma opção."],
    }

    def __init__(self, name: str, rank: str = "Soldado"):
        self.name = name
        if rank not in self.RANKS:
            rank = "Soldado"
        self.rank = rank
        self.efficiency_bonus = 1.0
        print(f"[MILITARY] {self.name} inicializado com a patente {self.rank}.")

    def execute_order(self, order: str, command_code: str):
        """Executa uma ordem militar se o código de segurança for válido."""
        print(f"[MILITARY] {self.name} ({self.rank}) recebeu a ordem: '{order}'")

        if SecurityGuardian.validate_command(command_code):
            phrase = random.choice(self.BEHAVIORS.get(self.rank, ["..."]))
            print(f"[BEHAVIOR] {self.name}: '{phrase}'")
            success_rate = min(1.0, 0.8 * self.efficiency_bonus)
            action_success = random.random() <= success_rate

            if action_success:
                print(f"[ACTION] Ordem '{order}' EXECUTADA com sucesso (Taxa: {success_rate:.0%}).")
            else:
                print(f"[ACTION] Ordem '{order}' FALHOU por atrito operacional (Taxa: {success_rate:.0%}).")

            return True, action_success
        else:
            print(f"[BEHAVIOR] {self.name}: 'Negativo! Sem código de confirmação válido, não posso agir.'")
            return False, False

class EconomySystem:
    """Gerencia recursos econômicos, eficiência e entropia (corrupção)."""

    def __init__(self, initial_resources: float = 1000.0):
        self.resources = initial_resources
        self.efficiency = 1.0  # 1.0 = 100%
        self.entropy = 0.0     # 0.0 = Nenhuma corrupção
        self.shield_active = False
        print(f"[ECONOMY] Sistema iniciado com {self.resources} créditos.")

    def update_cycle(self, production_base: float):
        """Atualiza a economia com base na eficiência e entropia."""
        actual_production = production_base * self.efficiency * (1 - self.entropy)
        self.resources += actual_production
        print(f"[ECONOMY] Ciclo finalizado. Produção: {actual_production:.2f}. Recursos atuais: {self.resources:.2f}")

    def inject_entropy(self, amount: float):
        """Simula a corrupção do Abyss injetando entropia."""
        if self.shield_active:
            amount *= 0.5 # Escudo reduz impacto
            print("[ECONOMY] Escudo de Aurora mitigou parte da entropia!")
        self.entropy = min(1.0, self.entropy + amount)
        print(f"[ECONOMY] AVISO: Entropia injetada! Nível atual: {self.entropy:.2%}")

class TechTree:
    """Gerencia a progressão tecnológica e desbloqueios."""

    def __init__(self):
        self.unlocked_techs = set()
        self.tech_data = {
            "IA Militar": {"cost": 500, "benefit": "Aumento de 20% na eficiência de ordens"},
            "Fusão Estelar": {"cost": 1200, "benefit": "Produção base de energia triplicada"},
            "Escudo de Aurora": {"cost": 2000, "benefit": "Proteção total contra entropia leve"},
            "Fragmentação de Abyss": {"cost": 1500, "benefit": "Injeção de 50% de entropia no inimigo"}
        }

    def research(self, tech_name: str, economy: EconomySystem, military: MilitaryBase = None):
        """Realiza pesquisa se houver recursos suficientes e aplica benefícios."""
        if tech_name in self.unlocked_techs:
            print(f"[TECH] {tech_name} já foi pesquisada.")
            return False

        if tech_name not in self.tech_data:
            print(f"[TECH] Tecnologia {tech_name} desconhecida.")
            return False

        cost = self.tech_data[tech_name]["cost"]
        if economy.resources >= cost:
            economy.resources -= cost
            self.unlocked_techs.add(tech_name)

            # Aplicação de efeitos
            if tech_name == "IA Militar" and military:
                military.efficiency_bonus += 0.2
            elif tech_name == "Fusão Estelar":
                economy.efficiency += 0.5
            elif tech_name == "Escudo de Aurora":
                economy.shield_active = True

            print(f"[TECH] Pesquisa concluída: {tech_name}. Benefício: {self.tech_data[tech_name]['benefit']}")
            return True
        else:
            print(f"[TECH] Recursos insuficientes para {tech_name}. Necessário: {cost}")
            return False

class NeuralLink:
    """Sistema de comunicação broadcast e simulação de conflito Aurora vs Abyss."""

    def __init__(self):
        self.log_eventos = []
        print("[NEURALLINK] Sistema de comunicação neural estabelecido.")

    def broadcast(self, sender: str, message: str, type: str = "INFO"):
        """Envia uma mensagem para todo o sistema."""
        event = f"[{type}] {sender}: {message}"
        self.log_eventos.append(event)
        print(f"[BROADCAST] {event}")

    def simulate_conflict(self, economy: EconomySystem, military: MilitaryBase):
        """Simula o impacto do conflito entre Ordem e Caos."""
        chance = random.random()
        if chance < 0.3:
            self.broadcast("ABYSS", "Fragmentação detectada! Injetando entropia no sistema econômico.", "CRITICAL")
            economy.inject_entropy(0.15)
        elif chance > 0.7:
            self.broadcast("AURORA", "Protocolo de Estabilização ativado. Eficiência aumentada.", "SUCCESS")
            economy.efficiency += 0.05
            economy.entropy = max(0, economy.entropy - 0.05)
        else:
            self.broadcast("NEUTRAL", "Estado sistêmico nominal.", "INFO")

if __name__ == "__main__":
    # Teste inicial da base militar
    guardian = SecurityGuardian()
    soldier = MilitaryBase("Valkyrie", "Soldado")
    commander = MilitaryBase("Leonidas", "Comandante")

    # Retorna uma tupla (seguranca_ok, acao_ok)
    sec_ok, act_ok = soldier.execute_order("Atacar flanco norte", "CMD-123456")
    commander.execute_order("Ativar Defesa Global", "INVALID-CODE")
