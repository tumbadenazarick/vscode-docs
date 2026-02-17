import os
import re
import json

class MassCodeLexer:
    """Analisador de massa de código para triagem automática."""

    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.function_registry = []

    def scan(self):
        print(f"🔍 Iniciando triagem de massa em: {self.target_dir}")
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith((".rs", ".py", ".ts", ".js")):
                    self._analyze_file(os.path.join(root, file))

    def _analyze_file(self, file_path):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            # Regex simples para capturar funções/métodos
            # Rust: pub fn name(...)
            # Python: def name(...)
            # JS/TS: function name(...) ou name(...) {
            patterns = [
                r"(?:pub\s+)?fn\s+([a-zA-Z_0-9]+)\s*\(",
                r"def\s+([a-zA-Z_0-9]+)\s*\(",
                r"function\s+([a-zA-Z_0-9]+)\s*\(",
            ]

            for pattern in patterns:
                matches = re.finditer(pattern, content)
                for match in matches:
                    self.function_registry.append({
                        "name": match.group(1),
                        "file": file_path,
                        "type": "function",
                        "context_hint": self._infer_context(file_path, match.group(1))
                    })

    def _infer_context(self, file_path, func_name):
        # Tenta inferir a intenção baseada no nome do arquivo ou da função
        if "pet" in file_path.lower() or "animal" in func_name.lower():
            return "PET_ARCHETYPE"
        if "npc" in file_path.lower() or "ia" in func_name.lower():
            return "NPC_ARCHETYPE"
        if "base" in file_path.lower() or "building" in func_name.lower():
            return "BASE_ARCHETYPE"
        if "weapon" in file_path.lower() or "gun" in func_name.lower() or "atacar" in func_name.lower():
            return "WEAPON_ARCHETYPE"
        return "GENERAL_CONTEXT"

    def save_report(self, output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.function_registry, f, indent=2, ensure_ascii=False)
        print(f"📊 Relatório de Massa gerado: {output_file}")
        self._generate_human_report()

    def _generate_human_report(self):
        print("\n--- 📝 RELATÓRIO DE INTENÇÃO (IDIOMA HUMANO) ---")
        contexts = {}
        for func in self.function_registry:
            ctx = func["context_hint"]
            if ctx not in contexts: contexts[ctx] = []
            contexts[ctx].append(func["name"])

        for ctx, funcs in contexts.items():
            print(f"\n📂 CONTEXTO: {ctx}")
            print(f"   Propósito: {self._describe_purpose(ctx)}")
            print(f"   Funções Identificadas: {', '.join(funcs[:5])}...")

    def _describe_purpose(self, context):
        descriptions = {
            "PET_ARCHETYPE": "Gerenciamento de mascotes, animais e apoio emocional.",
            "NPC_ARCHETYPE": "Lógica de inteligência artificial, decisões e diálogos.",
            "BASE_ARCHETYPE": "Gestão de infraestrutura, defesa de território e logística.",
            "WEAPON_ARCHETYPE": "Mecânicas de combate ofensivo, munição e dano direto.",
            "GENERAL_CONTEXT": "Funções genéricas de utilidade ou sistema base."
        }
        return descriptions.get(context, "Contexto abstrato ou não identificado.")

if __name__ == "__main__":
    lexer = MassCodeLexer(".")
    lexer.scan()
    lexer.save_report("mass_code_report.json")

    # Gerar resumo estatístico
    total = len(lexer.function_registry)
    print(f"✅ Total de funções mapeadas: {total}")
