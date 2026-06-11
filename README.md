# PortfolioHUB 🚀

Bem-vindo ao **PortfolioHUB**, uma plataforma de portfólio acadêmico e profissional centralizada, moderna e totalmente responsiva. Este projeto foi desenvolvido como parte do Desafio Final de Implantação, unindo tecnologias front-end nativas e inteligência artificial (Google Gemini) como ferramenta de apoio estratégico.

## 🌐 Link de Acesso Público (Live Demo)
Explore o projeto em tempo real através do GitHub Pages:
👉 **[https://kauan9r7.github.io/Portifolio_academico/](https://kauan9r7.github.io/Portifolio_academico/)**

---

## 🛠️ Recursos e Funcionalidades do Projeto

O PortfolioHUB foi construído utilizando práticas modernas de desenvolvimento web e arquitetura resiliente:

1. **Integração Dinâmica com GitHub API:** * Consome de forma assíncrona (`fetch` no JavaScript) os repositórios públicos do usuário `Kauan9r7`, injetando os dados diretamente no DOM.
   * **Mecanismo de Resiliência (Anti-Rate Limit):** Possui um sistema de fallback automático (`try/catch`). Se a API do GitHub atingir o limite de requisições por IP, o sistema intercepta o erro e carrega uma lista de contingência local estruturada, garantindo que o site nunca fique indisponível para o avaliador.

2. **Gestão de Usuários e Segurança (Simulação RBAC):**
   * Apresenta um painel de controle interativo para alternar perfis entre **Administrador** e **Convidado**.
   * A interface reage dinamicamente, liberando recursos avançados e áreas restritas apenas para perfis autorizados (Admin), demonstrando conceitos práticos de governança de acesso no front-end.

3. **Hub de Conexão Profissional (LinkedIn):**
   * Ponto de contato estratégico integrado à interface para direcionar visitantes e recrutadores ao perfil profissional do desenvolvedor: [LinkedIn - Cauan Bastos](https://www.linkedin.com/in/cauan-bastos-202389400/).

---

## 📂 Estrutura Hierárquica do Repositório

O projeto segue uma arquitetura limpa, contendo os arquivos de aplicação e todo o histórico de documentação exigido pelas fases do desafio:

```text
Portifolio_academico/
├── index.html               # Interface de usuário principal (HTML5)
├── style.css                # Estilização moderna e responsiva (CSS3)
├── script.js                # Lógica da API, tratamento de falhas e controle de acesso (JS)
├── .gitignore               # Proteção contra envio de arquivos temporários
└── desenvolvimento_docs
    ├── fase1_planejamento.md    # Documentação de planejamento do projeto
    ├── fase2_integracao.md      # Registro técnico das integrações (GitHub + LinkedIn)
    ├── fase3_seguranca.md       # Políticas de controle de acesso e resiliência da API
    ├── fase4_colaboracao.md     # Estratégia de versionamento, branches e governança
    └── fase5_testes.md          # Relatório completo e matriz de validação de testes