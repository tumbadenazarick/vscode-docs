use crate::prelude::*;
use std::time::{Duration, Instant};
use tokio::sync::mpsc;
use serde::{Serialize, Deserialize};

pub struct Game {
    pub state: GameStatus,
    pub economy: EconomySystem,
    pub military: MilitarySystem,
    pub ai: AISystem,
    pub technology: TechTree,
    pub event_tx: mpsc::UnboundedSender<GameEvent>,
    pub event_rx: mpsc::UnboundedReceiver<GameEvent>,
    pub last_update: Instant,
    pub config: GameConfig,
}

#[derive(Serialize, Deserialize)]
pub struct GameStatus {
    pub is_running: bool,
    pub tick: u64,
}

impl Game {
    pub async fn new(config: GameConfig) -> Result<Self, Box<dyn std::error::Error>> {
        let (event_tx, event_rx) = mpsc::unbounded_channel();

        Ok(Self {
            state: GameStatus { is_running: true, tick: 0 },
            economy: EconomySystem::new(config.starting_resources.clone()),
            military: MilitarySystem::new(),
            ai: AISystem::new(config.difficulty),
            technology: TechTree::default(),
            event_tx,
            event_rx,
            last_update: Instant::now(),
            config,
        })
    }

    pub async fn run(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        log::info!("Iniciando Operação Fronteira...");

        while self.state.is_running {
            let delta = self.last_update.elapsed();
            self.last_update = Instant::now();

            self.update(delta).await?;
            self.process_events().await?;

            self.state.tick += 1;
            tokio::time::sleep(Duration::from_millis(16)).await;
        }

        Ok(())
    }

    async fn update(&mut self, delta: Duration) -> Result<(), Box<dyn std::error::Error>> {
        self.economy.update(delta).await?;
        self.military.update(delta).await?;
        self.ai.update(delta, &self.military).await?;
        self.technology.update(delta).await?;
        Ok(())
    }

    async fn process_events(&mut self) -> Result<(), Box<dyn std::error::Error>> {
        while let Ok(event) = self.event_rx.try_recv() {
            match event {
                GameEvent::NPCDialogue { npc_id, text } => {
                    println!("[NPC {}]: {}", npc_id, text);
                }
                GameEvent::CommandConfirmed { code } => {
                    log::info!("Comando Validado: {}", code);
                }
                _ => {}
            }
        }
        Ok(())
    }
}
