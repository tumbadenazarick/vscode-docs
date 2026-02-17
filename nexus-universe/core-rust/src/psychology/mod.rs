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
    pub stress: f32, // 0.0 (Zen) a 1.0 (Colapso)
}

impl Person {
    pub fn update_psychology(&mut self, dt: f64) {
        // Aumenta a fome com o tempo
        self.needs.hunger += 0.01 * dt as f32;

        // Estresse aumenta se a segurança for baixa ou fome alta
        if self.needs.hunger > 0.5 || self.needs.safety < 0.3 {
            self.needs.stress += 0.05 * dt as f32;
        }

        self.needs.stress = self.needs.stress.clamp(0.0, 1.0);

        // Se a fome estiver alta, a produtividade cai drasticamente
        if self.needs.hunger > 0.8 {
            log::warn!("Cidadão {} está com fome e parou de produzir!", self.name);
        }
    }

    pub fn calculate_friction_error(&self) -> bool {
        use rand::Rng;
        let mut rng = rand::thread_rng();
        // Quanto mais estresse, maior a chance de cometer um erro crítico
        rng.gen::<f32>() < (self.needs.stress * 0.2)
    }
}
