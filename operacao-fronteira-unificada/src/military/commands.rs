use serde::{Serialize, Deserialize};
use rand::Rng;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Command {
    pub id: u64,
    pub action: String,
    pub confirmed: bool,
    pub confirmation_code: String,
}

pub struct CommandSystem {
    pub pending: Vec<Command>,
}

impl CommandSystem {
    pub fn new() -> Self {
        Self { pending: Vec::new() }
    }

    pub fn issue_command(&mut self, action: &str) -> String {
        let mut rng = rand::thread_rng();
        let code: u32 = rng.gen_range(100000..999999);
        let code_str = format!("CMD-{}", code);

        let cmd = Command {
            id: rng.gen(),
            action: action.to_string(),
            confirmed: false,
            confirmation_code: code_str.clone(),
        };

        self.pending.push(cmd);
        code_str
    }

    pub fn validate_code(&mut self, code: &str) -> bool {
        if let Some(cmd) = self.pending.iter_mut().find(|c| c.confirmation_code == code) {
            cmd.confirmed = true;
            log::info!("Comando {} confirmado com sucesso!", cmd.action);
            return true;
        }
        false
    }
}
