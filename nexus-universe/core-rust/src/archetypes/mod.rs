pub mod pet;
pub mod npc;
pub mod base;
pub mod weapon;
pub mod mount;

pub trait Action {
    fn execute(&self);
    fn intent(&self) -> String;
    fn signature(&self) -> SemanticSignature;
}

#[derive(Debug, Clone, PartialEq)]
pub enum SemanticSignature {
    Militar,
    Economica,
    Social,
    Suporte,
    Transporte,
}
