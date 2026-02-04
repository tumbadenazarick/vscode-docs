use serde::{Serialize, Deserialize};
use crate::social::Profession;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Person {
    pub id: String,
    pub name: String,
    pub profession: Profession,
    pub needs: MaslowHierarchy,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MaslowHierarchy {
    pub hunger: f32,
    pub safety: f32,
    pub self_actualization: f32,
}

impl Person {
    pub fn update_psychology(&mut self, dt: f64) {
        // Aumenta a fome com o tempo
        self.needs.hunger += 0.01 * dt as f32;

        // Se a fome estiver alta, a produtividade cai drasticamente
        if self.needs.hunger > 0.8 {
            log::warn!("Cidadão {} está com fome e parou de produzir!", self.name);
        }
    }
}
