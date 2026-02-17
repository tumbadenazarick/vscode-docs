mod research;
pub use research::*;

use std::time::Duration;

pub struct TechTree {
    pub technologies: Vec<Technology>,
}

impl Default for TechTree {
    fn default() -> Self {
        Self { technologies: Vec::new() }
    }
}

impl TechTree {
    pub async fn update(&mut self, _delta: Duration) -> Result<(), Box<dyn std::error::Error>> {
        Ok(())
    }
}
