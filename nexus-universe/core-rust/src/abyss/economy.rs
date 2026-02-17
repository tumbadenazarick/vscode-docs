use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CorruptionSystem {
    pub level: f32, // 0.0 a 1.0
    pub lost_credits: f64,
}

impl CorruptionSystem {
    pub fn process_cycle(&mut self, total_wealth: f64) -> f64 {
        // No Abyss, uma parte do dinheiro "some" por causa da corrupção
        let drain = total_wealth * (self.level as f64 * 0.1);
        self.lost_credits += drain;
        drain // Valor desviado
    }
}
