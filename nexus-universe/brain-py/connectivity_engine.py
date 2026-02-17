import os
import re

class ConnectivityEngine:
    """Detecta 'Código Vermelho' (desconectado) e sugere pontes de integração."""

    def __init__(self, root_dir="nexus-universe"):
        self.root_dir = root_dir
        self.modules = []
        self.dependencies = {}

    def map_connections(self):
        print("🔍 Mapeando conexões neurais do código...")
        for root, _, files in os.walk(self.root_dir):
            for f in files:
                if f.endswith((".rs", ".py", ".ts")):
                    path = os.path.join(root, f)
                    self.modules.append(path)
                    self._extract_imports(path)

    def _extract_imports(self, path):
        with open(path, "r", errors="ignore") as f:
            content = f.read()
            # Procura por 'use', 'import', 'require'
            imports = re.findall(r"(?:use|import|from|require)\s+([\w\.\:]+)", content)
            self.dependencies[path] = imports

    def list_red_code(self):
        """Lista arquivos que não importam ninguém nem são importados por ninguém."""
        print("\n🚩 RELATÓRIO DE CÓDIGO VERMELHO (DESCONECTADO):")
        all_deps = [d for deps in self.dependencies.values() for d in deps]

        for mod in self.modules:
            name = os.path.basename(mod).split(".")[0]
            is_imported = any(name in dep for dep in all_deps)
            has_imports = len(self.dependencies.get(mod, [])) > 0

            if not is_imported and not has_imports:
                print(f"🔴 DESCONECTADO: {mod}")
                print(f"   👉 Sugestão: Criar ponte em 'lib.rs' ou 'main.py'.")

if __name__ == "__main__":
    engine = ConnectivityEngine()
    engine.map_connections()
    engine.list_red_code()
