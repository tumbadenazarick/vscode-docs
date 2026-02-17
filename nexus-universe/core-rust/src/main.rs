use operacao_fronteira_unificada::prelude::*;
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Inicializar o sistema de logs
    env_logger::init();
    log::info!("=== OPERAÇÃO FRONTEIRA: LORD ECLIPSE ===");
    log::info!("Iniciando Sistema de Defesa e Gestão Unificado...");

    // Configuração inicial do jogo
    let config = GameConfig::default()
        .with_player_name("Lord Eclipse")
        .with_difficulty(Difficulty::Hard);

    // Criação da instância mestre do jogo
    let mut game = Game::new(config).await?;

    // Execução do loop principal de simulação e comando
    game.run().await?;

    Ok(())
}
