import os
import sys
import importlib.util
import traceback

def test_fragment(file_path):
    print(f"🔬 Analisando fragmento: {file_path}")
    try:
        # Tenta carregar o módulo
        spec = importlib.util.spec_from_file_location("fragmento", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        print("✅ Sintaxe OK")

        # Procura por funções comuns ou classes
        attrs = dir(module)
        print(f"📦 Atributos encontrados: {[a for a in attrs if not a.startswith('__')]}")

        return True
    except Exception:
        print("❌ ERRO DETECTADO:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    incoming_dir = "quarantine/incoming"
    files = [f for f in os.listdir(incoming_dir) if f.endswith(".py")]

    if not files:
        print("📭 Nenhum arquivo na pasta de entrada da quarentena.")
    else:
        for f in files:
            test_fragment(os.path.join(incoming_dir, f))
