use serde::{Serialize, Deserialize};
use std::collections::{HashMap, VecDeque};
use rand::Rng;
use crate::economy::ResourceType;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct NPCMilitar {
    pub id: String,
    pub name: String,
    pub role: NPCRole,
    pub personality: PersonalityTraits,
    pub dialogue_profile: DialogueProfile,
    pub relationship_with_player: i32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum NPCRole {
    Commander,
    Merchant,
    Diplomat,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PersonalityTraits {
    pub aggression: f32,
    pub greed: f32,
    pub loyalty: f32,
    pub caution: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DialogueProfile {
    pub tone: DialogueTone,
    pub catchphrases: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum DialogueTone {
    Formal,
    Casual,
    Aggressive,
}

impl NPCMilitar {
    pub fn new(id: String, name: String, role: NPCRole) -> Self {
        Self {
            id,
            name,
            role,
            personality: PersonalityTraits {
                aggression: 0.5,
                greed: 0.4,
                loyalty: 0.8,
                caution: 0.6,
            },
            dialogue_profile: DialogueProfile {
                tone: DialogueTone::Formal,
                catchphrases: vec!["A estratégia é tudo.".to_string()],
            },
            relationship_with_player: 0,
        }
    }

    pub fn generate_dialogue(&self, decision: &str, confirmed: bool) -> String {
        if !confirmed {
            return format!("[COMANDO BLOQUEADO]: {} requer código de confirmação. Operador: {}",
                decision.to_uppercase(), self.name);
        }

        let base_phrase = match decision {
            "attack" => {
                if self.personality.aggression > 0.7 {
                    "ALERTA: Forças inimigas detectadas - preparar ataque total!"
                } else {
                    "CONFIRMO: Iniciando manobra ofensiva coordenada."
                }
            },
            "trade" => "CONFIRMO: Proponho troca de suprimentos por créditos.",
            _ => "CONFIRMO: Mantendo vigilância no setor.",
        };

        format!("{} [STATUS: CONFIRMADO]", base_phrase)
    }
}
