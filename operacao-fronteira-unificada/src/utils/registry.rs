use serde::{Serialize, Deserialize};
use std::collections::HashMap;
use std::fs;

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Registry {
    pub game_metadata: GameMetadata,
    pub entities: HashMap<String, EntityMapping>,
    pub paths: HashMap<String, String>,
    pub economy_terms: HashMap<String, String>,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct GameMetadata {
    pub name: String,
    pub version: String,
    pub mode: String,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct EntityMapping {
    pub display_name: String,
    pub internal_id: String,
}

impl Registry {
    pub fn load() -> Result<Self, Box<dyn std::error::Error>> {
        let content = fs::read_to_string("config/registry.json")?;
        let registry: Registry = serde_json::from_str(&content)?;
        Ok(registry)
    }

    pub fn reload(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        let new_registry = Self::load()?;
        *self = new_registry;
        log::info!("🔄 Registro atualizado em tempo real!");
        Ok(())
    }

    pub fn get_name(&self, id: &str) -> String {
        self.entities.get(id)
            .map(|e| e.display_name.clone())
            .unwrap_or_else(|| id.to_string())
    }

    pub fn get_currency(&self) -> String {
        self.economy_terms.get("currency_name")
            .cloned()
            .unwrap_or_else(|| "Moeda".to_string())
    }
}
