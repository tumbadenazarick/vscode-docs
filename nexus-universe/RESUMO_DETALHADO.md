# Resumo Detalhado: Nexus Universe

## Arquitetura do Sistema (Monorepo)
O "Nexus Universe" agora é organizado como um monorepo unificado, integrando o backend TypeScript e o cérebro estratégico em Python.

### 1. Motor de Hierarquia Militar e Comportamento
A `MilitaryBase` não é apenas um sistema de patentes, mas um motor de resposta comportamental.
- **Lógica de Resposta:** NPCs reagem de forma diferente com base em sua patente. Um `Soldado` é focado em execução, enquanto um `General` foca em estratégia macro.
- **Validação de Intenção:** Nenhuma ação crítica ocorre sem um código `CMD-XXXXXX`. Isso simula a "corrente de comando" e evita falhas sistêmicas (funções fantasma).

### 2. Guardião de Segurança (Security Guardian)
Atua como o firewall do jogo. Ele valida a integridade de cada comando enviado ao motor. No futuro, este sistema será integrado ao `std::panic::catch_unwind` do Rust para garantir que falhas lógicas em comandos experimentais não derrubem o servidor.

### 3. Economia de Eficiência e Entropia
Diferente de economias tradicionais de RPG, aqui o foco é na **estabilidade sistêmica**.
- **Eficiência:** Afetada por tecnologias e moral (Protocolo Aurora).
- **Entropia/Corrupção:** Injetada pelo Abyss. Representa a degradação dos links econômicos e a perda de recursos por "caos" administrativo ou sabotagem.

### 4. Tecnologia e NeuralLink
A árvore tecnológica (`TechTree`) agora aplica modificadores reais à eficiência militar e mitigação de entropia. O `NeuralLink` atua como o sistema nervoso central, rastreando entidades (NPCs) e simulando o conflito constante entre Aurora e Abyss.

### 5. Psicologia e Necessidades (Maslow)
Implementamos a base para o sistema psicológico dos NPCs. O estresse é influenciado pela entropia do ambiente, podendo levar a estados de rebelião, afetando diretamente a economia e a segurança da base.

## A "Lógica de Fricção"
O jogo utiliza uma "Lógica de Fricção" onde cada ação tem um custo não apenas em recursos, mas em estabilidade. O estresse acumulado no sistema (Entropia) pode gerar falhas críticas, desertores ou revoltas, forçando o jogador a equilibrar expansão tecnológica com manutenção da ordem.

## Unificação e CI/CD
O sistema foi movido para uma estrutura de monorepo em `nexus-universe/`. O backend em Node.js reside em `server-ts/`, enquanto a lógica de IA está em `brain-py/`. A pipeline de CI/CD foi atualizada para validar ambos os mundos, garantindo que testes de IA e build de infraestrutura ocorram em sincronia.

## Conclusão e Próximos Passos
Este núcleo unificado serve como o cérebro estratégico que dita as regras para o motor de alto desempenho em Rust (core-rust). A próxima fase envolverá a implementação física dos arquétipos semânticos e a expansão da economia de recursos massivos.
