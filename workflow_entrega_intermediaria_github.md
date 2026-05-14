# Workflow — Entrega Intermediária: Criação de Repositório com Versionamento

## Objetivo do workflow

Este workflow define o que deve ser feito para preparar a entrega intermediária do desafio **Criação de Repositório com Versionamento**.

A ideia é deixar o projeto local completamente organizado, documentado e validado, de forma que, ao final, esteja tudo pronto para apenas executar o `push` para o GitHub.

---

## Entregáveis esperados

Ao final deste workflow, o projeto deve conter:

- Repositório local estruturado;
- Projeto inicial criado, preferencialmente uma página web;
- Arquivos organizados em pastas;
- Arquivos `README.md` criados e formatados;
- Histórico de versionamento com Git;
- Estrutura preparada para publicação no GitHub Pages;
- Links e informações preparados para integração com LinkedIn;
- Material preparado para apresentação final;
- Tudo pronto para ser enviado ao GitHub com `git push`.

---

# 1. Planejamento do Repositório

## Objetivo da etapa

Definir previamente como o repositório será organizado, quais tipos de projetos serão incluídos e quais arquivos deverão existir antes de iniciar o versionamento.

## O que deve ser feito

### 1.1 Definir o nome do repositório

Escolha um nome claro e profissional.

Exemplos:

```text
portfolio-hub
portfolio-academico
meu-portfolio-dev
repositorio-academico
```

Nome sugerido:

```text
portfolio-hub
```

### 1.2 Definir o objetivo do repositório

O repositório deve servir como um portfólio acadêmico e profissional, reunindo projetos, documentos, slides e páginas desenvolvidas pelo estudante.

Texto-base para usar no README:

```md
Este repositório tem como objetivo reunir projetos acadêmicos e pessoais desenvolvidos durante minha formação, utilizando boas práticas de organização, documentação e versionamento com Git e GitHub.
```

### 1.3 Definir a estrutura inicial de diretórios

Criar uma estrutura simples, organizada e fácil de entender.

Estrutura recomendada:

```text
portfolio-hub/
├── README.md
├── index.html
├── assets/
│   ├── css/
│   ├── img/
│   └── js/
├── projetos-academicos/
│   └── projeto-inicial/
│       ├── README.md
│       ├── index.html
│       ├── style.css
│       └── script.js
├── projetos-pessoais/
│   └── README.md
├── documentos/
│   └── README.md
├── slides/
│   └── README.md
└── .gitignore
```

### 1.4 Definir quais seções o repositório terá

O repositório deve conter, no mínimo:

- Projetos acadêmicos;
- Projetos pessoais;
- Documentação;
- Slides;
- Página inicial do portfólio;
- README principal.

### 1.5 Criar a pasta local do projeto

No computador, criar a pasta do projeto:

```bash
mkdir portfolio-hub
cd portfolio-hub
```

---

# 2. Criação e Versionamento de Projetos

## Objetivo da etapa

Criar um projeto inicial, preparar os arquivos principais e configurar o controle de versão local com Git.

## O que deve ser feito

### 2.1 Criar o projeto inicial

O projeto inicial pode ser uma página web simples representando o portfólio.

Arquivos mínimos recomendados:

```text
index.html
assets/css/style.css
assets/js/script.js
```

### 2.2 Criar a página inicial

A página inicial deve conter:

- Nome do estudante;
- Curso ou área de estudo;
- Breve descrição profissional;
- Seção de projetos acadêmicos;
- Seção de projetos pessoais;
- Link para GitHub;
- Link para LinkedIn;
- Contato.

Exemplo de conteúdo da página:

```text
Olá, eu sou [Seu Nome].
Este é meu portfólio acadêmico e profissional, criado para reunir meus projetos, documentos e estudos desenvolvidos durante minha formação.
```

### 2.3 Criar os arquivos do projeto inicial

Criar os arquivos:

```bash
touch index.html
mkdir -p assets/css assets/js assets/img
touch assets/css/style.css
touch assets/js/script.js
```

### 2.4 Inicializar o Git

Dentro da pasta principal do projeto, executar:

```bash
git init
```

### 2.5 Criar o `.gitignore`

Criar o arquivo `.gitignore` para evitar o envio de arquivos desnecessários.

Exemplo:

```gitignore
.DS_Store
Thumbs.db
.vscode/
node_modules/
.env
```

### 2.6 Adicionar os arquivos ao controle de versão

```bash
git add .
```

### 2.7 Criar o primeiro commit

O primeiro commit deve representar a versão inicial do projeto.

```bash
git commit -m "versao 1.0 do portfolio"
```

### 2.8 Fazer alterações controladas

Depois do primeiro commit, realizar alguma melhoria no projeto, por exemplo:

- Melhorar o texto da página inicial;
- Ajustar o CSS;
- Criar novas pastas;
- Atualizar o README;
- Adicionar seção de projetos.

Depois, criar novo commit:

```bash
git add .
git commit -m "organiza estrutura inicial do repositorio"
```

### 2.9 Preparar o repositório para conexão com o GitHub

Ajustar a branch principal:

```bash
git branch -M main
```

Neste ponto, o projeto local já deve estar pronto para receber o link do repositório remoto e fazer o push.

---

# 3. Organização e Documentação do Repositório

## Objetivo da etapa

Garantir que o repositório esteja bem organizado, com pastas claras e documentação adequada em arquivos `README.md`.

## O que deve ser feito

### 3.1 Organizar os projetos em pastas

Cada projeto deve ficar em uma pasta própria.

Exemplo:

```text
projetos-academicos/
└── projeto-inicial/
    ├── README.md
    ├── index.html
    ├── style.css
    └── script.js
```

### 3.2 Criar o README principal

O arquivo `README.md` da raiz do projeto deve explicar o repositório inteiro.

Estrutura recomendada:

```md
# PortfolioHUB

## Sobre o repositório

Este repositório reúne projetos acadêmicos e pessoais desenvolvidos durante minha formação, com foco em organização, documentação e versionamento utilizando Git e GitHub.

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

## Acesso

- Repositório GitHub: [inserir link]
- GitHub Pages: [inserir link]
- LinkedIn: [inserir link]
```

### 3.3 Criar README em cada seção

Cada pasta importante deve ter um `README.md`.

Exemplo para `projetos-academicos/README.md`:

```md
# Projetos Acadêmicos

Esta pasta reúne projetos desenvolvidos em atividades acadêmicas, trabalhos de curso e exercícios práticos.
```

Exemplo para `projetos-pessoais/README.md`:

```md
# Projetos Pessoais

Esta pasta reúne projetos criados para estudo, prática e desenvolvimento de habilidades técnicas.
```

Exemplo para `documentos/README.md`:

```md
# Documentos

Esta pasta contém documentos de apoio, relatórios e materiais relacionados aos projetos.
```

Exemplo para `slides/README.md`:

```md
# Slides

Esta pasta contém apresentações utilizadas para explicar os projetos presentes no repositório.
```

### 3.4 Verificar clareza da documentação

Antes de finalizar, conferir se o README principal responde:

- Qual é o objetivo do repositório?
- Quais pastas existem?
- O que existe em cada pasta?
- Quais tecnologias foram usadas?
- Como acessar a página publicada?
- Como acessar o LinkedIn?
- Como acessar o GitHub?

### 3.5 Criar commit da documentação

```bash
git add .
git commit -m "adiciona documentacao do repositorio"
```

---

# 4. Github Pages

## Objetivo da etapa

Preparar o projeto para ser publicado no GitHub Pages.

## O que deve ser feito

### 4.1 Garantir que exista um `index.html` na raiz

O GitHub Pages pode usar o arquivo `index.html` da raiz como página principal.

Conferir se existe:

```text
portfolio-hub/index.html
```

### 4.2 Conferir se os caminhos dos arquivos estão corretos

No `index.html`, os links para CSS e JavaScript devem funcionar corretamente.

Exemplo:

```html
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/script.js"></script>
```

### 4.3 Testar a página localmente

Abrir o `index.html` no navegador e verificar:

- Se a página carrega;
- Se o CSS funciona;
- Se os links estão corretos;
- Se não existem imagens quebradas;
- Se o conteúdo está claro.

### 4.4 Preparar instrução para ativar o GitHub Pages

Depois do push para o GitHub, será necessário:

1. Entrar no repositório no GitHub;
2. Ir em `Settings`;
3. Entrar em `Pages`;
4. Em `Build and deployment`, selecionar:
   - Source: `Deploy from a branch`;
   - Branch: `main`;
   - Folder: `/root`;
5. Salvar;
6. Copiar o link gerado pelo GitHub Pages.

### 4.5 Atualizar o README com espaço para o link do GitHub Pages

No README principal, deixar o campo preparado:

```md
## GitHub Pages

A página publicada do projeto estará disponível em:

[inserir link do GitHub Pages após a publicação]
```

### 4.6 Criar commit da preparação do GitHub Pages

```bash
git add .
git commit -m "prepara projeto para publicacao no github pages"
```

---

# 5. Compartilhamento e Integração com LinkedIn

## Objetivo da etapa

Preparar o repositório para ser compartilhado publicamente e integrado ao perfil profissional do LinkedIn.

## O que deve ser feito

### 5.1 Garantir que o repositório será público

No GitHub, o repositório deverá estar como público para que possa ser acessado pela avaliação e pelo LinkedIn.

### 5.2 Preparar links que serão usados

Depois do push, será necessário separar:

```text
Link do repositório GitHub:
Link do GitHub Pages:
Link do LinkedIn:
Link do vídeo no YouTube:
```

### 5.3 Preparar texto para publicação no LinkedIn

Texto sugerido:

```text
Desenvolvi um repositório no GitHub para organizar meus projetos acadêmicos e pessoais, aplicando boas práticas de versionamento com Git, documentação em Markdown e publicação com GitHub Pages.

O objetivo é construir um portfólio profissional mais organizado e acessível.

Repositório: [inserir link]
Página publicada: [inserir link]
```

### 5.4 Preparar integração no perfil do LinkedIn

No LinkedIn, adicionar o projeto em uma das áreas:

- Seção `Projetos`;
- Seção `Destaques`;
- Publicação no feed;
- Descrição do perfil, se fizer sentido.

### 5.5 Atualizar o README com o link do LinkedIn

No README principal:

```md
## LinkedIn

Meu perfil profissional está disponível em:

[inserir link do LinkedIn]
```

### 5.6 Criar commit da preparação para compartilhamento

```bash
git add .
git commit -m "prepara links e integracao com linkedin"
```

---

# 6. Revisão Final e Apresentação

## Objetivo da etapa

Revisar todos os arquivos, preparar a apresentação final e deixar o projeto pronto para envio ao GitHub.

## O que deve ser feito

### 6.1 Revisar a estrutura final

Conferir se a estrutura está parecida com esta:

```text
portfolio-hub/
├── README.md
├── index.html
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   └── js/
│       └── script.js
├── projetos-academicos/
│   ├── README.md
│   └── projeto-inicial/
│       ├── README.md
│       ├── index.html
│       ├── style.css
│       └── script.js
├── projetos-pessoais/
│   └── README.md
├── documentos/
│   └── README.md
├── slides/
│   └── README.md
└── .gitignore
```

### 6.2 Revisar os critérios de avaliação

Conferir se o projeto atende aos critérios:

- Organização: estrutura clara do repositório;
- Documentação: README principal e READMEs por seção;
- Integração: links e preparação para LinkedIn;
- Publicação: projeto preparado para GitHub Pages;
- Apresentação: roteiro pronto para vídeo de até 5 minutos.

### 6.3 Preparar roteiro da apresentação de 5 minutos

Roteiro sugerido:

```text
1. Apresentação inicial
Olá, meu nome é [Seu Nome] e este é o meu repositório de portfólio acadêmico e profissional.

2. Objetivo do repositório
O objetivo deste repositório é reunir projetos acadêmicos e pessoais, utilizando boas práticas de organização, documentação e versionamento.

3. Estrutura do repositório
Aqui estão as principais pastas: projetos acadêmicos, projetos pessoais, documentos, slides e arquivos da página principal.

4. Versionamento com Git
O projeto foi versionado com Git, contendo commits organizados para registrar a evolução do desenvolvimento.

5. Documentação
O repositório possui um README principal e arquivos README em pastas específicas, explicando o conteúdo de cada seção.

6. GitHub Pages
A página inicial foi preparada para publicação pelo GitHub Pages.

7. Integração com LinkedIn
O repositório e a página publicada serão adicionados ao LinkedIn para compor meu perfil profissional.

8. Encerramento
Com isso, o repositório apresenta meus projetos de forma organizada, documentada e acessível.
```

### 6.4 Preparar evidências para o PDF final

Separar prints de:

- Estrutura de pastas;
- Repositório no GitHub;
- Histórico de commits;
- README principal;
- Página no GitHub Pages;
- Integração ou publicação no LinkedIn;
- Link do vídeo no YouTube.

### 6.5 Fazer verificação final no Git

Executar:

```bash
git status
```

Se existirem arquivos pendentes:

```bash
git add .
git commit -m "revisao final da entrega intermediaria"
```

### 6.6 Deixar tudo pronto para o push

Ao final, o projeto deve estar finalizado localmente.

O único passo restante deve ser conectar ao repositório remoto e enviar para o GitHub.

Comandos finais que serão executados apenas quando o repositório remoto estiver criado:

```bash
git remote add origin LINK_DO_REPOSITORIO
git push -u origin main
```

Se o remoto já tiver sido configurado:

```bash
git push
```

---

# Checklist final antes do push

Antes de enviar para o GitHub, conferir:

- [ ] O repositório local foi criado;
- [ ] A estrutura de pastas está organizada;
- [ ] Existe um `README.md` principal;
- [ ] Existem READMEs nas principais pastas;
- [ ] Existe uma página inicial `index.html`;
- [ ] O projeto inicial está criado;
- [ ] O Git foi inicializado;
- [ ] Existem commits com mensagens claras;
- [ ] O projeto está pronto para GitHub Pages;
- [ ] Os links para LinkedIn estão preparados;
- [ ] O roteiro da apresentação está pronto;
- [ ] O PDF final poderá ser montado com prints e links;
- [ ] O projeto está pronto para apenas executar o `push`.

---

# Comandos principais resumidos

```bash
mkdir portfolio-hub
cd portfolio-hub

git init

mkdir -p assets/css assets/js assets/img
mkdir -p projetos-academicos/projeto-inicial
mkdir -p projetos-pessoais documentos slides

touch README.md
touch index.html
touch assets/css/style.css
touch assets/js/script.js
touch .gitignore
touch projetos-academicos/README.md
touch projetos-academicos/projeto-inicial/README.md
touch projetos-academicos/projeto-inicial/index.html
touch projetos-academicos/projeto-inicial/style.css
touch projetos-academicos/projeto-inicial/script.js
touch projetos-pessoais/README.md
touch documentos/README.md
touch slides/README.md

git add .
git commit -m "versao 1.0 do portfolio"

git add .
git commit -m "organiza estrutura e documentacao"

git branch -M main

# Executar apenas depois de criar o repositório no GitHub:
git remote add origin LINK_DO_REPOSITORIO
git push -u origin main
```

---

# Resultado esperado

Ao concluir este workflow, o projeto estará totalmente preparado localmente, com estrutura, documentação, página inicial e commits organizados.

Depois disso, basta criar o repositório no GitHub, conectar o remoto e executar o `push`.
