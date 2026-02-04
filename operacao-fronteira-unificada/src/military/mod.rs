mod units;
mod commands;

pub use units::*;
pub use commands::*;

use std::time::Duration;
use dashmap::DashMap;
use std::sync::Arc;

pub struct MilitarySystem {
    pub units: Arc<DashMap<u32, Unit>>,
    pub command_system: CommandSystem,
}

impl MilitarySystem {
    pub fn new() -> Self {
        Self {
            units: Arc::new(DashMap::new()),
            command_system: CommandSystem::new(),
        }
    }

    pub async fn update(&mut self, _delta: Duration) -> Result<(), Box<dyn std::error::Error>> {
        Ok(())
    }
}
