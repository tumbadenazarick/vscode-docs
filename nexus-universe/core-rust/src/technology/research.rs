use serde::{Serialize, Deserialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Technology {
    pub id: String,
    pub name: String,
    pub researched: bool,
}
