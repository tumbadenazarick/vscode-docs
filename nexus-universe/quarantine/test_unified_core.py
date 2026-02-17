import sys
import os

# Adiciona o diretório brain-py ao path para importar o unified_core
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'brain-py'))

from unified_core import MilitaryBase, SecurityGuardian, EconomySystem, TechTree, NeuralLink

def run_tests():
    print("=== INICIANDO TESTES DO NEXUS UNIVERSE ===\n")

    # 1. Teste de Segurança
    print("--- Teste 1: Segurança ---")
    assert SecurityGuardian.validate_command("CMD-123456") == True
    assert SecurityGuardian.validate_command("ABC-123456") == False
    print("OK\n")

    # 2. Teste de Base Militar
    print("--- Teste 2: Base Militar ---")
    general = MilitaryBase("Sun Tzu", "General")
    # Ordem válida (segurança deve passar)
    sec_ok, act_ok = general.execute_order("Bombardeio", "CMD-999888")
    assert sec_ok == True
    # Ordem inválida (sem código)
    sec_ok, act_ok = general.execute_order("Bombardeio", "NO-CODE")
    assert sec_ok == False
    print("OK\n")

    # 3. Teste de Economia e Entropia
    print("--- Teste 3: Economia ---")
    econ = EconomySystem(1000)
    econ.update_cycle(100)
    assert econ.resources == 1100
    econ.inject_entropy(0.5)
    econ.update_cycle(100) # 100 * 1.0 * (1 - 0.5) = 50
    assert econ.resources == 1150
    print("OK\n")

    # 4. Teste de Tecnologia
    print("--- Teste 4: Tecnologia ---")
    tech = TechTree()
    econ.resources = 600
    assert tech.research("IA Militar", econ, general) == True
    assert general.efficiency_bonus > 1.0
    assert econ.resources == 100
    assert tech.research("IA Militar", econ, general) == False # Já pesquisada
    assert tech.research("Fusão Estelar", econ) == False # Sem fundos
    print("OK\n")

    # 5. Teste de NeuralLink e Conflito
    print("--- Teste 5: NeuralLink ---")
    link = NeuralLink()
    link.broadcast("SISTEMA", "Teste de broadcast")
    # Simula conflito algumas vezes para garantir que roda sem erro
    for _ in range(5):
        link.simulate_conflict(econ, general)
    print("OK\n")

    print("=== TODOS OS TESTES PASSARAM COM SUCESSO! ===")

if __name__ == "__main__":
    run_tests()
