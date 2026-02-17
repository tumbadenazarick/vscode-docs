use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum GameEvent {
    // Militares
    UnitTrained { unit_id: u32, unit_type: String },
    AttackLaunched { attacker_id: u32, target_id: u32 },
    CommandConfirmed { code: String },

    // IA
    NPCDialogue { npc_id: String, text: String },

    // Economia
    ResourceUpdate { resource: String, amount: f64 },

    // Sistema
    Victory(String),
    Defeat(String),
}
