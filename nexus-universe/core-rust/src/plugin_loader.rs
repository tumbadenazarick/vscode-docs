use std::fs;
use std::path::Path;

pub struct PluginLoader;

impl PluginLoader {
    pub fn load_external_logic() {
        let plugin_dir = "../plugins";
        if let Ok(entries) = fs::read_dir(plugin_dir) {
            for entry in entries {
                if let Ok(entry) = entry {
                    let path = entry.path();
                    if path.is_file() {
                        log::info!("🔌 Módulo Externo Detectado: {:?}", path.file_name().unwrap());
                        // Aqui o motor registraria a lógica contida no arquivo para expansão sem limites
                    }
                }
            }
        }
    }
}
