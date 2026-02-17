use crate::archetypes::Action;

pub struct Npc;

impl Action for Npc {
    fn execute(&self) {
        println!("👤 O NPC ataca com arma de fogo (Intenção: Tática/Missão)");
    }
    fn intent(&self) -> String {
        "Execução de Ordens e Controle de Área".to_string()
    }
}
