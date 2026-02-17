# RELATÓRIO DE INTENÇÃO - SISTEMA NEXUS MASTER (TRIAGEM DE MASSA)

## 1. Módulos Identificados e Propósitos
*   **NexusSieve:** Atua como um filtro pré-commit. Ele classifica o código recebido em categorias (Militar, Economia, etc.) e coloca automaticamente novas funções em "Quarentena" antes da unificação.
*   **NexusSemanticParser:** Resolve o problema de "mesmo nome, intenções diferentes". Ele usa busca por palavras-chave (regex) para detectar se um objeto chamado "NPC" é, na verdade, uma Arma, Montaria, Pet ou Base.
*   **NexusMassiveAnalyzer:** Gerencia a "Assinatura de Alma" (Hash) de cada bloco de código. Permite a **Renomeação Global (Hot-Rename)**: você muda o nome de um personagem em um lugar e o sistema protege todas as referências internas.
*   **Abyss Fragmenter/Disruptor:** O módulo de entropia. Projetado para desestabilizar o jogo propositalmente (ex: corromper links, injetar inflação negativa) para testar a resiliência do sistema e permitir falhas criativas.

## 2. Solução para o Problema de Ambiguidade (Nomes Iguais)
O sistema não confiará apenas no nome da classe. Ele utilizará uma **Assinatura de Contexto**:
*   `NPC` + [keywords: fogo, ataque, tática] -> **CONTEXTO MILITAR**
*   `NPC` + [keywords: sela, stamina, galope] -> **CONTEXTO MONTARIA**
*   `NPC` + [keywords: carinho, lealdade, evoluir] -> **CONTEXTO PET**

## 3. Estratégia para "Funções Fantasmas"
Funções que ainda não existem fisicamente serão registradas na `biblioteca_fantasmas`. O `GhostManager` em Rust será notificado para rastrear quantas vezes essas funções são chamadas pela IA antes de serem programadas, gerando um mapa de prioridade de desenvolvimento.

## 4. Riscos de Primeira Análise
*   **Colisão de Hash:** Se dois códigos forem 100% idênticos, o Hash de alma será igual.
*   **Falsos Positivos de Contexto:** Um "Pet" que tem uma função de "Ataque" pode ser confundido com um "Soldado".
    *   *Solução:* Implementar pesos (ex: se tiver 'mordida' e 'ataque', Pet ganha mais peso que Soldado).
