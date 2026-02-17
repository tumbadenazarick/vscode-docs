use std::panic;

pub struct AbyssSandbox;

impl AbyssSandbox {
    pub fn run_experimental<F, R>(name: &str, logic: F) -> Option<R>
    where
        F: FnOnce() -> R + panic::UnwindSafe
    {
        log::info!("🌑 Entrando no Abyss Sandbox: Executando mecânica experimental '{}'", name);

        let result = panic::catch_unwind(logic);

        match result {
            Ok(val) => {
                log::info!("✅ Mecânica '{}' concluída com sucesso no Abyss.", name);
                Some(val)
            },
            Err(_) => {
                log::error!("💀 FALHA DETECTADA: Mecânica '{}' colapsou no Abyss. Sistema principal preservado.", name);
                None
            }
        }
    }
}
