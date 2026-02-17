pub mod economy;
pub mod military;
pub mod social;
pub mod sandbox;
pub mod fragmenter;

pub use economy::*;
pub use military::*;
pub use social::*;
pub use sandbox::*;
pub use fragmenter::*;

use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AbyssMirror {
    pub instability_level: f32,
}

impl AbyssMirror {
    pub fn new() -> Self {
        Self { instability_level: 0.1 }
    }

    // OPOSTO DO MILITAR: Rebelião Interna
    pub fn trigger_rebellion(&self, unit_id: u32) {
        log::warn!("🔥 [ABYSS]: Unidade {} se rebelou contra o comando!", unit_id);
    }

    // OPOSTO DA ECONOMIA: Dreno de Recursos
    pub fn drain_resources(&self, amount: f64) -> f64 {
        log::error!("📉 [ABYSS]: Drenando {:.2} créditos para o mercado negro.", amount);
        amount
    }

    // OPOSTO DA IA: Corrupção Narrativa
    pub fn corrupt_dialogue(&self, original: &str) -> String {
        format!("[DADO CORROMPIDO]: {}... O Abismo sussurra traição.", original)
    }
}
