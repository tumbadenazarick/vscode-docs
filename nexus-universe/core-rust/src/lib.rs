pub mod prelude {
    pub use crate::core::*;
    pub use crate::military::*;
    pub use crate::economy::*;
    pub use crate::ai::*;
    pub use crate::technology::*;
    pub use crate::utils::registry::*;
    pub use crate::utils::logger::*;
    pub use crate::utils::save_load::*;
    pub use crate::utils::ghost_manager::*;
    pub use crate::psychology::*;
    pub use crate::social::*;
    pub use crate::security::*;
    pub use crate::neural_link::*;
    pub use crate::plugin_loader::*;
}

pub mod core;
pub mod military;
pub mod economy;
pub mod ai;
pub mod technology;
pub mod utils;
pub mod psychology;
pub mod social;
pub mod abyss;
pub mod archetypes;
pub mod security;
pub mod neural_link;
pub mod plugin_loader;
