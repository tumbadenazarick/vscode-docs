# Resumo Detalhado: Galaxia Aurora & Nexus Integrado

## Visão Geral do Projeto
O sistema unificado combina RPG de estratégia, simulação econômica e gestão militar em uma arquitetura monorepo distribuída entre Rust (Performance/Combate) e Python (IA/Estratégia).

## Arquitetura de Componentes

### 1. Núcleo de Comando Nexus (SistemaMestre)
O cérebro estratégico que gerencia a autoridade do comandante.
- **Blindagem SHA-256:** Cada ação gera um token de autorização (`NEXUS-AUTH-...`) para evitar "funções fantasma".
- **Hierarquia Cardinal:** Permissões de nível 10 permitem reescrita de realidade e comandos globais.

### 2. Engine Operação Fronteira (Rust)
Responsável pelo processamento massivo de entidades e combate.
- **Status Effects:** Gerencia regeneração, escudos e debuffs com persistência entre turnos.
- **Poder Estocástico:** Introduz variabilidade no combate, onde o "Poder Total" é uma combinação de base determinística e variação aleatória de 5%.

### 3. Abyss Fragmenter & Mirror
O sistema de "Caos" que gera instabilidade controlada.
- **Inversão AST:** O `EspelhoInversor` lê o código da Aurora e gera o código do Abyss (ex: transforma `ataque` em `defesa`), permitindo que o jogo aprenda e se adapte à estratégia do jogador criando sua antítese perfeita.

### 4. Economia e Psicologia (Lógica de Fricção)
Integração profunda entre recursos e moral.
- **Maslow Tier:** NPCs evoluem em suas necessidades. A falta de recursos econômicos rebaixa os NPCs para o nível de "Segurança", aumentando o estresse e o risco de insurreição.

## Fluxo de Jogo (Loop Principal)
1. **Fase de Manutenção:** Redução de cooldowns e processamento de regeneração de HP (Rust).
2. **Fase Econômica:** Geração de ouro e cálculo de eficiência (Python).
3. **Fase de Comando:** O jogador emite ordens via código CMD, validadas pelo Sentinel.
4. **Fase de Conflito:** O Abyss Mirror analisa a estratégia e injeta entropia no sistema.

## Próximos Passos
A integração completa exige que o `registry.json` mapeie todos os tokens de autorização entre os módulos, permitindo o Hot-Reload sincronizado.
