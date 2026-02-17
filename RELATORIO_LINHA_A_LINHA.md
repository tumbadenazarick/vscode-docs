# 🔍 ANÁLISE LINHA A LINHA - SISTEMA OMNIVERSE

## 🛠️ NÚCLEO RUST (core-rust)
- **src/main.rs:**
  - *L1-10:* Inicializa o `env_logger` para monitoramento.
  - *L12-25:* Cria a instância `Game` com configurações de "Lord Eclipse" e inicia o loop infinito.
- **src/core/game_state.rs:**
  - *L40-55:* Implementa o processamento paralelo via `Rayon`. Cada unidade e pessoa é atualizada simultaneamente em múltiplos núcleos de CPU.
- **src/abyss/fragmenter.rs:**
  - *L10-20:* Define a função `corrupt_entity_link`. Ela gera um erro intencional para testar se o motor consegue se recuperar de falhas lógicas.
- **src/archetypes/mod.rs:**
  - *L10-25:* Define a `SemanticSignature`. É o que impede que uma "Arma" seja confundida com um "Pet".

## 🧠 CÉREBRO PYTHON (brain-py)
- **nexus_management.py:**
  - *L35-60:* O `_detect_intent` usa expressões regulares para ler o código fonte em massa e decidir se ele pertence ao contexto Militar ou Social.
- **hot_reload.py:**
  - *L15-30:* Monitora o carimbo de tempo do arquivo `registry.json`. Se mudar, ele recarrega as variáveis globais do jogo sem desligar o sistema.

## 🌐 SERVIDOR TS (server-ts)
- **server.ts:**
  - *L20-45:* Configura o Socket.io. É a ponte de comunicação que permite ao jogador humano interagir com os milhares de NPCs processados pelo Rust.
