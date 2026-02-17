use crate::archetypes::Action;

pub struct Base;

impl Action for Base {
    fn execute(&self) {
        println!("🏰 A Base ataca com artilharia (Intenção: Defesa de Território)");
    }
    fn intent(&self) -> String {
        "Proteção de Recursos e Logística".to_string()
    }
}
