use std::collections::HashMap;
use std::sync::Arc;
use dashmap::DashMap;
use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum PermissionLevel {
    Guest,
    Soldier,
    Commander,
    GodMode,
}

pub struct SecurityGuardian {
    pub permissions: Arc<DashMap<String, PermissionLevel>>,
    pub call_history: Arc<DashMap<String, usize>>,
}

impl SecurityGuardian {
    pub fn new() -> Self {
        let guardian = Self {
            permissions: Arc::new(DashMap::new()),
            call_history: Arc::new(DashMap::new()),
        };

        // Permissões iniciais
        guardian.permissions.insert("PROTAGONISTA_001".to_string(), PermissionLevel::GodMode);
        guardian
    }

    pub fn validate_call(&self, entity_id: &str, required_level: PermissionLevel) -> bool {
        let current_level = self.permissions.get(entity_id)
            .map(|l| l.clone())
            .unwrap_or(PermissionLevel::Guest);

        let authorized = match (current_level, required_level) {
            (PermissionLevel::GodMode, _) => true,
            (PermissionLevel::Commander, PermissionLevel::GodMode) => false,
            (PermissionLevel::Commander, _) => true,
            (PermissionLevel::Soldier, PermissionLevel::Commander) => false,
            (PermissionLevel::Soldier, PermissionLevel::GodMode) => false,
            (PermissionLevel::Soldier, _) => true,
            (PermissionLevel::Guest, PermissionLevel::Guest) => true,
            _ => false,
        };

        if !authorized {
            log::error!("🛑 ACESSO NEGADO: Entidade '{}' tentou executar função de alto nível.", entity_id);
        } else {
            let mut count = self.call_history.entry(entity_id.to_string()).or_insert(0);
            *count += 1;
        }

        authorized
    }

    pub fn integrity_check(&self, code_fragment: &str, expected_hash: &str) -> bool {
        let actual_hash = format!("{:x}", md5::compute(code_fragment));
        actual_hash == expected_hash
    }
}
