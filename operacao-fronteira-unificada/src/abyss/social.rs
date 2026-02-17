use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DiscordSystem {
    pub internal_conflicts: u32,
}

impl DiscordSystem {
    pub fn generate_rumor(&self, npc_name: &str) -> String {
        format!("Boato espalhado: {} está planejando uma rebelião secreta!", npc_name)
    }
}
