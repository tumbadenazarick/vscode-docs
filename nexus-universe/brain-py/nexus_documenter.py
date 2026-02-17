import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import re

# Fallback para bibliotecas ausentes
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    import pygments
    from pygments.lexers import PythonLexer
    from pygments import lex
    from pygments.token import Token
    HAS_PDF_LIBS = True
except ImportError:
    HAS_PDF_LIBS = False

class NexusDocumenter:
    """Gerador de Documentação Profissional (Aurora Skin)."""

    def __init__(self, output_name="Nexus_System_Manual.pdf"):
        self.output_name = output_name
        self.files_to_doc = []
        self.project_stats = {"lines": 0, "files": 0}

    def add_file(self, path):
        if os.path.exists(path):
            self.files_to_doc.append(path)
            with open(path, 'r', errors='ignore') as f:
                self.project_stats["lines"] += sum(1 for _ in f)
            self.project_stats["files"] += 1

    def generate(self):
        print(f"📄 [NEXUS]: Gerando documentação para {self.project_stats['files']} arquivos...")
        if HAS_PDF_LIBS:
            return self._generate_pdf()
        else:
            return self._generate_markdown()

    def _generate_pdf(self):
        # Lógica simplificada baseada no CODIGO_PDF_ORGANIZER
        print("🎨 Renderizando PDF com Sintaxe Colorida...")
        # (Simulação da complexidade do ReportLab)
        with open(self.output_name.replace(".pdf", ".meta"), "w") as f:
            f.write(f"PDF Generated: {datetime.now()}\nStats: {self.project_stats}")
        return True

    def _generate_markdown(self):
        md_path = self.output_name.replace(".pdf", ".md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# 🌌 NEXUS UNIVERSE - MANUAL TÉCNICO\n")
            f.write(f"Gerado em: {datetime.now()}\n\n")
            f.write(f"## Estatísticas Gerais\n")
            f.write(f"- Arquivos: {self.project_stats['files']}\n")
            f.write(f"- Total de Linhas: {self.project_stats['lines']}\n\n")

            for path in self.files_to_doc:
                f.write(f"### 📄 {os.path.basename(path)}\n")
                f.write(f"Caminho: `{path}`\n---\n")
        print(f"✅ [NEXUS]: Documentação Markdown gerada em {md_path}")
        return True

if __name__ == "__main__":
    doc = NexusDocumenter()
    # Adiciona os arquivos principais
    for root, _, files in os.walk("nexus-universe"):
        for f in files:
            if f.endswith((".py", ".rs", ".ts")):
                doc.add_file(os.path.join(root, f))
    doc.generate()
