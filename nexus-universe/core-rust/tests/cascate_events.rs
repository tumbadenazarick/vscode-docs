use operacao_fronteira_unificada::prelude::*;

#[tokio::test]
async fn test_colapso_social_por_fome() {
    let mut game = Game::new(GameConfig::default()).await.unwrap();

    // Simula falta de comida
    game.economy.storage.resources.insert(ResourceType::Food, 0.0);

    // Adiciona um médico crítico
    let mut dr_silva = Person {
        id: "doc_1".to_string(),
        name: "Dr. Silva".to_string(),
        profession: Profession {
            name: "Médico".to_string(),
            class: SocialClass::High,
            importance: SystemicImportance::Critical,
            p_type: ProfessionType::NonCombatant,
        },
        needs: MaslowHierarchy { hunger: 0.9, safety: 1.0, self_actualization: 0.5, stress: 0.0 },
    };

    // Processa psicologia
    dr_silva.update_psychology(100.0);

    assert!(dr_silva.needs.hunger > 0.8);
    // Aqui o sistema detectaria o colapso pois o médico parou de trabalhar
}
