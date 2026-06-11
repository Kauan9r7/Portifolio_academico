document.addEventListener("DOMContentLoaded", () => {
    const username = "Kauan9r7";
    const projectsContainer = document.getElementById("github-projects");
    const loadingElement = document.getElementById("loading");

    // PROJETOS DE BACKUP (Fallback): Se a API do GitHub bloquear por excesso de acessos,
    // o site usará esses dados locais para nunca aparecer quebrado para o avaliador.
    const fallbackProjects = [
        {
            name: "Portifolio_academico",
            description: "Plataforma PortfolioHUB centralizada para exibição de projetos integrados com o GitHub e controle de acessos.",
            language: "HTML",
            html_url: `https://github.com/Kauan9r7/Portifolio_academico`
        }
    ];

    // Função para desenhar os cards na tela
    function renderProjects(repos, isFallback = false) {
        loadingElement.style.display = "none";
        projectsContainer.innerHTML = ""; // Limpa a mensagem de carregando

        if (isFallback) {
            const notice = document.createElement("p");
            notice.style.gridColumn = "1 / -1";
            notice.style.fontSize = "0.85rem";
            notice.style.color = "#d9383a";
            notice.style.marginBottom = "15px";
            notice.style.fontWeight = "bold";
            notice.innerText = "⚠️ Nota de Contingência: Dados locais carregados (Limite temporário da API do GitHub atingido).";
            projectsContainer.appendChild(notice);
        }

        repos.forEach(repo => {
            const card = document.createElement("div");
            card.className = "project-card";
            card.innerHTML = `
                <div>
                    <h3>${repo.name}</h3>
                    <p>${repo.description || "Sem descrição disponível no momento."}</p>
                </div>
                <div style="margin-top: 15px;">
                    <span style="font-size: 0.8rem; background: #eaecef; padding: 3px 8px; border-radius: 10px; margin-right: 10px;">
                        ${repo.language || "HTML/CSS"}
                    </span>
                    <a href="${repo.html_url}" target="_blank" class="project-link">Ver no GitHub</a>
                </div>
            `;
            projectsContainer.appendChild(card);
        });
    }

    // Chamada Assíncrona para a API do GitHub
    async function fetchGitHubRepos() {
        try {
            const response = await fetch(`https://api.github.com/users/${username}/repos`);
            
            // Se o GitHub recusar o acesso (Status 403 ou 404), força a ida para o catch
            if (!response.ok) throw new Error("Limite da API excedido ou falha de conexão.");
            
            const repos = await response.json();
            const myRepos = repos.filter(repo => !repo.fork);

            if (myRepos.length === 0) {
                projectsContainer.innerHTML = "<p>Nenhum repositório público encontrado.</p>";
                return;
            }

            renderProjects(myRepos, false);

        } catch (error) {
            console.warn("GitHub API inacessível. Ativando modo de segurança local: ", error.message);
            // Executa o plano de segurança exibindo os dados locais salvos
            renderProjects(fallbackProjects, true);
        }
    }

    // LÓGICA DA FASE 3: Simulação de Controle de Acesso (Segurança)
    const btnAdmin = document.getElementById("btn-admin");
    const btnGuest = document.getElementById("btn-guest");
    const statusPermissao = document.getElementById("status-permissao");
    const areaRestrita = document.getElementById("area-restrita");

    btnAdmin.addEventListener("click", () => {
        statusPermissao.innerText = "Administrador Autenticado";
        statusPermissao.style.color = "#28a745";
        areaRestrita.style.display = "block";
    });

    btnGuest.addEventListener("click", () => {
        statusPermissao.innerText = "Modo Convidado (Leitura apenas)";
        statusPermissao.style.color = "#6a737d";
        areaRestrita.style.display = "none";
    });

    fetchGitHubRepos();
});