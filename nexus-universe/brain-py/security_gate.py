import hashlib
import time

class SecurityGate:
    """Juiz de Segurança para o Cérebro Python."""

    def __init__(self):
        self.authorized_keys = {"nexus_key_001": "HIGH", "abyss_key_001": "LOW"}
        self.call_logs = []

    def authenticate_call(self, token, caller_id):
        """Valida se a chamada da IA ou do sistema é legítima."""
        if token in self.authorized_keys:
            log_msg = f"✅ [{time.ctime()}] Acesso permitido para {caller_id} (Nível: {self.authorized_keys[token]})"
            self.call_logs.append(log_msg)
            return True
        else:
            log_msg = f"❌ [{time.ctime()}] TENTATIVA DE INVASÃO por {caller_id}!"
            print(log_msg)
            self.call_logs.append(log_msg)
            return False

    def sanitize_input(self, text):
        """Impede que comandos maliciosos entrem na narrativa."""
        forbidden_words = ["DROP TABLE", "DELETE FROM", "system(", "eval("]
        for word in forbidden_words:
            if word in text:
                print(f"⚠️ BLOQUEADO: Tentativa de injeção detectada.")
                return "[DADO CORROMPIDO]"
        return text

    def get_integrity_hash(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

if __name__ == "__main__":
    gate = SecurityGate()
    if gate.authenticate_call("nexus_key_001", "NarrativeAI"):
        print(gate.sanitize_input("Iniciando cena: eval('destruir tudo')"))
