use crate::archetypes::{Action, SemanticSignature};

pub struct Pet;

impl Action for Pet {
    fn execute(&self) {
        println!("🐾 O Pet ataca com mordida (Intenção: Lealdade/Proteção)");
    }
    fn intent(&self) -> String {
        "Apoio Emocional e Combate Próximo".to_string()
    }
    fn signature(&self) -> SemanticSignature {
        SemanticSignature::Suporte
    }
}
