import re
import hashlib
import time

class SecurityGuardian:
    @staticmethod
    def validate_command(command_code: str) -> bool:
        """Mandatory CMD-XXXXXX validation."""
        pattern = r"^CMD-\d{6}$"
        return bool(re.match(pattern, command_code))

class SentinelKernel:
    def __init__(self, commander="Lord Eclipse"):
        self.commander = commander
        self.stability_level = 100
        self.cardinal_valve_active = False

    def validate_action(self, action_id, context_data):
        # Falha -45 Check
        if self.stability_level <= -45:
            self.cardinal_valve_active = True
            print("🚨 [SENTINEL]: ESTABILIDADE EM -45. VÁLVULA CARDINAL ATIVA. BLOQUEANDO DRENO.")
            return False

        # Token creation
        token = hashlib.sha256(f"{action_id}-{time.time()}".encode()).hexdigest()[:8]
        print(f"🛡️ [SECURITY]: Ação {action_id} autorizada. Token: {token}")
        return True

    def update_stability(self, delta):
        self.stability_level += delta
        if self.stability_level < -45:
            self.stability_level = -45
