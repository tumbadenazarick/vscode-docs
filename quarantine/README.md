# SISTEMA DE QUARENTENA - OMNIVERSE

Este diretório isola códigos novos ou defeituosos para evitar quebras no sistema principal.

## Como usar:
1. Coloque o novo código em `quarantine/incoming/`.
2. Execute `python quarantine/tester.py`.
3. Se o teste passar, mova o código para a pasta correta (`src/` ou `galaxia-aurora-python/`).
4. Se falhar, corrija o erro antes da integração.

## Pastas:
- `incoming/`: Arquivos aguardando análise.
- `sandbox/`: Área para testes manuais.
- `logs/`: Relatórios de erros.
