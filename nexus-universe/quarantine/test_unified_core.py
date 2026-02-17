import sys
import os

# Adiciona o diretório brain-py ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'brain-py'))

from unified_core import GalaxiaAurora, SecurityGuardian, EconomySystem, MilitaryBase

def run_nexus_tests():
    print("🧪 [TEST] Iniciando Bateria de Testes Unificados...\n")

    # 1. Teste de Segurança
    print("--- Teste 1: Segurança de Comando ---")
    assert SecurityGuardian.validate_command("CMD-123456") == True
    assert SecurityGuardian.validate_command("ERRO-000000") == False
    print("✅ OK\n")

    # 2. Teste de Economia
    print("--- Teste 2: Sustentabilidade Econômica ---")
    eco = EconomySystem(5000)
    eco.custo_manutencao = 2000
    # Produção de 1200 com custo de 2000 deve resultar em perda
    # Saldo = 5000 + (1200 - 2000) = 4200
    eco.processar_ciclo(1200)
    assert eco.ouro == 4200
    print("✅ OK\n")

    # 3. Teste de Comportamento Militar
    print("--- Teste 3: Comportamento e Atrito ---")
    general = MilitaryBase("Sun Tzu", "General")
    # Ordem com código válido
    sec, act = general.execute_order("Ofensiva de Inverno", "CMD-999111")
    assert sec == True
    # Ordem com código inválido
    sec, act = general.execute_order("Retirada", "INVALIDO")
    assert sec == False
    print("✅ OK\n")

    # 4. Simulação de Turno Completo
    print("--- Teste 4: Ciclo Vital do Jogo ---")
    jogo = GalaxiaAurora("Caíque")
    jogo.rodar_turno("Inspeção de Tropas", "CMD-000111")
    assert jogo.turno == 2
    print("✅ OK\n")

    print("🏁 [FINISH] Todos os sistemas Nexus estão nominais!")

if __name__ == "__main__":
    try:
        run_nexus_tests()
    except AssertionError as e:
        print(f"❌ [FAIL] Teste falhou! Detalhes: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"💥 [CRASH] Erro inesperado: {e}")
        sys.exit(1)
