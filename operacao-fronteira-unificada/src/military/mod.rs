mod units;
mod commands;

pub use units::*;
pub use commands::*;

use std::time::Duration;

pub struct MilitarySystem {
    pub units: Vec<Unit>,
    pub command_system: CommandSystem,
}

impl MilitarySystem {
    pub fn new() -> Self {
        Self {
            units: Vec::new(),
            command_system: CommandSystem::new(),
        }
    }

    pub async fn update(&mut self, _delta: Duration) -> Result<(), Box<dyn std::error::Error>> {
        Ok(())
    }
}
