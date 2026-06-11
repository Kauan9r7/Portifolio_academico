# Fase 3 - Gestão de Usuários e Segurança

Este documento detalha os controles de acesso implementados na interface e os mecanismos de segurança de disponibilidade adotados contra falhas de fornecedores terceiros.

---

## 1. Perfis de Usuários Definidos

O sistema implementa o mapeamento estático de papéis (RBAC - Role-Based Access Control) simulados no front-end para preservação de integridade:

* **Administrador (Admin):** Liberação total da interface, visibilidade do painel crítico de métricas (`#area-restrita`) e permissões de escrita.
* **Convidado (Guest):** Permissão estrita de leitura. A interface oculta de forma automatizada via manipulação de propriedades estruturais do DOM qualquer painel administrativo.

---

## 2. Políticas de Segurança e Alta Disponibilidade (Resiliência)

Com o suporte consultivo do Google Gemini, identificou-se uma vulnerabilidade de indisponibilidade decorrente da barreira de requisições de IPs anônimos impostas pela infraestrutura da GitHub REST API (*Rate Limiting* em 60 requisições/hora).

### Mitigação Aplicada:
* **Mecanismo de Fallback Automático:** O script de integração foi blindado com um bloco de tratamento estruturado (`try/catch`). Caso o servidor do GitHub responda com erros de exaustão de chamadas (`HTTP status 403`), o sistema intercepta a exceção e injeta imediatamente uma carga de dados estática salva de forma nativa.
* **Resultado:** O portfólio mantém-se 100% resiliente e disponível à banca examinadora acadêmica sob qualquer condição adversa de tráfego de rede.