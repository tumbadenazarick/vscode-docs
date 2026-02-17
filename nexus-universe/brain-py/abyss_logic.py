import random

class AbyssLogic:
    """O Lado Sombrio do Cérebro Python."""

    def __init__(self):
        self.entropy = 0.5

    def mirror_action(self, action_name):
        """Converte uma ação positiva em uma falha ou sabotagem."""
        opposites = {
            "atacar": "trair_aliado",
            "defender": "abandonar_posto",
            "curar": "envenenar",
            "construir": "sabotar_infraestrutura"
        }
        return opposites.get(action_name, "erro_desconhecido")

    def generate_chaos_dialogue(self, character_name):
        phrases = [
            f"{character_name} teve um surto psicótico e atacou o computador central!",
            f"O sistema detectou que {character_name} está enviando segredos para o inimigo.",
            f"A moral de {character_name} caiu para zero. O Abismo é sua nova casa."
        ]
        return random.choice(phrases)

if __name__ == "__main__":
    abyss = AbyssLogic()
    print(f"Ação oposta de 'atacar': {abyss.mirror_action('atacar')}")
