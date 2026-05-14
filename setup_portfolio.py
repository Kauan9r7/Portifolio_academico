import os

base_dir = r"c:\Users\cauan\Documents\Portfolio_academico\portfolio-hub"
os.makedirs(base_dir, exist_ok=True)
os.chdir(base_dir)

print("Git not found. Skipping git init.")

dirs_phase1 = [
    "assets/css",
    "assets/js",
    "assets/img",
]
for d in dirs_phase1:
    os.makedirs(d, exist_ok=True)

files_phase1 = {
    "index.html": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfólio - Cauan</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header>
        <h1>Cauan</h1>
        <p>Estudante - Portfólio Acadêmico e Profissional</p>
    </header>
    <main>
        <section>
            <h2>Sobre Mim</h2>
            <p>Olá, eu sou Cauan.</p>
            <p>Este é meu portfólio acadêmico e profissional, criado para reunir meus projetos, documentos e estudos desenvolvidos durante minha formação.</p>
        </section>
        
        <section>
            <h2>Projetos Acadêmicos</h2>
            <ul>
                <li><a href="projetos-academicos/projeto-inicial/index.html">Projeto Inicial</a></li>
            </ul>
        </section>

        <section>
            <h2>Projetos Pessoais</h2>
            <p>Em breve...</p>
        </section>
    </main>
    <footer>
        <p>Contato</p>
        <ul>
            <li><a href="#">GitHub</a></li>
            <li><a href="#">LinkedIn</a></li>
        </ul>
    </footer>
    <script src="assets/js/script.js"></script>
</body>
</html>""",
    "assets/css/style.css": """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

header {
    background-color: #333;
    color: #fff;
    padding: 2rem 0;
    text-align: center;
}

main {
    padding: 2rem;
    max-width: 800px;
    margin: auto;
}

section {
    margin-bottom: 2rem;
}

footer {
    background-color: #f4f4f4;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}""",
    "assets/js/script.js": """console.log("Portfólio carregado com sucesso!");""",
    ".gitignore": """.DS_Store
Thumbs.db
.vscode/
node_modules/
.env"""
}

for path, content in files_phase1.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

dirs_phase2 = [
    "projetos-academicos/projeto-inicial",
    "projetos-pessoais",
    "documentos",
    "slides",
]
for d in dirs_phase2:
    os.makedirs(d, exist_ok=True)

files_phase2 = {
    "README.md": """# PortfolioHUB

## Sobre o repositório

Este repositório tem como objetivo reunir projetos acadêmicos e pessoais desenvolvidos durante minha formação, utilizando boas práticas de organização, documentação e versionamento com Git e GitHub.

## Estrutura do repositório

- `projetos-academicos/`: projetos desenvolvidos em atividades acadêmicas;
- `projetos-pessoais/`: projetos criados para estudo e prática;
- `documentos/`: documentos de apoio e registros;
- `slides/`: apresentações relacionadas aos projetos;
- `assets/`: arquivos de estilo, imagens e scripts usados na página principal.

## Tecnologias utilizadas

- HTML;
- CSS;
- JavaScript;
- Git;
- GitHub;
- GitHub Pages.

## Projetos incluídos

### Projeto Inicial — Página de Portfólio

Página web criada para apresentar o portfólio acadêmico e profissional.

## GitHub Pages

A página publicada do projeto estará disponível em:

[inserir link do GitHub Pages após a publicação]

## LinkedIn

Meu perfil profissional está disponível em:

[inserir link do LinkedIn]

## Acesso

- Repositório GitHub: [inserir link]
- GitHub Pages: [inserir link]
- LinkedIn: [inserir link]""",
    "projetos-academicos/README.md": """# Projetos Acadêmicos\n\nEsta pasta reúne projetos desenvolvidos em atividades acadêmicas, trabalhos de curso e exercícios práticos.""",
    "projetos-pessoais/README.md": """# Projetos Pessoais\n\nEsta pasta reúne projetos criados para estudo, prática e desenvolvimento de habilidades técnicas.""",
    "documentos/README.md": """# Documentos\n\nEsta pasta contém documentos de apoio, relatórios e materiais relacionados aos projetos.""",
    "slides/README.md": """# Slides\n\nEsta pasta contém apresentações utilizadas para explicar os projetos presentes no repositório.""",
    "projetos-academicos/projeto-inicial/index.html": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Inicial</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Bem-vindo ao Projeto Inicial</h1>
    <p>Este é o primeiro projeto acadêmico do repositório.</p>
    <script src="script.js"></script>
</body>
</html>""",
    "projetos-academicos/projeto-inicial/style.css": """body {
    font-family: Arial, sans-serif;
    padding: 20px;
}""",
    "projetos-academicos/projeto-inicial/script.js": """console.log("Projeto Inicial carregado.");""",
    "projetos-academicos/projeto-inicial/README.md": """# Projeto Inicial\n\nPágina inicial simples para estruturação do repositório de portfólio."""
}

for path, content in files_phase2.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done creating structure.")
