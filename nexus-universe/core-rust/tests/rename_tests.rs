use operacao_fronteira_unificada::prelude::*;
use std::fs;

#[test]
fn test_hot_rename_via_registry() {
    let mut registry = Registry::load().unwrap();

    // Nome original do protagonista
    assert_eq!(registry.get_name("PROTAGONISTA_001"), "Caíque");

    // Simula alteração externa no arquivo registry.json
    let original_content = fs::read_to_string("../config/registry.json").unwrap();
    let new_content = original_content.replace("\"display_name\": \"Caíque\"", "\"display_name\": \"Lord Eclipse\"");
    fs::write("../config/registry.json", new_content).unwrap();

    // Executa o Hot-Reload
    registry.reload().unwrap();

    // Verifica se o nome mudou sem quebrar o ID interno
    assert_eq!(registry.get_name("PROTAGONISTA_001"), "Lord Eclipse");

    // Restaura o arquivo original para não afetar outros testes
    fs::write("../config/registry.json", original_content).unwrap();

    println!("✅ Hot-Rename validado: O nome mudou em tempo real mantendo a integridade do sistema.");
}
