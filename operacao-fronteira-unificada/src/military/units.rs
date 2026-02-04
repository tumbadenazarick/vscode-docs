use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use std::time::{Duration, Instant};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum UnitType {
    Infantry,
    Tank,
    Aircraft,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Unit {
    pub id: u32,
    pub unit_type: UnitType,
    pub health: f32,
    pub max_health: f32,
    pub supplies: f32,
    pub position: (f32, f32),
}

impl Unit {
    pub fn new(id: u32, unit_type: UnitType) -> Self {
        Self {
            id,
            unit_type,
            health: 100.0,
            max_health: 100.0,
            supplies: 100.0,
            position: (0.0, 0.0),
        }
    }

    pub fn update(&mut self, delta: Duration) {
        // Consumo de suprimentos (Bloco 1)
        let consumption = 0.01 * delta.as_secs_f32();
        self.supplies = (self.supplies - consumption).max(0.0);

        if self.supplies == 0.0 {
            self.health -= 0.1 * delta.as_secs_f32();
        }
    }
}
