use crate::archetypes::{Action, SemanticSignature};

pub struct Weapon;

impl Action for Weapon {
    fn execute(&self) {
        println!("🔫 A Arma ataca com munição (Intenção: Dano Direto)");
    }
    fn intent(&self) -> String {
        "Destruição de Alvos e Combate Ofensivo".to_string()
    }
    fn signature(&self) -> SemanticSignature {
        SemanticSignature::Militar
    }
}
