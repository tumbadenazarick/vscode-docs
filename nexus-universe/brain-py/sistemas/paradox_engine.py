import random

class ParadoxEngine:
    def __init__(self):
        self.erros_permitidos = True
        self.quarentena_ativa = []

    def isolar_fantasma(self, codigo_massa):
        assinatura = hash(codigo_massa)
        print(f"👻 [PARADOX]: Detectada função fantasma {assinatura}. Isolando em Quarentena...")
        self.quarentena_ativa.append(codigo_massa)

    def simular_conflito_social(self, npc_a, npc_b):
        caos = random.uniform(0, 1)
        if caos > 0.7:
            print(f"💢 [CONFLITO]: Erro de comunicação entre {npc_a} and {npc_b}. Traição gerada.")
            return "HOSTIL"
        return "NEUTRO"

    def hot_swap_seguro(self, nome_antigo, nome_novo):
        print(f"🔄 [REMAP]: {nome_antigo} agora é conhecido como {nome_novo}. Sombra mantida.")
        return {nome_novo: nome_antigo}
