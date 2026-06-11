# Fase 4 - Compartilhamento, Controle de Acesso e Versionamento

Este documento registra os padrões de engenharia de software adotados no gerenciamento do repositório PortfolioHUB, garantindo a integridade do código e preparando o ambiente para simulações colaborativas.

---

## 1. Estratégia de Versionamento (Git Flow Simplificado)

Para atender aos critérios de uso adequado de Git/GitHub solicitados nos requisitos, estabeleceu-se a seguinte política de ramificação (branches):

* **`main` (produção):** Branch protegida e estável. Contém apenas o código homologado que é publicado automaticamente no GitHub Pages.
* **`feature/seguranca-e-api`:** Branch temporária utilizada para o desenvolvimento e teste das implementações de tratamento de falhas da API e do painel de controle de usuários.

---

## 2. Configuração de Governança e Boas Práticas do Repositório

Visando a segurança e organização do código, foram aplicadas duas ações estruturais no repositório:

### A. Implementação do Arquivo `.gitignore`
* **Propósito:** Blindar o repositório contra o envio acidental de arquivos de lixo eletrônico gerados localmente por sistemas operacionais (como `.DS_Store` e `Thumbs.db`) ou ambientes de desenvolvimento (`.vscode/`).
* **Nota de Auditoria:** Como a integração consome o endpoint público da GitHub REST API, não há credenciais, chaves privadas ou tokens trafegando no código do lado do cliente (Client-side), eliminando riscos de exposição de segredos em conformidade com as diretrizes de segurança regulamentares.

### B. Práticas Colaborativas Demonstradas
* **Rastreabilidade:** Cada evolução das fases anteriores foi acompanhada de mensagens de commit claras e semânticas, permitindo a auditoria de evolução do projeto pela banca examinadora.