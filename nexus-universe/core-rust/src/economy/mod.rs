mod resources;
pub use resources::*;

use std::time::Duration;

pub struct EconomySystem {
    pub storage: ResourceStorage,
}

impl EconomySystem {
    pub fn new(starting: std::collections::HashMap<ResourceType, f64>) -> Self {
        Self {
            storage: ResourceStorage::new(starting),
        }
    }

    pub async fn update(&mut self, delta: Duration) -> Result<(), Box<dyn std::error::Error>> {
        self.storage.update(delta).await?;
        Ok(())
    }
}
