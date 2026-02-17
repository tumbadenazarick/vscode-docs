use operacao_fronteira_unificada::prelude::*;

#[test]
fn test_ghost_function_tracking() {
    let ghost_manager = GhostManager::new();

    // Simula a chamada de uma função que ainda não foi implementada
    ghost_manager.call_ghost("spawn_mount", "MOUNT_SYSTEM");
    ghost_manager.call_ghost("spawn_mount", "MOUNT_SYSTEM");
    ghost_manager.call_ghost("calculate_mana", "MAGIC_SYSTEM");

    let ghosts = ghost_manager.ghosts;

    assert!(ghosts.contains_key("MOUNT_SYSTEM:spawn_mount"));
    assert_eq!(ghosts.get("MOUNT_SYSTEM:spawn_mount").unwrap().call_count, 2);
    assert_eq!(ghosts.get("MAGIC_SYSTEM:calculate_mana").unwrap().call_count, 1);

    println!("✅ Ghost Manager rastreou com sucesso as funções fantasmas.");
}
