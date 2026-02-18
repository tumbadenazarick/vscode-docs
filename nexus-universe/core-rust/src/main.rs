use serde::{Serialize, Deserialize};
use rand::prelude::*;

#[derive(Debug, Serialize, Deserialize, Clone, PartialEq)]
pub enum ClassePersonagem {
    Monarca, Sombra, Lorde, Comandante, Guerreiro, Mago, Inexistente,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub enum StatusEffectType {
    Escudo(u128),
    Regen(i128),
    DebuffPoder(u128),
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct StatusEffect {
    pub tipo: StatusEffectType,
    pub duracao_restante: u8,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub enum EfeitoHabilidade {
    DanoDireto(u128),
    AumentoMoral(i8),
    Invocacao(u32),
    Escudo(u128),
    Debuff(i8),
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Habilidade {
    pub nome: String,
    pub efeito: EfeitoHabilidade,
    pub custo_energia: u32,
    pub cooldown: u8,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Personagem {
    pub nome: String,
    pub classe: ClassePersonagem,
    pub nivel: u32,
    pub poder_base: u128,
    pub hp_max: i128,
    pub hp_atual: i128,
    pub status_ativos: Vec<StatusEffect>,
    pub cooldowns_atual: Vec<u8>,
}

impl Personagem {
    pub fn calcular_poder_total(&self) -> u128 {
        let mut rng = thread_rng();
        let base_det = self.poder_base as f64 * (1.0 + (self.nivel as f64 * 0.1));
        let var: f64 = rng.gen_range(0.95..1.05);
        (base_det * var) as u128
    }

    pub fn aplicar_status(&mut self, tipo: StatusEffectType, duracao: u8) {
        self.status_ativos.push(StatusEffect {
            tipo,
            duracao_restante: duracao,
        });
    }

    pub fn processar_fase_manutencao(&mut self) {
        // Redução de Cooldowns
        for cd in self.cooldowns_atual.iter_mut() {
            if *cd > 0 { *cd -= 1; }
        }

        // Processamento de Status
        self.status_ativos.retain_mut(|status| {
            if let StatusEffectType::Regen(valor) = status.tipo {
                self.hp_atual = (self.hp_atual + valor).clamp(0, self.hp_max);
            }
            status.duracao_restante = status.duracao_restante.saturating_sub(1);
            status.duracao_restante > 0
        });
    }
}

pub struct UnidadeMilitar {
    pub nome: String,
    pub poder: u128,
    pub moral: i8,
}

impl UnidadeMilitar {
    pub fn calcular_forca_real(&self) -> u128 {
        let fator_moral = (self.moral.clamp(-100, 100) as f64 + 100.0) / 100.0;
        (self.poder as f64 * fator_moral) as u128
    }
}

fn main() {
    println!("--- OPERAÇÃO FRONTEIRA: ENGINE MILITAR ---");
    let mut heroi = Personagem {
        nome: "Jin-Woo".to_string(),
        classe: ClassePersonagem::Monarca,
        nivel: 10,
        poder_base: 5000,
        hp_max: 1000,
        hp_atual: 800,
        status_ativos: vec![],
        cooldowns_atual: vec![0, 2],
    };

    heroi.aplicar_status(StatusEffectType::Regen(50), 3);
    println!("HP Inicial: {}", heroi.hp_atual);
    heroi.processar_fase_manutencao();
    println!("HP após Regen: {}", heroi.hp_atual);
    println!("Força Real: {}", heroi.calcular_poder_total());
}
