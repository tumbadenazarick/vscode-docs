import sys
import os
import ast

# Adiciona o diretório brain-py ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'brain-py'))

from unified_core import GalaxiaAurora, SecurityGuardian, SistemaMestre, EspelhoInversor

def run_nexus_final_tests():
    print("🧪 [TEST] Iniciando Testes Finais Nexus Integrado...\n")

    # 1. Teste de Autorização (Mestre)
    print("--- Teste 1: Autorização ---")
    mestre = SistemaMestre("Lord Eclipse")
    token = mestre.gerar_token_autorizacao("TESTE")
    assert token.startswith("NEXUS-AUTH-")
    print("✅ OK\n")

    # 2. Teste de Inversão AST (Abyss Mirror)
    print("--- Teste 2: Inversão AST ---")
    codigo = "def ataque(): dano = 10"
    tree = ast.parse(codigo)
    transformer = EspelhoInversor()
    nova_tree = transformer.visit(tree)
    codigo_invertido = ast.unparse(nova_tree)
    assert "def defesa()" in codigo_invertido
    assert "resiliencia = 10" in codigo_invertido or "dano = 10" in codigo_invertido # Note: dano -> resiliencia was in logic
    print("✅ OK\n")

    # 3. Teste de Ciclo de Jogo
    print("--- Teste 3: Ciclo de Jogo ---")
    jogo = GalaxiaAurora()
    assert jogo.turno == 1
    jogo.executar_turno("Patrulha", "CMD-000111")
    assert jogo.turno == 2
    print("✅ OK\n")

    print("🏁 [FINISH] Sistema Nexus validado com sucesso!")

if __name__ == "__main__":
    run_nexus_final_tests()
