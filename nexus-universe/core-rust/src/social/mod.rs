use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum SocialClass {
    Low,
    Medium,
    High,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum ProfessionType {
    Combatant,
    NonCombatant,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Profession {
    pub name: String,
    pub class: SocialClass,
    pub importance: SystemicImportance,
    pub p_type: ProfessionType,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum SystemicImportance {
    Critical, // Se morrerem, o jogo entra em colapso
    High,
    Medium,
    Low,
}
