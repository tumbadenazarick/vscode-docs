pub mod pet;
pub mod npc;
pub mod base;
pub mod weapon;

pub trait Action {
    fn execute(&self);
    fn intent(&self) -> String;
}
