use serde::{Serialize, Deserialize};
use rand::Rng;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BetrayalSystem {
    pub instability: f32,
}

impl BetrayalSystem {
    pub fn check_betrayal(&self, unit_loyalty: f32) -> bool {
        let mut rng = rand::thread_rng();
        let chance = (1.0 - unit_loyalty) * self.instability;
        rng.gen::<f32>() < chance
    }

    pub fn trigger_friendly_fire(&self) -> f32 {
        // Dano causado por confusão ou traição
        let mut rng = rand::thread_rng();
        rng.gen_range(10.0..50.0)
    }
}
