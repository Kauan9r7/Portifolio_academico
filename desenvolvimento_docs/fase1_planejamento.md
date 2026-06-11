# Fase 1 - Planejamento da Implantação: PortfolioHUB

Este documento estabelece a estratégia de arquitetura, o plano de implantação e o cronograma acelerado para o projeto PortfolioHUB, utilizando o Google Gemini como assistente estratégico de engenharia.

---

## 1. Arquitetura da Solução Proposta

Para garantir escalabilidade, segurança e uma integração fluida com a API do GitHub, a arquitetura padrão recomendada para o PortfolioHUB seguirá o modelo abaixo:

* **Camada de Apresentação (Frontend):** Interface responsiva construída em React.js (ou Next.js) e estilizada com Tailwind CSS, garantindo visualização otimizada dos portfólios.
* **Camada de Integração:** Conexão direta com a **GitHub REST API** para consumo de dados públicos de repositórios, commits e linguagens dos usuários.
* **Gestão de Identidade e Segurança (Autenticação):** Implementação de **OAuth 2.0** utilizando o provedor oficial do GitHub (GitHub Apps ou OAuth Apps), eliminando a necessidade de armazenar senhas locais sensíveis.
* **Hospedagem/Deploy:** Deploy contínuo via Vercel ou Netlify integrado à branch `main` do GitHub.

---

## 2. Cronograma de Execução Acelerada (Sprint de 3 Dias)

Considerando o prazo limite de **14/06/2026**, o projeto será executado no seguinte ritmo:

| Data | Fase | Foco Principal |
| :--- | :--- | :--- |
| **11/06 (Hoje)** | Fase 1 e Fase 2 | Planejamento de arquitetura, criação do repositório GitHub e estrutura inicial do código. |
| **12/06** | Fase 3 e Fase 4 | Configuração de perfis de acesso, autenticação via GitHub OAuth e definição da estratégia de Git Flow. |
| **13/06** | Fase 5 | Integração final de dados, rodada de testes de segurança/permissões e correção de bugs. |
| **14/06** | Fase 6 | Revisão da documentação final, gravação do vídeo de apresentação (YouTube) e exportação do PDF para entrega até às 23h55. |

---

## 3. Evidências de Uso do Google Gemini (Apoio à Decisão)

O Google Gemini foi configurado e utilizado ativamente na Fase 1 para as seguintes tomadas de decisão:
1. **Definição do Cronograma:** Modelagem de um cronograma de contingência para execução de um projeto de 6 fases em apenas 72 horas.
2. **Escolha da Autenticação:** Recomendação do uso de GitHub OAuth em detrimento de senhas locais, visando conformidade com a LGPD e melhores práticas de segurança de dados.