use tokio::sync::broadcast;
use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum VersionType {
    Aurora,
    Abyss,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Message {
    pub from: VersionType,
    pub payload: String,
    pub intent_id: String,
}

pub struct NeuralLink {
    pub tx: broadcast::Sender<Message>,
}

impl NeuralLink {
    pub fn new() -> Self {
        let (tx, _) = broadcast::channel(100);
        Self { tx }
    }

    pub fn send_pulse(&self, from: VersionType, intent: &str, data: &str) {
        let msg = Message {
            from,
            intent_id: intent.to_string(),
            payload: data.to_string(),
        };
        let _ = self.tx.send(msg);
    }

    pub fn listen(&self) -> broadcast::Receiver<Message> {
        self.tx.subscribe()
    }
}

// Lógica de Sincronização: Detecta se Aurora e Abyss estão tentando fazer coisas opostas no mesmo ID
pub fn detect_conflict(m1: &Message, m2: &Message) -> Option<String> {
    // Se o ID for igual mas as versões forem diferentes, pode haver conflito
    if m1.intent_id == m2.intent_id && format!("{:?}", m1.from) != format!("{:?}", m2.from) {
         return Some(format!("⚠️ CONFLITO DE VERSÃO: {:?} vs {:?} no objetivo {}", m1.from, m2.from, m1.intent_id));
    }
    None
}
