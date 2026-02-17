use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Fragmenter {
    pub corruption_rate: f32,
}

impl Fragmenter {
    pub fn corrupt_entity_link(&self, id_a: &str, id_b: &str) -> String {
        log::error!("💀 [ABYSS]: Corrompendo link entre {} e {}.", id_a, id_b);
        "ERROR_NULL_REFERENCE".to_string()
    }

    pub fn inject_economic_entropy(&self, current_efficiency: &mut f64) {
        *current_efficiency *= -1.0;
        log::warn!("📉 [ABYSS]: Entropia injetada. Eficiência econômica invertida para {}", current_efficiency);
    }
}
