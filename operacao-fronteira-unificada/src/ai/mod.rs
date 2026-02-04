mod npc;
mod behavior;

pub use npc::*;
pub use behavior::*;

use crate::prelude::*;
use std::time::Duration;

pub struct AISystem {
    pub difficulty: Difficulty,
    pub npcs: Vec<NPCMilitar>,
}

impl AISystem {
    pub fn new(difficulty: Difficulty) -> Self {
        Self {
            difficulty,
            npcs: Vec::new(),
        }
    }

    pub async fn update(&mut self, _delta: Duration, _military: &MilitarySystem) -> Result<(), Box<dyn std::error::Error>> {
        // Lógica de atualização da IA
        Ok(())
    }
}
