use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use std::time::Duration;
use thiserror::Error;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq, Hash)]
pub enum ResourceType {
    Credits,
    Minerals,
    Energy,
    Food,
    Supplies,
    Fuel,
}

pub struct ResourceStorage {
    pub resources: HashMap<ResourceType, f64>,
    pub capacity: HashMap<ResourceType, f64>,
}

impl ResourceStorage {
    pub fn new(starting: HashMap<ResourceType, f64>) -> Self {
        let mut capacity = HashMap::new();
        for res in starting.keys() {
            capacity.insert(res.clone(), 10000.0);
        }
        Self {
            resources: starting,
            capacity,
        }
    }

    pub async fn update(&mut self, delta: Duration) -> Result<(), EconomyError> {
        // Simulação de renda passiva (ex: +1 por tick de energia)
        let amount = 1.0 * (delta.as_secs_f64());
        let current = self.resources.entry(ResourceType::Energy).or_insert(0.0);
        *current = (*current + amount).min(10000.0);
        Ok(())
    }

    pub fn can_afford(&self, costs: &HashMap<ResourceType, f64>) -> bool {
        costs.iter().all(|(res, &amt)| {
            self.resources.get(res).unwrap_or(&0.0) >= &amt
        })
    }

    pub fn total_wealth(&self) -> f64 {
        self.resources.values().sum()
    }
}

#[derive(Debug, Error)]
pub enum EconomyError {
    #[error("Recursos insuficientes")]
    InsufficientResources,
}
