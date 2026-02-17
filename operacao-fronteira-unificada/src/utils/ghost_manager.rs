use dashmap::DashMap;
use std::sync::Arc;
use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GhostFunction {
    pub name: String,
    pub context: String,
    pub call_count: u64,
}

pub struct GhostManager {
    pub ghosts: Arc<DashMap<String, GhostFunction>>,
}

impl GhostManager {
    pub fn new() -> Self {
        Self {
            ghosts: Arc::new(DashMap::new()),
        }
    }

    pub fn call_ghost(&self, name: &str, context: &str) {
        let key = format!("{}:{}", context, name);
        let mut ghost = self.ghosts.entry(key.clone()).or_insert(GhostFunction {
            name: name.to_string(),
            context: context.to_string(),
            call_count: 0,
        });
        ghost.call_count += 1;
        log::warn!("👻 Função Fantasma chamada: {} no contexto {}. Chamadas: {}", name, context, ghost.call_count);
    }
}
