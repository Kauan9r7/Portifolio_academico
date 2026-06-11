document.addEventListener("DOMContentLoaded", () => {
    const username = "Kauan9r7";
    const projectsContainer = document.getElementById("github-projects");
    const loadingElement = document.getElementById("loading");

    async function fetchGitHubRepos() {
        try {
            const response = await fetch(`https://api.github.com/users/${username}/repos`);
            if (!response.ok) throw new Error("Erro ao buscar repositórios");
            
            const repos = await response.json();
            loadingElement.style.display = "none";

            // Filtra para remover bifurcações (forks) se preferir mostrar apenas os seus originais
            const myRepos = repos.filter(repo => !repo.fork);

            if (myRepos.length === 0) {
                projectsContainer.innerHTML = "<p>Nenhum repositório público encontrado.</p>";
                return;
            }

            myRepos.forEach(repo => {
                const card = document.createElement("div");
                card.className = "project-card";

                card.innerHTML = `
                    <div>
                        <h3>${repo.name}</h3>
                        <p>${repo.description || "Sem descrição disponível."}</p>
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

        } catch (error) {
            console.error(error);
            loadingElement.innerText = "Falha ao carregar repositórios do GitHub.";
        }
    }

    fetchGitHubRepos();
});