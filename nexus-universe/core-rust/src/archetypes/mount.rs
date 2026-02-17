use crate::archetypes::{Action, SemanticSignature};

pub struct Mount;

impl Action for Mount {
    fn execute(&self) {
        println!("🐎 A Montaria acelera (Intenção: Transporte)");
    }
    fn intent(&self) -> String {
        "Mobilidade e Deslocamento Rápido".to_string()
    }
    fn signature(&self) -> SemanticSignature {
        SemanticSignature::Transporte
    }
}
