import random
from datetime import datetime
from typing import Dict, List, Optional, Any

class EntidadeJogo:
    def __init__(self, nome: str, nivel_forca: int = 10, saude_max: int = 100):
        self.nome = nome
        self.nivel_forca = nivel_forca
        self.saude_max = saude_max
        self.saude = saude_max
        self.ativo = True
        self.criado_em = datetime.now()

    def receber_dano(self, dano: int) -> bool:
        self.saude -= max(0, dano)
        if self.saude <= 0:
            self.saude = 0
            self.ativo = False
            return True
        return False

    def curar(self, quantidade: int) -> None:
        self.saude = min(self.saude_max, self.saude + quantidade)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nome": self.nome,
            "nivel_forca": self.nivel_forca,
            "saude_max": self.saude_max,
            "saude": self.saude,
            "ativo": self.ativo,
            "criado_em": self.criado_em.isoformat()
        }

    @classmethod
    def carregar(cls, data: Dict[str, Any]) -> 'EntidadeJogo':
        entidade = cls(data["nome"], data["nivel_forca"], data["saude_max"])
        entidade.saude = data["saude"]
        entidade.ativo = data["ativo"]
        entidade.criado_em = datetime.fromisoformat(data["criado_em"])
        return entidade

class Protagonista(EntidadeJogo):
    def __init__(self, nome: str, nivel: int = 1, forca_base: int = 100,
                 poderes: List[str] = None, lealdade: int = 100):
        super().__init__(nome, forca_base, 200)
        self.nivel = nivel
        self.poderes = poderes or ["Comando Estratégico"]
        self.lealdade = lealdade
        self.xp = 0
        self.pontos_retribuicao = 0
        self.moral = 100
        self.pontos_romance: Dict[str, int] = {}
        self.pontos_talento = 0

    def ganhar_xp(self, xp_ganho: int) -> bool:
        self.xp += xp_ganho
        xp_necessario = self.nivel * 100
        if self.xp >= xp_necessario:
            self.nivel += 1
            self.xp -= xp_necessario
            self.nivel_forca += 10
            self.saude_max += 20
            self.saude = self.saude_max
            self.pontos_talento += 1
            return True
        return False

    def usar_intervencao_psicologica(self, alvo: EntidadeJogo, custo: int) -> bool:
        if self.pontos_retribuicao >= custo:
            self.pontos_retribuicao -= custo
            dano = self.nivel_forca * random.uniform(0.5, 1.5)
            alvo.receber_dano(int(dano))
            if hasattr(alvo, 'moral'):
                alvo.moral = max(0, alvo.moral - 20)
            return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "nivel": self.nivel,
            "poderes": self.poderes,
            "lealdade": self.lealdade,
            "xp": self.xp,
            "pontos_retribuicao": self.pontos_retribuicao,
            "moral": self.moral,
            "pontos_romance": self.pontos_romance,
            "pontos_talento": self.pontos_talento
        })
        return data

    @classmethod
    def carregar(cls, data: Dict[str, Any]) -> 'Protagonista':
        prot = cls(data["nome"], data["nivel"], data["nivel_forca"],
                   data["poderes"], data["lealdade"])
        base_data = {k: v for k, v in data.items() if k in ["saude", "ativo", "criado_em"]}
        base_entidade = EntidadeJogo.carregar(base_data)
        prot.__dict__.update(base_entidade.__dict__)
        prot.xp = data["xp"]
        prot.pontos_retribuicao = data["pontos_retribuicao"]
        prot.moral = data["moral"]
        prot.pontos_romance = data["pontos_romance"]
        prot.pontos_talento = data["pontos_talento"]
        return prot
