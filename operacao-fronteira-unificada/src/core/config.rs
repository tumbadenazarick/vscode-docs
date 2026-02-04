use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use crate::economy::ResourceType;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GameConfig {
    pub player_name: String,
    pub difficulty: Difficulty,
    pub starting_resources: HashMap<ResourceType, f64>,
    pub victory_threshold: f32,
    pub economic_victory_threshold: f64,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize)]
pub enum Difficulty {
    Easy,
    Medium,
    Hard,
    Legendary,
}

impl Default for GameConfig {
    fn default() -> Self {
        let mut resources = HashMap::new();
        resources.insert(ResourceType::Credits, 1000.0);
        resources.insert(ResourceType::Minerals, 500.0);

        Self {
            player_name: "Comandante".to_string(),
            difficulty: Difficulty::Medium,
            starting_resources: resources,
            victory_threshold: 0.7,
            economic_victory_threshold: 100000.0,
        }
    }
}

impl GameConfig {
    pub fn with_player_name(mut self, name: &str) -> Self {
        self.player_name = name.to_string();
        self
    }
    pub fn with_difficulty(mut self, difficulty: Difficulty) -> Self {
        self.difficulty = difficulty;
        self
    }
}
