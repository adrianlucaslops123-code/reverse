# CDC_SITE_MASTER_SPECIFICATION

Especificação técnica e visual completa do site da **CDC Capacitação em Qualidade**, produzida por engenharia reversa do site publicado e do seu código-fonte. É um documento **independente**: com ele, a biblioteca (`CDC_DESIGN_LIBRARY/`), o Design System (`CDC_DESIGN_SYSTEM.md`) e os recursos originais (`ASSETS_INVENTORY.md`), um desenvolvedor ou uma IA consegue reconstruir o site sem depender de outra explicação.

| Item | Valor |
|---|---|
| Site analisado | https://cdc-cursos-kappa.vercel.app/ (Vercel) |
| Código-fonte | https://github.com/adrianlucaslops123-code/landing-page-cdc · branch padrão · commit `65c37e7` ("Adiciona três vídeos à área comum de vídeos", 3 nov. 2026, 00:49 UTC) |
| Correspondência código ↔ site | o `<body>` do `index.html` publicado é **idêntico** ao do repositório (comparação linha a linha). Só mudam as referências de CSS/JS do *build* |
| Data da análise | 3 e 4 nov. 2026 (navegador em 3 nov.; teste de *build* em 4 nov.) |
| Método | leitura integral do código (`index.html`, 10 arquivos CSS, 20 módulos JS, `vite.config.js`, `package.json`, `package-lock.json`, README) + verificação no navegador (Chromium headless via Playwright: 1440×900, 1280×720, 1024×768, 768×1024, 2560×1440, iPhone 13 e movimento reduzido) + *build* refeito fora da Vercel, idêntico byte a byte ao publicado |
| Restrição | análise e documentação apenas. **Nada foi alterado** no site, no repositório `landing-page-cdc` nem na hospedagem |

Legenda de confiabilidade (vale para todo o documento): **EXATO** (código) · **CALCULADO** (fórmula do código) · **OBSERVADO** (medido no site) · **ESTIMATIVA** · **NÃO IDENTIFICADO**. Valores sem marca são EXATOS.

---

## 1. Visão geral do projeto

**O que é:** a página única (*one-page*) de vendas e apresentação da CDC, um centro de treinamento para **Inspetor de Soldagem Nível 1** no Maracanã, Rio de Janeiro, que existe desde 2005, a um quarteirão do SENAI de solda e a 10 minutos da FBTS. A página também abriga uma **área do aluno própria** (biblioteca de PDFs com leitor, busca e vídeos) que abre por cima dela.

**Proposta de experiência:** "o mundo da solda vista pela máscara". Palco escuro de oficina, onde a luz do arco, da brasa e do metal fundido é o elemento gráfico. O logotipo vira **metal de partículas** que o visitante aquece com o mouse (como um maçarico) e "abre o arco" com o clique. A rolagem é desenhada como um **cordão de solda**. As provas da certificação são contadas uma a uma, numa cena presa com ilustrações técnicas animadas.

**Público:** profissionais que vão prestar as provas de qualificação ou recertificação de Inspetor de Soldagem N1 (FBTS/SENAI).

**Objetivos comerciais na página:** levar ao agendamento com a Rose pelo WhatsApp (botões, formulário de pré-inscrição e botão flutuante), à compra do curso semipresencial (Kiwify) e ao uso da área do aluno e do aplicativo CDC.

**Tecnologia (resumo):** HTML + CSS + JavaScript puro (ES Modules), empacotado com **Vite 8**. Bibliotecas: **GSAP 3.15** (com ScrollTrigger, SplitText, ScrambleText), **Lenis 1.3** (rolagem suave), **three.js 0.186** (logo de partículas WebGL) e **pdf.js 5.7** (leitor). Sem framework de componentes, sem backend, sem banco de dados. Detalhes em `TECHNICAL_DEPENDENCIES.md`.

**Importante sobre plataformas:** este site **não usa Lovable Cloud nem Supabase**. Ele é estático e está publicado na Vercel. O único vínculo com o Lovable é um **link externo** para o aplicativo separado `https://cdc-capacita-o-em-qualidade.lovable.app/` (botão "Conhecer o aplicativo"). Ver §14.

---

## 2. Identidade visual

- **Tema único escuro**: fundo `#07090c` (aço), superfícies `#0d1116` e `#141a21`, contornos de 1 px em azul-acinzentado translúcido.
- **Cor da marca**: laranja de brasa `#fb781e` (do logo), com brasa clara `#ffb24a`, brasa escura `#c2410c` e dourado da placa `#c99f53`.
- **Acento frio**: azul do arco elétrico `#a8d8ff` (foco, clarão).
- **Assinatura**: gradiente de revenimento (palha `#d9b46a` → bronze `#a8632e` → roxo `#6c4f9e` → azul `#3f72d4`) em filetes, sublinhados e no cordão de progresso.
- **Tipografia de chapa industrial**: Archivo expandida e pesada nos títulos, Instrument Sans no texto, IBM Plex Mono em caixa alta nos rótulos técnicos.
- **Textura**: grão de filme sobre tudo (7 %), vinheta no hero e fotos com gradação fria/quente.
- **Logotipo** "CDC" em script, sempre aplicado como **máscara** (`public/marca/cdc-mascara.png`, 1400 × 717), pintado de laranja, de metal fundido ou feito de partículas.
- **Tom de voz**: direto, técnico e próximo ("Quem treina você já passou pelas mesmas provas.", "É só enviar.", "Fale com a Rose").

Detalhamento em `CDC_DESIGN_SYSTEM.md` §1–2.

---

## 3. Design System

Documento próprio: **`CDC_DESIGN_SYSTEM.md`** (tokens, escalas, estados, sombras, componentes, *motion*, responsividade, camadas e regras para novos componentes). Resumo dos tokens (`src/estilo/tokens.css`):

```css
:root {
  color-scheme: dark;
  --aco-0: #07090c; --aco-1: #0d1116; --aco-2: #141a21; --aco-3: #1d252e;
  --fio: rgba(168, 194, 222, 0.12); --fio-forte: rgba(168, 194, 222, 0.22);
  --texto: #eef1f4; --texto-2: #a3adb8; --texto-3: #6b7682;
  --brasa: #fb781e; --brasa-quente: #ffb24a; --brasa-escura: #c2410c; --brasa-texto: #1a0a02; --ouro: #c99f53;
  --arco: #a8d8ff;
  --revenido-palha: #d9b46a; --revenido-bronze: #a8632e; --revenido-roxo: #6c4f9e; --revenido-azul: #3f72d4;
  --revenido: linear-gradient(90deg, var(--revenido-palha), var(--revenido-bronze) 30%, var(--revenido-roxo) 62%, var(--revenido-azul));
  --display: 'Archivo', 'Arial Narrow', 'Helvetica Neue', sans-serif;
  --ui: 'Instrument Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --mono: 'IBM Plex Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace;
  --t-mega: clamp(52px, 10.4vw, 176px); --t-h2: clamp(38px, 5.8vw, 96px); --t-h2-menor: clamp(32px, 4.2vw, 68px);
  --t-h3: clamp(21px, 1.8vw, 28px); --t-corpo: 17px; --t-pequeno: 14px; --t-mono: 12px;
  --gutter: max(16px, min(5vw, 64px)); --largura: 1240px;
  --r-pilula: 999px; --r-cartao: 18px; --r-botao: 12px; --r-peca: 10px;
  --entrada: cubic-bezier(0.16, 1, 0.3, 1); --saida: cubic-bezier(0.55, 0, 0.75, 0.2);
  --mola: cubic-bezier(0.34, 1.4, 0.64, 1); --suave: cubic-bezier(0.65, 0, 0.35, 1);
  --vidro: rgba(20, 26, 33, 0.62); --vidro-forte: rgba(14, 18, 24, 0.86); --desfoque: blur(18px) saturate(1.25);
}
```

Definidos e **não usados**: `--aco-3`, `--t-mega`, `--saida`.

---

## 4. Tipografia

- **Archivo** (variável: largura 62–125 %, peso 100–900): todos os títulos, números, preços, nomes, menu, lema e fecho. Pesos usados: 600, 640, 650, 660, 680, 700, 720, 740, 750, 760, 780, 800, 820. Larguras usadas: 102, 104, 106, 108, 110, 112, 116 e 125 % (o fecho anima de 62 a 116 %).
- **Instrument Sans** (variável: largura 75–100 %, peso 400–700): corpo de 17 px / 1,55, botões (600), links, campos (16 px), enunciados.
- **IBM Plex Mono** (400, 500): rótulos (12 px, 0,14 em, caixa alta), selos, tags, contadores, legendas técnicas, metadados, cursor (10 px).
- Hierarquia completa, escala por largura de tela e tamanhos medidos: `CDC_DESIGN_SYSTEM.md` §3.
- Animações tipográficas: fichas TIP-01 a TIP-07.

---

## 5. Paleta de cores

Tabelas completas (tokens, aplicações, contagem de usos, contraste WCAG e cores literais): `CDC_DESIGN_SYSTEM.md` §2. Principais contrastes (CALCULADO): texto `#eef1f4` sobre `#07090c` = 17,58:1 · `#a3adb8` = 8,76:1 · `#6b7682` = 4,31:1 · brasa `#fb781e` sobre `#07090c` = 7,41:1 · texto do botão `#1a0a02` sobre `#fb781e` = 7,17:1.

---

## 6. Componentes

| Componente | Classe(s) | Onde | Ficha / seção |
|---|---|---|---|
| Abertura (cortina de metal fundido) | `.carga` | sobre tudo, ao carregar | CAR-01 |
| Grão de filme | `.grao` | página inteira | FUN-01 |
| Cursor próprio + rótulo | `.cursor`, `[data-cursor]` | computador | CUR-01, CUR-02 |
| Cordão de solda (progresso) | `.cordao` | borda direita | ROL-01 |
| Barra de navegação | `.nav` | topo fixo | ROL-03 |
| Menu de tela cheia | `.menu`, `.menu-botao` | ≤ 1080 px | CEN-07 |
| Botões | `.botao`, `--brasa`, `--vidro`, `--grande` | todas as seções | BOT-01 a BOT-03 |
| Botão de som | `.som` | barra | BOT-05, SOM-01 |
| Logo pintável | `.logo`, `.logo--fundido` | barra, rodapé, portal, app | TIP-07 |
| Selo | `.selo` | hero | FUN-04 |
| Rótulo de seção | `.rotulo` | início de cada seção | FUN-04 |
| Título de seção | `.titulo`, `.titulo--menor` | seções | TIP-01 |
| Números | `.numeros`, `.numero` | A CDC | TIP-04 |
| Credencial | `.credencial` | Equipe | CRT-01 |
| Plano | `.plano`, `.plano--destaque` | Treinamentos | CRT-01 |
| Prova | `.prova`, `.prova__fig`, `.ilus` | Prova por prova | CEN-01, CEN-02 |
| Recurso | `.recurso` | Material, Estrutura | CRT-01 |
| Rota | `.rota` | Estrutura | CEN-04 |
| Fita de fotos | `.filme` | Estrutura | CEN-03 |
| Depoimento | `.falas`, `.fala` | Depoimentos | CEN-05 |
| Acesso | `.acesso` | Área do aluno | CUR-02, CRT-01 |
| Estante | `.estante__item` | Área do aluno | CEN-10 |
| Pergunta | `.pergunta` | Dúvidas | CEN-06 |
| Janela de app + questão | `.janela-app`, `.questao`, `.opcao`, `.retorno` | Aplicativo | CEN-09 |
| Fecho | `.contato__titulo` | Contato | TIP-06, TIP-07 |
| Brasas | `.contato__palco canvas` | Contato | FUN-02 |
| Pré-inscrição | `.inscricao` | Contato | CEN-08 |
| Canal + copiar | `.canal`, `.copiar` | Contato | BOT-06 |
| Rodapé | `.rodape` | fim | Design System §7.2 |
| WhatsApp flutuante | `.zap` | canto inferior direito | BOT-04 |
| Redes sociais | `.redes-canto`, `.redes-linha`, `.redes-popup` | canto, rodapé, pop-up | CEN-13 |
| Aviso | `.aviso` | embaixo, centro | BOT-06 |
| Portal + biblioteca + leitor + vídeos | `.portal`, `.biblioteca`, `.leitor`, `.videos` | camada sobre a página | CEN-10 a CEN-12 |

---

## 7. Estrutura da página (ordem real, de cima para baixo)

Há **uma única página** (`index.html`). Não há roteador de páginas. Âncoras (`#id`) levam às seções, e *hashes* especiais abrem o portal (§12).

| # | Elemento | `id` | Rótulo | Layout (computador) | Altura observada em 1440×900 |
|---|---|---|---|---|---|
| — | link "pular" | n/a | n/a | escondido até receber foco | n/a |
| — | abertura `.carga` | n/a | n/a | tela cheia, removida no fim | n/a |
| 01 | **Hero** | `inicio` | n/a | texto à esquerda (até 600 px), logo de partículas à direita (centro em 69 %), lema sob o logo, dica embaixo à direita, "Role" no centro. **Preso por 1 tela** | 900 + 900 de trava |
| 02 | **A CDC** (manifesto) | `a-cdc` | 01 A CDC | manifesto em largura de 26ch + grade de 4 números | 1 111 |
| 03 | **Nossa equipe** | `equipe` | 02 Nossa equipe | título + 2 credenciais lado a lado | 938 |
| 04 | **Treinamentos e valores** | `treinamentos` | 03 Treinamentos e valores | título, introdução, 3 planos (`1.15fr 1fr 1fr`) | 1 293 |
| 05 | **Prova por prova** | `provas` | 04 Prova por prova | cena presa: cabeça + contador, prova ativa (texto / figura), índice de 8 no rodapé | 5 940 (com trava) |
| 06 | **Material oferecido** | `material` | 05 Material oferecido | título + 3 recursos | 963 |
| 07 | **Estrutura e hospedagem** | `estrutura` | 06 Estrutura e hospedagem | texto + rota (`1.1fr / 0.9fr`), 2 recursos, fita de 10 fotos (presa e horizontal) | 4 912 (com trava) |
| 08 | **Depoimentos** | `depoimentos` | 07 Depoimentos | carrossel de 3 falas + controles | 886 |
| 09 | **Área do aluno** | `area-do-aluno` | 08 Área do aluno | título, introdução, busca, 3 acessos, estante de 3 materiais | 920 |
| 10 | **Dúvidas** | `duvidas` | 09 Dúvidas | título à esquerda, 6 perguntas à direita | 733 |
| 11 | **Aplicativo** | `aplicativo` | 10 Aplicativo | apresentação + botão à esquerda, janela do app à direita | 950 |
| 12 | **Contato** | `contato` | n/a | fecho em 3 linhas + formulário e canais (2 colunas), brasas ao fundo | 1 298 |
| — | **Rodapé** | n/a | n/a | logo fundido, 3 colunas, linha legal, crédito | 711 |
| — | flutuantes | n/a | n/a | WhatsApp (direita), redes (esquerda), cordão (direita, centro), aviso | n/a |
| — | **Portal** | `portal` | n/a | camada fixa: topo + biblioteca ou leitor | n/a |
| — | pop-up de redes | n/a | n/a | `dialog` modal | n/a |

Altura total do documento: **22 456 px** em 1440×900 (21 556 px roláveis); **17 445 px** com movimento reduzido (sem travas). **OBSERVADO.**

Ordem dos elementos no `<body>`: `a.pular` · `div.carga` · `div.grao` · `div.cursor` · `div.cordao` · `header.nav` · `div.menu#menu` · `main` (seções 01–12) · `footer.rodape` · `a.zap` · `div.portal#portal` · `nav.redes-canto` · `dialog.redes-popup` · `div.aviso` · script.

### 7.1 `<head>` (literal)

- `<html lang="pt-BR">`, `charset UTF-8`, `viewport: width=device-width, initial-scale=1, viewport-fit=cover`.
- `<title>CDC Capacitação em Qualidade</title>`
- `description`: "Treinamento para Inspetor de Soldagem Nível 1 no Rio de Janeiro. Preparação para as provas de qualificação e recertificação da FBTS, desde 2005, a um quarteirão do SENAI de solda no Maracanã."
- `theme-color`: `#07090c`
- `og:title`: "CDC Capacitação em Qualidade" · `og:description`: "Treinamento para Inspetor de Soldagem Nível 1. Desde 2005 no Maracanã, Rio de Janeiro." · `og:image`: `./og.jpg` (1200 × 630)
- Ícones: `./marca/favicon.png` (64 × 64), `./marca/apple-touch-icon.png` (180 × 180)
- `preconnect` para `fonts.googleapis.com` e `fonts.gstatic.com`, folha do Google Fonts (§4)
- Script inline no `<head>`: `document.documentElement.classList.add('js')` e, se `matchMedia('(hover: none)')`, `classList.add('toque')`.

---

## 8. Conteúdo institucional (textos literais)

> Redação **original**, copiada do `index.html` e dos arquivos JS. Não reescrever. Quebras de linha de formatação foram removidas. "↗", "→" e "←" fazem parte dos rótulos.

### 8.1 Navegação

- Logo: link para `#inicio`, `aria-label` "CDC, voltar ao início".
- Links: **A CDC** (`#a-cdc`) · **Treinamentos** (`#treinamentos`) · **Provas** (`#provas`) · **Estrutura** (`#estrutura`) · **Depoimentos** (`#depoimentos`) · **Contato** (`#contato`).
- Botão de som (`aria-label` "Ligar o som da página" / "Desligar o som da página").
- **Área do aluno** (`#area-do-aluno`) · **Inscreva-se** (`#treinamentos`).
- Menu do celular: `01` A CDC · `02` Treinamentos · `03` Provas · `04` Estrutura · `05` Depoimentos · `06` Área do aluno · `07` Contato. Rodapé do menu: "WhatsApp (21) 98257-0418" (`https://wa.me/5521982570418?text=Olá, Rose! Vim pelo site da CDC.`).
- Link de acessibilidade: "Pular para os treinamentos".

### 8.2 Abertura

"CDC · Capacitação em Qualidade" · contador "000".

### 8.3 Hero (`#inicio`)

- Lema (sob o logo): **Capacitação em qualidade**
- Selo: **Inspetor de Soldagem N1 · FBTS**
- H1: **Treinamento para Inspetor de Soldagem Nível 1**
- Texto: "Preparação para as provas de qualificação e recertificação, com instrutores certificados pela FBTS e pelo SENAI, material similar ao da prova e um centro de treinamento a um quarteirão do SENAI de solda, no Maracanã."
- Botões: **Ver treinamentos e valores** (`#treinamentos`) · **Agendar com a Rose** (ícone do WhatsApp; `https://wa.me/5521982570418?text=Olá, Rose! Quero agendar meu treinamento na CDC.`)
- Dica (mouse): "Passe o mouse para aquecer o metal · clique para abrir o arco" · (toque): "Toque no logo para abrir o arco"
- Indicador: "Role"

### 8.4 01 · A CDC (`#a-cdc`)

- Título acessível (oculto): "Sobre a CDC"
- Manifesto: "Desde 2005, a CDC prepara inspetores de soldagem para as provas de qualificação. Nossos instrutores já fizeram essas provas, o material é similar ao que você vai encontrar no dia e o método trabalha os pontos que mais levam à reprovação."
- Números:
  - **2005** · "Ano em que a CDC começou a preparar inspetores" (conta a partir de 1990)
  - **95%** · "De aprovação na prova de acompanhamento de soldagem"
  - **99%** · "De aprovação na prova de estufas e consumíveis"
  - **10min** · "Do centro de treinamento até a FBTS"

### 8.5 02 · Nossa equipe (`#equipe`)

- Título: **Quem treina você já passou pelas mesmas provas.**
- Credencial 1 · "Instrutor" · **Deiwson Ribeiro** · "Responsável pelo treinamento teórico. Criou o passo a passo de acompanhamento de soldagem usado na CDC." · registros: **IS 1429 N1** FBTS · **IS 1423 N1** SENAI
- Credencial 2 · "Instrutora" · **Rozilene Ribeiro (Rose)** · "Inspetora de Soldagem Nível 1, certificada pela FBTS e pelo SENAI. É com ela que você agenda o seu treinamento." · registros: **IS 8176 N1** FBTS · **IS 1426 N1** SENAI

### 8.6 03 · Treinamentos e valores (`#treinamentos`)

- Título: **Escolha como você quer se preparar.**
- Introdução: "O agendamento é feito com a Rose, de acordo com a disponibilidade do calendário e a agenda dos instrutores."
- **Plano em destaque** · tag "Semipresencial" · **Curso Inspetor de Soldagem Nível 1** · "Aulas gravadas, on-line e presenciais. Acesso válido por 6 meses." · preço **R$ 2.200** · "À vista ou parcelado no cartão de crédito" · lista: "Professores certificados pela FBTS e pelo SENAI" · "Salas de aula confortáveis e ambientadas para as aulas práticas" · "Material didático similar ao utilizado na prova" · "Instrumentos e equipamentos similares aos utilizados na prova" · "Ambiente calmo e tranquilo, próximo ao local da prova" · botões: **Comprar o curso** (`https://pay.kiwify.com.br/b2fQ0VB`) · **Tirar dúvidas** (`https://wa.me/5521982570418?text=Olá, Rose! Tenho uma dúvida sobre o Curso Inspetor de Soldagem Nível 1.`)
- **Plano 2** · tag "8 h por dia com instrutor" · **Treinamento para Qualificação de Inspetor de Soldagem** · "Documentos técnicos + tratamento térmico" **R$ 900** · *2 dias* · "Dureza, inspeção de eletrodo, estufa, acompanhamento de soldagem e inspeção visual" **R$ 550** · *por diária de retreinamento · sugerimos 4 dias* · botão **Agendar com a Rose** (`?text=Olá, Rose! Quero agendar o Treinamento para Qualificação de Inspetor de Soldagem.`)
- **Plano 3** · tag "Nova formatação" · **Treinamento para Recertificação Nível 1** · "Disciplinas: visual de ajuste de junta, inspeção durante a soldagem e visual final de solda." · "Recertificação" **R$ 1.100** · *2 dias* · "Recertificação" **R$ 1.650** · *3 dias* · botão **Agendar com a Rose** (`?text=Olá, Rose! Quero agendar o Treinamento para Recertificação Nível 1.`)

### 8.7 04 · Prova por prova (`#provas`)

- Título: **Cada prova tem um método.** · contador "01 / 08" · índice: Teórica · Documentos técnicos · Tratamento térmico · Acompanhamento de soldagem · Visual e dimensional · Dureza · Estufas e consumíveis · Recertificação

| Nº | Título | Texto | Nota / dado | Legenda da figura |
|---|---|---|---|---|
| 01 | Teórica | "O professor Deiwson Ribeiro, responsável pelo treinamento teórico, trabalha com você os capítulos em que você tem mais dificuldade. Treinamento teórico não é só resolver questões: é mostrar como raciocinar para resolver as questões da prova, explicando o conteúdo." | "Banco de questões por dois meses, num sistema parecido com o da prova. Para liberar login e senha e ver os valores, fale com a gente." ("fale com a gente" → `#contato`) | Simulados no nível da prova |
| 02 | Documentos técnicos | "A prova tem dois exercícios: um para verificar o desempenho dos soldadores e outro para verificar a qualificação. Elaboramos um método que trabalha os pontos que mais levam à reprovação, por isso nossos alunos têm facilidade nessa prova." | "Já existe CEQUAL aplicando esta prova no computador, como a prova teórica. Fique atento." | Leitura de documentos e símbolos |
| 03 | Tratamento térmico | "A CDC criou um método de ensino que facilita o aprendizado e aumenta a sua velocidade na análise dos gráficos de tratamento térmico, porque o tempo de execução da prova é um dos fatores que podem atrapalhar a aprovação." | n/a | Análise rápida dos gráficos |
| 04 | Acompanhamento de soldagem | "O Deiwson desenvolveu um passo a passo que facilita a memorização de todos os itens que devem ser verificados antes, durante e depois da soldagem. Nosso procedimento é semelhante ao do CEQUAL, o que dá ao aluno tranquilidade na hora da prova." | **95%** de aprovação nesta prova | Antes, durante e depois da soldagem |
| 05 | Visual e dimensional | "Trabalhamos junto com o aluno para que ele identifique, localize, avalie e não confunda as descontinuidades. A prova deixa de ser subjetiva, como muita gente pensa, e ganha conceitos a serem assimilados." | "Temos uma grande quantidade de corpos de prova com descontinuidades similares às da prova. Média de aprovação igual à do acompanhamento de soldagem." | Identificar, localizar, avaliar |
| 06 | Dureza | "A prova tem duas partes. Na primeira, você lê as impressões já existentes num corpo de prova, numa situação criada na CDC semelhante à da prova. Na segunda, prepara a superfície e executa duas batidas; se uma delas ovalizar, tem direito a uma terceira." | "Acompanhamos como você executa as batidas e ensinamos a técnica para chegar a 100% sem ovalização." | Batidas sem ovalização |
| 07 | Estufas e consumíveis | "Assim como nas outras provas, desenvolvemos meios para você assimilar quais são as irregularidades dos consumíveis e como detectá-las. Na prova de estufas e consumíveis, oferecemos ambiente, material, instrumentos e equipamentos semelhantes aos da prova." | **99%** de aprovação nesta prova | Estufas como as da prova |
| 08 | Recertificação | "Treinamento no modelo novo de recertificação, simplificado, com instrutores que já fizeram as provas. Por isso, conhecimento e capacitação para um treinamento eficaz, nas mesmas condições oferecidas na prova." | n/a | As três disciplinas da nova formatação |

Textos dentro das ilustrações: "Símbolo de soldagem · exemplo", "6", "EPS" (02) · "°C", "tempo", "aquecimento", "patamar", "resfriamento", "Gráfico de exemplo", leitura "25 °C" que muda (03) · "Antes", "Durante", "Depois" (04) · "porosidade", "mordedura" (05) · "1ª batida", "ovalizou", "3ª batida" (06) · "Visual de / ajuste de junta", "Inspeção durante / a soldagem", "Visual final / de solda" (08).

### 8.8 05 · Material oferecido (`#material`)

- Título: **Recursos para você não travar no dia da prova.**
- **Material escrito**: "Procedimentos similares aos utilizados nas provas" · "Exercícios que desenvolvem a compreensão e o raciocínio" · "Vários simulados" · "Treinamento personalizado"
- **Aula informatizada**: "Aula de tratamento térmico e documentos técnicos no computador" · "Simulados no computador no nível da prova"
- **Material audiovisual**: "Vídeos desenvolvidos para facilitar o entendimento, principalmente da prova teórica"

### 8.9 06 · Estrutura e hospedagem (`#estrutura`)

- Título: **Conheça nosso CT de Treinamento**
- "Nosso Centro de Treinamento conta com uma estrutura preparada para proporcionar conforto, praticidade e qualidade durante toda a jornada de aprendizado dos nossos alunos."
- "O ambiente dispõe de salas equipadas com computadores de ótima qualidade, proporcionando condições adequadas para estudos, atividades e desenvolvimento profissional."
- "Além disso, contamos com uma cozinha totalmente equipada e disponibilizada para utilização de todos os alunos, oferecendo mais comodidade durante a permanência no centro de treinamento."
- Itens: "Instrumentos, corpos de prova e exercícios liberados depois das 8 horas de treinamento com o instrutor, para você estudar mais." · "Quartos coletivos com ar-condicionado, TV e wi-fi." · "Ambiente tranquilo, voltado inteiramente para o aprendizado."
- Rota (`aria-label` "CDC a um quarteirão do SENAI e a 10 minutos da FBTS"): nós "CDC", "SENAI", "FBTS"; distâncias "1 quarteirão", "10 min"; legenda "A um quarteirão do SENAI de solda, onde as provas são realizadas, e a 10 minutos da FBTS." + "Rua Jorge Rudge, 180 · Maracanã"
- **Sala de informática**: "Sala totalmente equipada" · "Computadores de ótima qualidade" · "Ambiente preparado para apoiar os estudos e as atividades de formação dos alunos"
- **Cozinha equipada**: "Geladeira" · "Fogão" · "Air fryer" · "Misteira" · "Armários" · "Espaço disponível para utilização de todos os alunos"
- Fita de fotos (`aria-label` "Fotos do CT de Treinamento"):

| Nº | Legenda | Arquivo | Proporção | Texto alternativo (`alt`) |
|---|---|---|---|---|
| 01 | Sala de Documentos e Tratamento | `fotos/ct-sala-de-informatica.webp` | 825/1100 | Sala de informática com computadores, teclados e cadeiras |
| 02 | Sala de Recertificação e Visual | `fotos/ct-sala-de-aula.webp` | 1467/1100 | Sala de aula com mesas longas, quadro branco e o pôster da CDC com as posições de soldagem |
| 03 | Estufas e Consumíveis e Acompanhamento | `fotos/ct-sala-de-estudos.webp` | 1100/1100 | Sala com carteiras, a placa da CDC na parede e uma estante de livros |
| 04 | Sala de Documentos e Tratamento | `fotos/ct-apoio.webp` | 825/1100 | Mesa com computador, impressora, notebook e monitor na parede |
| 05 | Acompanhamento e Soldagem | `fotos/ct-treino-pratico.webp` | 825/1100 | Instrutor mede um tubo soldado com trena ao lado de uma pessoa com máscara e avental de solda |
| 06 | Estufas e Consumíveis | `fotos/ct-estufas-e-consumiveis.webp` | 825/1100 | Corredor com as estufas de secagem e caixas de consumíveis de soldagem |
| 07 | Hospedagem: quarto coletivo | `fotos/ct-hospedagem.webp` | 678/1100 | Quarto coletivo com beliches de lençóis verdes e mesas de apoio |
| 08 | Cozinha equipada | `fotos/ct-cozinha.webp` | 770/1100 | Cozinha com mesa e cadeiras, armários, micro-ondas, liquidificador e filtro de água |
| 09 | Fogão de cinco bocas | `fotos/ct-fogao.webp` | 825/1100 | Fogão de cinco bocas na cozinha do centro de treinamento |
| 10 | Air fryer e misteira | `fotos/ct-air-fryer-e-misteira.webp` | 727/1100 | Air fryer e misteira sobre a bancada da cozinha |

> Os nomes das salas e ambientes são os das legendas acima. Atenção: a legenda 01 ("Sala de Documentos e Tratamento") está numa foto cujo arquivo e `alt` falam em "sala de informática". Registrado como está no site.

### 8.10 07 · Depoimentos (`#depoimentos`)

- Título acessível (oculto): "Depoimentos de alunos"
- "Bom dia Deiwson e Rose. Gostaria de agradecer a vcs pelo excelente treinamento que vcs me proporcionaram. Fui aprovado no exame. Graças a Deus. Parabéns e muito obrigado!! Abraço" · **Geraldo Feliciano Ferreira** · Aprovado no exame
- "Opa... só saiu meu resultado hoje da recertificação!! Obrigado pela atenção dispensada!!" · **Maurilio Knop** · Recertificado
- "Deiwson e Rose, bom dia, obrigado pelo treinamento e hospitalidade. Passando pra te falar que fui aprovado na recertificação." · **Oswaldo Teles** · Recertificado
- Controles: "←" ("Depoimento anterior") · "**1** de 3" · "→" ("Próximo depoimento")

### 8.11 08 · Área do aluno (`#area-do-aluno`)

- Título: **Apostilas, vídeos e exercícios.**
- "Os materiais da área comum abrem aqui mesmo no site: leia, pesquise em todos eles e continue de onde parou."
- Busca: *placeholder* "Pesquisar nos materiais: dureza, eletrodo, simbologia…" · botão **Pesquisar**
- Acessos: "Área comum" **Vídeos** → · "Área comum" **Material** → · "Área do curso" **Faça seu login** ↗ (Kiwify)
- Estante: "Prova teórica · questões + gabarito" **Apostila teórica** "168 páginas" · "Recertificação · IB-024 FBTS" **Procedimento de recertificação** "39 páginas" · "Prova prática · consumíveis e estufas" **Procedimentos de provas práticas** "5 páginas" · cada um com "Ler"

### 8.12 09 · Dúvidas (`#duvidas`)

- Título: **Perguntas frequentes**
- **Como agendo o meu treinamento?** "Fale com a Rose pelo telefone ou WhatsApp (21) 98257-0418. O agendamento segue a disponibilidade do calendário e a agenda dos instrutores."
- **Onde fica o centro de treinamento?** "Na Rua Jorge Rudge, 180, no Maracanã, Rio de Janeiro (RJ). Fica a um quarteirão do SENAI de solda, onde as provas são realizadas, e a 10 minutos da FBTS."
- **A CDC oferece hospedagem?** "Sim. Quartos coletivos com ar-condicionado, TV e wi-fi, no local de treinamento. Depois das 8 horas de treinamento com o instrutor, os instrumentos, corpos de prova e exercícios ficam liberados para você continuar estudando."
- **Como funciona o Curso Inspetor de Soldagem Nível 1?** "É semipresencial, com aulas gravadas, on-line e presenciais, e o acesso vale por 6 meses. O pagamento pode ser à vista ou parcelado no cartão de crédito."
- **Como são cobrados os treinamentos de qualificação?** "Documentos técnicos e tratamento térmico: R$ 900 por 2 dias. Dureza, inspeção de eletrodo, estufa, acompanhamento de soldagem e inspeção visual: R$ 550 por diária de retreinamento (sugerimos 4 dias). O treinamento é de 8 horas por dia."
- **Como acesso o material de estudo?** "Pela Área do aluno, aqui no site: a apostila teórica, o procedimento de recertificação e os procedimentos de provas práticas abrem direto no leitor, com busca e sumário. O curso fica na plataforma Kiwify, com o seu login." ("Área do aluno" → `#area-do-aluno`)

### 8.13 10 · Aplicativo (`#aplicativo`)

- Título: **Conheça o CDC Capacitação em Qualidade**
- "O CDC Capacitação em Qualidade é uma plataforma desenvolvida para transformar a preparação de profissionais da área da qualidade e inspeção de soldagem."
- "Reunimos questões técnicas, simulados, explicações e ferramentas de acompanhamento em um ambiente digital pensado para proporcionar uma experiência de estudo mais organizada, dinâmica e eficiente."
- "Mais do que responder questões, queremos ajudar você a compreender o conteúdo e avançar na sua preparação profissional."
- Janela: caminho "Questões › Inspeção de soldagem" · estado "Modo estudo" · módulo "MÓDULO: INSPEÇÃO DE SOLDAGEM" · "Questão demonstrativa" · "Inspeção visual"
- Enunciado: "Durante a inspeção visual de uma junta soldada, qual das seguintes descontinuidades corresponde a uma abertura na superfície do metal de solda ou do metal de base?"
- Alternativas: A) "Inclusão de escória." · B) "Porosidade interna." · **C) "Trinca."** (correta) · D) "Falta de fusão interna." · E) "Inclusão metálica."
- Rodapé da janela: "Exemplo interativo" · botão "Tentar novamente"
- Retornos (`aplicativo.js`):
  - Certo: "**Resposta correta.**" + "A **trinca** é uma descontinuidade do tipo fratura: forma uma abertura no metal de solda ou no metal de base. Quando atinge a superfície, pode ser identificada já na inspeção visual."
  - Errado: "**Resposta incorreta. A alternativa correta é a C) Trinca.**" + motivo + a mesma explicação.
  - Motivos: A "A inclusão de escória é material não metálico retido na solda, e não uma abertura no metal." · B "A porosidade interna é formada por gás aprisionado dentro do cordão, abaixo da superfície." · D "A falta de fusão interna é a ausência de união entre passes, ou com o metal de base, no interior da junta." · E "A inclusão metálica é um metal estranho retido na solda, como partículas de tungstênio."
- Botão: **Conhecer o aplicativo ↗** (`https://cdc-capacita-o-em-qualidade.lovable.app/`)
- Crédito: "Aplicativo desenvolvido por Adrian Lucas Lopes Maximiano."

### 8.14 11 · Contato (`#contato`)

- Fecho: **Com qualidade** / **desenvolvemos** / **competências.** (em caixa alta pelo CSS; a 3.ª linha em metal fundido)
- Formulário: **Pré-inscrição pelo WhatsApp** · "Preencha e o WhatsApp abre com a mensagem pronta para a Rose. É só enviar." · "Seu nome" (*placeholder* "Nome e sobrenome") · "Treinamento" · "Mensagem (opcional)" (*placeholder* "Datas que você prefere, dúvidas…") · botão **Abrir no WhatsApp**
- Opções do campo "Treinamento", na ordem: "Curso Inspetor de Soldagem Nível 1 (semipresencial)" · "Qualificação: documentos técnicos + tratamento térmico" · "Qualificação: diárias de retreinamento" · "Recertificação Nível 1 (2 dias)" · "Recertificação Nível 1 (3 dias)" · "Hospedagem" · "Tenho uma dúvida"
- Mensagens: erro "Escreva o seu nome para a Rose saber com quem está falando." · envio "O WhatsApp abre numa nova aba com a sua mensagem. Se não abrir, escreva para (21) 98257-0418."
- Canais:
  - **Telefone e WhatsApp**: (21) 98257-0418 [Copiar] · "Rose · agendamento dos treinamentos" · (21) 98257-0433 [Copiar]
  - **E-mail**: deiwsonribeiro@gmail.com [Copiar] · rosecdcinsp@gmail.com [Copiar]
  - **Endereço**: "Rua Jorge Rudge, 180" / "Maracanã · Rio de Janeiro (RJ)" · "Abrir no mapa ↗" (`https://www.google.com/maps/search/?api=1&query=Rua Jorge Rudge, 180, Maracanã, Rio de Janeiro - RJ`)
  - **Redes sociais**: "Instagram e Facebook oficiais" · "Redes sociais ↗" (abre o pop-up)

### 8.15 Rodapé

"CDC Capacitação em Qualidade" / "Deiwson Ribeiro ME · desde 2005" · links: A CDC, Treinamentos, Provas, Estrutura, Depoimentos, Área do aluno, Contato · "(21) 98257-0433 · (21) 98257-0418" / "Rua Jorge Rudge, 180 · Maracanã · Rio de Janeiro (RJ)" · Instagram, Facebook · "© 2026 CDC Capacitação em Qualidade. Todos os direitos reservados." · "Site desenvolvido por Adrian Lucas Lopes Maximiano."

### 8.16 Elementos flutuantes e pop-up

- WhatsApp: "Agendar com a Rose" (`aria-label` "Falar com a Rose no WhatsApp").
- Pop-up de redes: **Redes sociais** · "Acompanhe a CDC nos perfis oficiais." · Instagram "@deiwsonrosecdcoficial" · Facebook "cdctreinamentos.com.br".
- Avisos do copiar: "Copiado: <valor>" · "Selecionei para você. Use Ctrl+C ou Copiar."

### 8.17 Portal da área do aluno

- Topo: "← Voltar ao site" · logo + "Área do aluno" · "Área do curso ↗" (Kiwify)
- Cabeça: rótulo "CDC Área comum" · **Materiais de estudo** · "Apostila de questões, procedimento de recertificação e procedimentos de provas práticas. Leia aqui mesmo, pesquise em todos os materiais e continue de onde parou." · abas "Materiais 3" / "Vídeos 3" (o HTML traz 0, o script atualiza para 3)
- Vídeos (HTML de reserva, escondido quando há vídeos): "Ainda não há vídeos na área comum." · "Os vídeos aparecem aqui assim que forem publicados. As aulas gravadas do Curso Inspetor de Soldagem Nível 1 ficam na Área do curso." · "Entrar na Área do curso ↗"
- Cartões e mensagens gerados pelo JS (`portal.js`, `leitor.js`): "Ler agora" · "Continuar na pág. N" · "Baixar PDF" / "Abrir PDF ↗" · "Você parou na página N de T" · "Continue de onde parou" · "Buscando nos materiais…" · "Nada encontrado para “q”. Tente outra palavra." · "N ocorrência(s) de “q”" · "<títulos> é escaneado e fica fora da busca; use o sumário dentro dele." · "Não foi possível carregar o índice de busca. Verifique a conexão e tente de novo." · leitor: "Materiais", "Sumário", "Páginas", "Buscar", *placeholder* "Buscar neste material", "Abrir PDF ↗", "Baixar", "Abrindo o material… N%", "Não foi possível abrir este material agora.", "Tentar de novo", "Digite uma palavra para achar as páginas onde ela aparece.", "Digite pelo menos 2 letras.", "Buscando…", "N ocorrência(s) em N página(s)", "Nada encontrado neste material.", "Este documento foi escaneado: ele é uma imagem e não tem texto para buscar. Use o sumário ou as miniaturas."

### 8.18 Materiais (`materiais.js`, literal)

| Material | Prova · código | Resumo | Sumário (título, página) |
|---|---|---|---|
| **Apostila teórica** | Prova teórica · Questões + gabarito | "Apostila de questões atualizada para a prova teórica, organizada por capítulo, com o gabarito no final." | Índice 1 · Introdução 2 · Terminologia 5 · Simbologia 19 · Processos 61 · Consumíveis 83 · Metalurgia 95 · Controle de deformações 104 · Metais de base 117 · Ensaios mecânicos 120 · Ensaios não destrutivos 124 · Qualificações 131 · Instrumental e técnicas de medidas 139 · Documentos técnicos 153 · Proteção 161 · Gabarito 165 |
| **Procedimento de recertificação** | Recertificação · IB-024 · FBTS | "Exame de recertificação Nível 1: instruções aos candidatos, etapas da prova, critério de aprovação e anexos." | Revisões 1 · Objetivo, documentos e definições 2 · Metodologia e condições gerais 3 · Sequência das atividades 6 · Critério de aprovação 8 · Anexo 1 · Lista de verificação 9 · Anexo 2 · Relatório de não conformidade 10 · Anexo 3 · Fabricação e montagem 11 · Anexo 4 · Execução de soldagem 18 · Formulário de acompanhamento de soldagem 21 · Posições de soldagem 22 · Anexo 5 · Ensaio visual de solda 24 · Critérios de aceitação (API, ASME, AWS) 27 · Avaliação de descontinuidades 38 · Segurança, saúde e meio ambiente 39 |
| **Procedimentos de provas práticas** | Prova prática · Consumíveis e estufas | "Inspeção de recebimento, armazenagem, secagem e manutenção da secagem de consumíveis nos exames de qualificação." | 1 Objetivo 1 · 2 Documentos complementares 1 · 3 Definições e abreviações 1 · 4 Metodologia 1 · 4.1 Inspeção de recebimento 1 · 4.2 Armazenamento 2 · 4.3 Estufa de armazenamento 3 · 4.4 Secagem e manutenção da secagem 3 · 4.5 Estufas de secagem e manutenção 4 |

Vídeos: ficha CEN-12.

### 8.19 Rótulos de acessibilidade (`aria-label`, literais)

Barra e menu: "CDC, voltar ao início" · "Seções" · "Ligar o som da página" / "Desligar o som da página" · "Abrir menu" / "Fechar menu" · "Menu". Página: "Depoimentos de alunos" (carrossel) · "Depoimento anterior" · "Próximo depoimento" · "Fotos do CT de Treinamento" · "CDC a um quarteirão do SENAI e a 10 minutos da FBTS" · "Materiais da área comum" · "Falar com a Rose no WhatsApp" · "Rodapé" · "Redes sociais da CDC" (canto e rodapé) · "<Rede> da CDC (abre em nova aba)" · "Reproduzir o vídeo: <título>" · "Ler <título>". Portal e leitor: "Conteúdo da área comum" · "Leitor de material" · "Página anterior" · "Página atual" · "Próxima página" · "Diminuir o zoom" · "Ajustar à largura" · "Aumentar o zoom" · "Navegação do material" · "Fechar o painel" · "Ocorrência anterior" · "Próxima ocorrência" · "Páginas do material". Pop-up: "Fechar". Rótulos ocultos de formulário: "Pesquisar nos materiais" · "Buscar neste material".

### 8.20 Dados institucionais consolidados

| Dado | Valor |
|---|---|
| Nome | CDC Capacitação em Qualidade |
| Razão social exibida | Deiwson Ribeiro ME |
| Desde | 2005 |
| Endereço | Rua Jorge Rudge, 180 · Maracanã · Rio de Janeiro (RJ) |
| Telefones | (21) 98257-0418 (Rose, WhatsApp, agendamento) · (21) 98257-0433 |
| E-mails | deiwsonribeiro@gmail.com · rosecdcinsp@gmail.com |
| Instagram | @deiwsonrosecdcoficial |
| Facebook | facebook.com/cdctreinamentos.com.br |
| Instrutores | Deiwson Ribeiro (IS 1429 N1 FBTS, IS 1423 N1 SENAI) · Rozilene Ribeiro "Rose" (IS 8176 N1 FBTS, IS 1426 N1 SENAI) |
| Compra do curso | Kiwify (`pay.kiwify.com.br/b2fQ0VB`) · login: `dashboard.kiwify.com.br/login` |
| Aplicativo | cdc-capacita-o-em-qualidade.lovable.app (desenvolvido por Adrian Lucas Lopes Maximiano) |
| Origem do conteúdo | segundo o README do projeto: páginas de cdccursos.com.br (site antigo em Wix) e fotos enviadas pela CDC |

---

## 9. Motion design

Princípios, curvas, tabela de durações e movimento reduzido: `CDC_DESIGN_SYSTEM.md` §11. Narrativa de movimento da página, em ordem:

1. **Abertura** (1–3,2 s): o logo enche de metal fundido; a cortina recolhe de baixo para cima (CAR-01).
2. **Hero**: o metal "chega" espalhado e branco, esfria no lugar da esquerda para a direita em ~1,35 s; aos 2,15 s um arco automático acende; o título sobe palavra por palavra; selo, texto, botões, lema e "Role" surgem do desfoque (ARC-01, ARC-02, TIP-01, TIP-02).
3. **Interação no hero**: maçarico, arco, faíscas, inclinação (ARC-01 a ARC-03; CUR-01 estado de calor).
4. **Saída do hero** (1 tela presa): câmera atravessa o logo, que vira brasas; texto se desfaz; vinheta fecha (ARC-04).
5. **Manifesto** acende palavra por palavra; números contam (TIP-03, TIP-04).
6. **Cartões** entram em lotes, inclinam e acendem sob o mouse (TIP-02, CRT-01).
7. **Prova por prova** (5,6 telas presas): uma prova por passo, com transição de folhear e ilustração animada (CEN-01, CEN-02).
8. **Estrutura**: rota com tracejado vivo; fita de fotos anda na horizontal, inclinando com a velocidade (CEN-04, CEN-03).
9. **Depoimentos**: troca a cada 7 s, palavra por palavra (CEN-05).
10. **Aplicativo**: a janela sobe com profundidade (rotação de 11°) (CEN-09).
11. **Fecho**: o lema se estica (62 → 116 % de largura) e acende; brasas sobem ao fundo; "competências." em metal fundido (TIP-06, TIP-07, FUN-02).
12. **Sempre presentes**: cordão de solda, grão de filme, cursor, barra que some e volta, botões magnéticos (ROL-01, FUN-01, CUR-01, ROL-03, BOT-02).

---

## 10. Animações e microinterações (catálogo com valores)

| # | Animação | Gatilho | Duração · curva · deslocamento · escala | Ficha |
|---|---|---|---|---|
| 1 | Abertura: avanço do metal | carregamento | até 30 % em 0,9 s `power2.out`; +30 % por tarefa em 0,6 s; final 0,45 s `power2.inOut` | CAR-01 |
| 2 | Abertura: brilho do logo | fim da carga | `scale 1.08`, `drop-shadow 28px` em 0,35 s `power2.out` | CAR-01 |
| 3 | Abertura: cortina | fim da carga | `clip-path inset(0 0 100% 0)` em 1,0 s `expo.inOut`; logo `y −60`, opacidade 0 em 0,6 s `power2.in` | CAR-01 |
| 4 | Montagem do logo | cortina sobe | atraso 0,05–1,35 s por ponto; mola 55; atrito 7 → 2,6 em 3 s; esfria τ 1,1 s | ARC-01 |
| 5 | Arco automático | t = 2,15 s | clarão 0,6; 140 faíscas força 8; flash CSS 0,55 → 0 em 0,9 s `expo.out` | ARC-02 |
| 6 | Título do hero | abertura + 0,15 s | palavras `yPercent 118 → 0`, `rotate 3° → 0`, 1,15 s `expo.out`, cascata 0,04 s | TIP-01 |
| 7 | Resto do hero | abertura + 0,45 s | `y 22 → 0`, `blur 8 → 0`, opacidade 0 → 1, 1,1 s `expo.out`, cascata 0,1 s | TIP-02 |
| 8 | Dica do hero | `is-pronto` | opacidade 0 → 0,85 em 1 s, atraso 0,4 s | FUN-03 |
| 9 | Maçarico | mouse no hero | raio 1,05 un. (≈ 63,5 px); aquece 2,4/s; empurra 22; pega 14 | ARC-01 |
| 10 | Inclinação do logo | mouse | até 0,32 rad (18,3°); mola k 26, c 6,5; ocioso `sin(0,42t)·0,14` | ARC-01 |
| 11 | Clique: arco | `pointerdown` no hero | explosão raio 3 un. força 24; segura 80; clarão 1 (meia-vida 63 ms); 240 faíscas força 11; flash 0,9 → 0 em 0,9 s; tremor `x 7, y −4 → 0` em 0,45 s `elastic.out(1.2, 0.25)` | ARC-02 |
| 12 | Faíscas | arco / passe rápido | gravidade 16; arrasto e^(−0,9dt); quique −0,32; vida 0,45–1,55 s; rastro 30 ms | ARC-03 |
| 13 | Saída do hero | rolagem (1 tela presa) | texto `y −50`, `blur 10`, opacidade 0, `power1.in` na 1.ª metade; câmera `smoothstep`, distância até 12 %; giro 0,2 rad; vinheta 0 → 1 | ARC-04 |
| 14 | "Role" | sempre | linha de 28 px cresce e recolhe, 2 s `--suave` | FUN-03 |
| 15 | Cursor: anel | `pointermove` | segue em 0,38 s `power3.out`; tamanhos 38/58/76/120 px em 0,35 s `--entrada` | CUR-01 |
| 16 | Cursor: rótulo | `[data-cursor]` | disco 76 px brasa; texto 0 → 1 em 0,2 s | CUR-02 |
| 17 | Barra: esconder / mostrar | direção da rolagem, além de 110 % da tela | `yPercent −160` em 0,45 s `power2.in` / `0` em 0,7 s `expo.out` | ROL-03 |
| 18 | Barra: sólida | `scrollY > 40` | fundo 0,55 → 0,82 e sombra, 0,4 s | ROL-03 |
| 19 | Links: sublinhado | *hover* / seção atual | `scale 0 → 1`, origem troca de lado, 0,5 s `--entrada` | ROL-03 |
| 20 | Links: letras | `mouseenter` | ScrambleText A–Z, 0,55 s | TIP-05 |
| 21 | Âncoras | clique | 1,7 s *ease-in-out quart* | ROL-02 |
| 22 | Cordão | rolagem | altura = progresso; ponta tremula 0,12 s `steps(2)`; aparece com 0,6 s | ROL-01 |
| 23 | Blocos `[data-surgir]` | `top 90%` | `y 26`, `blur 8` → 0, 1,05 s `expo.out`, cascata 0,09 s | TIP-02 |
| 24 | Títulos `[data-titulo]` | `top 88%` | ver #6 | TIP-01 |
| 25 | Manifesto | rolagem (`scrub 0.6`) | opacidade 0,13 → 1 por palavra; laranja nas palavras-chave | TIP-03 |
| 26 | Números | `top 88%` | 2 s `expo.out`, dígitos embaralham até 55 % | TIP-04 |
| 27 | Cartões: inclinação | mouse | ±3,5° / ±4,5°, 0,6 s `power3.out`, perspectiva 1 100 | CRT-01 |
| 28 | Cartões: luz | mouse | radial 240–440 px, opacidade 0,35–0,4 s | CRT-01 |
| 29 | Botão brasa: varredura | *hover* | faixa de luz `translate −120% → 120%` em 0,8 s `--entrada` | BOT-01 |
| 30 | Botões: magnetismo | mouse | x × 0,28, y × 0,36 em 0,5 s; volta em 0,9 s `elastic.out(1, 0.4)` | BOT-02 |
| 31 | Botões: onda | `pointerdown` | 12 px → `scale 40`, opacidade 0, 0,7 s `--entrada` | BOT-03 |
| 32 | WhatsApp: aparecer | `scrollY > 70 %` | `translate 0 140% → 0` em 0,7 s `--mola` | BOT-04 |
| 33 | WhatsApp: expandir | *hover* | texto `max-width 0 → 200px` em 0,5 s, `gap 0 → 10px` em 0,4 s | BOT-04 |
| 34 | WhatsApp: anel | sempre | `box-shadow` 0 → 18 px em 2,6 s | BOT-04 |
| 35 | Selo: ponto | sempre | opacidade 1 → 0,35 → 1 em 2,4 s | FUN-04 |
| 36 | Som: barras | som ligado | altura 5 → 16 → 5 px em 0,9 s | BOT-05 |
| 37 | Provas: troca | marco de rolagem | sai `y −28·s`, `blur 6`, 0,32 s `power2.in` / entra `y 40·s`, `blur 10`, 0,95 s `expo.out`; figura `clip-path` de cima para baixo, `scale 1.04 → 1`, 1,05 s `expo.inOut` | CEN-01 |
| 38 | Provas: contador | troca | ScrambleText 0–9, 0,5 s | CEN-01 |
| 39 | Provas: índice | rolagem | barra de 2 px enche por prova | CEN-01 |
| 40 | Ilustrações | prova ativa | 8 linhas do tempo (0,9–3,2 s) | CEN-02 |
| 41 | Rota | `top 78%` | linhas 0,8 s; nós `back.out(2.4)` 0,6 s; tracejado −60 a cada 4 s, infinito | CEN-04 |
| 42 | Fita de fotos | rolagem (presa) | x até −(largura − janela); `skewX` ±7° pela velocidade; foto interna `xPercent 5 → −5`, `scale 1.12` | CEN-03 |
| 43 | Depoimentos | 7 s / setas / teclado / arrastar | palavras `y 18`, `blur 6` → 0, 0,8 s, cascata 0,025 s; autor `x −14` 0,7 s | CEN-05 |
| 44 | Acordeão | clique | abre 0,6 s `expo.out` / fecha 0,45 s `power3.inOut`; ícone gira 0,45 s `--mola` | CEN-06 |
| 45 | Janela do app | `top 86%` | `y 72`, `rotateX 11°`, `scale .965` → 0, 1,4 s `expo.out`; peças `y 16`, 0,9 s, cascata 0,06 s | CEN-09 |
| 46 | Questão: resposta | clique | retorno abre 0,7 s; acerto `scale .985 → 1` `elastic.out(1, 0.45)`; erro `x −7 → 0` `elastic.out(1.1, 0.3)`; trilho 22 → 100 % em 0,9 s | CEN-09 |
| 47 | Fecho | rolagem (`scrub 0.8`) | `font-stretch 62 → 116 %`, `letter-spacing .06 → −.035 em`, `xPercent ±6 → 0`, opacidade 0,25 → 1, cascata 0,12 | TIP-06 |
| 48 | Metal fundido | sempre | gradiente 220 %, 7 s linear | TIP-07 |
| 49 | Brasas | seção na tela | 140 brasas, semente 2005 | FUN-02 |
| 50 | Grão | sempre | 6 posições a cada 0,9 s | FUN-01 |
| 51 | Menu | botão | cortina 0,7 s `expo.inOut`; links `yPercent 60`, 0,8 s, cascata 0,05 s; fecha 0,5 s | CEN-07 |
| 52 | Formulário: erro | enviar sem nome | tremor ±7 px em 0,42 s | CEN-08 |
| 53 | Aviso | copiar | `translate −50% 140% → 0` em 0,6 s `--mola`; 2,6 s visível | BOT-06 |
| 54 | Portal | clique | `clip-path: circle()` da origem, 0,9 s / 0,6 s `expo.inOut`; conteúdo `y 26`, 0,9 s, cascata 0,05 s | CEN-10 |
| 55 | Pop-up de redes | botão | `redes-entra` 0,45 s (`translate 0 14px`, opacidade) | CEN-13 |
| 56 | Redes do canto | `is-rolou` | `translate 12px → 0` 0,6 s, opacidade 0,5 s | CEN-13 |

**Parallax:** há paralaxe interno só na fita de fotos (#42). Não há paralaxe de camadas de fundo. **Profundidade:** o logo 3D (7 camadas, perspectiva de 32°), cartões inclinados (perspectiva 1 100) e a janela do app (`rotateX 11°`). **Física:** molas e gravidade no logo e nas faíscas, molas na inclinação, `elastic` na soltura magnética e no tremor.

---

## 11. Responsividade

Pontos de quebra e comportamento por aparelho: `CDC_DESIGN_SYSTEM.md` §12. Como **reproduzir** a responsividade:

1. Tipos e espaços com `clamp()` exatamente como nas tabelas do Design System (não usar degraus fixos por *breakpoint*).
2. Coluna de 1 240 px + *gutter* `max(16px, min(5vw, 64px))` + `env(safe-area-inset-*)` em todos os elementos encostados nas bordas.
3. Alturas com `svh` (`100svh` no hero e nas provas presas), com `100vh` de reserva.
4. Detecção de capacidade, não de largura, para as interações: `(hover: none)` → classe `toque` (sem hovers, sem Lenis, densidade de partículas de celular); `(hover: hover) and (pointer: fine)` → cursor, magnetismo, inclinação e luz.
5. Cenas presas com `gsap.matchMedia()` e as **mesmas condições** do original: provas (≥ 901 × 620 e sem movimento reduzido), fita (≥ 761 px e sem movimento reduzido), hero (sempre, exceto movimento reduzido).
6. O logo de partículas recalcula enquadramento e densidade por proporção da tela (deitada: 42 % × 46 %, centro em 69/44 %; em pé: 84 % × 24 %, centro em 50/27 %).
7. `ScrollTrigger.config({ ignoreMobileResize: true })` para a barra de endereço do celular não recalcular tudo.
8. Fecho medido em JS a cada `refreshInit`.

---

## 12. Funcionalidades (cada elemento interativo)

| Elemento | O que faz | Onde | Como funciona | Componente (arquivo) | Dependências | Como reproduzir |
|---|---|---|---|---|---|---|
| Âncoras internas | rolam suavemente até a seção | barra, menu, rodapé, botões | intercepta `a[href^="#"]`, `irPara` 1,7 s, foco no destino | `motor/rolagem.js` | Lenis | ROL-02 |
| Link "pular" | vai aos treinamentos | topo, só com foco | CSS `:focus` mostra o link | `base.css` | n/a | `.pular` |
| Botão de som | liga/desliga som sintetizado | barra | Web Audio, `localStorage` | `motor/som.js` | Web Audio | BOT-05, SOM-01 |
| Menu | navegação em tela cheia | ≤ 1080 px | cortina `clip-path`, Esc fecha | `cenas/contato.js` | GSAP | CEN-07 |
| Logo de partículas | aquecer com o mouse, abrir o arco com clique/toque | hero | three.js + física própria | `fogo/particulas.js` | three.js | ARC-01–03 |
| Botões de WhatsApp | abrem conversa com mensagem pronta | hero, planos, menu, flutuante, formulário | links `wa.me/5521982570418?text=…` | `index.html`, `cenas/contato.js` | WhatsApp | CEN-08 |
| Comprar o curso | checkout | plano em destaque | link Kiwify (nova aba) | `index.html` | Kiwify | link |
| Índice das provas | salta para uma prova | provas (modo preso) | clique → `irPara` no meio do trecho | `cenas/provas.js` | GSAP | CEN-01 |
| Carrossel | troca depoimentos | depoimentos | setas, teclado, arrastar, 7 s | `cenas/depoimentos.js` | GSAP SplitText | CEN-05 |
| Busca nos materiais | encontra páginas com o termo | área do aluno e portal | índice JSON, sem acentos | `aluno/busca.js`, `aluno/portal.js` | `indice.json` | CEN-10 |
| Acessos / estante | abrem o portal ou o leitor | área do aluno | *hash* + cortina circular | `aluno/portal.js` | GSAP | CEN-10 |
| Faça seu login | área do curso | área do aluno, portal | link Kiwify | `index.html`, `materiais.js` | Kiwify | link |
| Leitor de PDF | lê, busca, salta, amplia | portal | pdf.js virtualizado | `aluno/leitor.js` | pdf.js | CEN-11 |
| Vídeos | toca aulas | portal, aba Vídeos | capa → `iframe` youtube-nocookie | `aluno/videos.js` | YouTube | CEN-12 |
| Acordeão | mostra respostas | dúvidas | `details` + GSAP | `cenas/contato.js` | GSAP | CEN-06 |
| Prévia da questão | responder e ver explicação | aplicativo | estado local | `cenas/aplicativo.js` | GSAP | CEN-09 |
| Conhecer o aplicativo | abre o app | aplicativo | link Lovable (nova aba) | `index.html` | app no Lovable | link |
| Pré-inscrição | monta a mensagem do WhatsApp | contato | `input` → `href` | `cenas/contato.js` | WhatsApp | CEN-08 |
| Copiar | copia telefone/e-mail | contato | Clipboard API + reserva | `motor/interacao.js` | Clipboard | BOT-06 |
| Telefones / e-mails | ligam / escrevem | contato | `tel:` / `mailto:` | `index.html` | n/a | links |
| Abrir no mapa | mapa | contato | Google Maps `search` | `index.html` | Google Maps | link |
| Redes sociais | perfis oficiais | canto, rodapé, pop-up | `dialog.showModal()` | `redes.js` | n/a | CEN-13 |
| Progresso salvo | continua de onde parou | portal, estante | `localStorage['cdc-aluno-v1']` | `aluno/portal.js` | n/a | CEN-10 |

**Galerias:** só a fita de fotos (não abre em tela cheia). **Formulários:** pré-inscrição e buscas (não enviam dados a servidor). **Vídeos:** só na área comum (YouTube). Não há vídeo de fundo.

---

## 13. Arquitetura técnica

### 13.1 Árvore de arquivos (repositório `landing-page-cdc`)

```
index.html                 página única (todas as seções, portal, pop-up)
package.json               scripts e 4 dependências
package-lock.json
vite.config.js             base './', modo "artefato" (bibliotecas por CDN)
README.md
public/
  og.jpg                   imagem de compartilhamento (1200×630)
  marca/                   cdc-mascara.png (1400×717), favicon.png (64), apple-touch-icon.png (180)
  fotos/                   10 fotos .webp do CT
  materiais/               3 PDFs, capas/ (3 .webp), indice.json (texto das páginas)
  vendor/pdfjs/            pdf.worker.min.mjs + standard_fonts/ (12 fontes + 2 licenças)
src/
  main.js                  liga tudo na ordem certa
  redes.js                 links das redes sociais (único lugar)
  motor/   carga.js · rolagem.js · texto.js · interacao.js · som.js
  fogo/    particulas.js · brasas.js
  cenas/   hero.js · provas.js · estrutura.js · depoimentos.js · contato.js · aplicativo.js
  aluno/   materiais.js · portal.js · leitor.js · busca.js · videos.js
  estilo/  tokens · base · topo · secoes · provas · fim · aluno · redes · aplicativo · videos (.css)
```

### 13.2 Ordem de inicialização (`src/main.js`, EXATO)

1. `gsap.registerPlugin(ScrollTrigger)`. Lê `prefers-reduced-motion` e `(hover: none)`. Adiciona `com-movimento` (se não reduzido). Rede de segurança: remove `com-movimento` em 8 s.
2. `history.scrollRestoration = 'manual'`, guarda o destino do *hash*, `scrollTo(0, 0)`.
3. `criarSom`, `criarRolagem` (Lenis), `rolagem.parar()`, `iniciarInteracao` (cursor, magnetismo, onda, cartões, copiar).
4. Inicia `particulas()` com a máscara. Se falhar → `hero.sem-webgl`.
5. `abrir({ tarefas: [document.fonts.ready, logoPronto] })`. Quando a cortina começa a subir:
   `rolagem.seguir()` → `logo.comecar()` → `entradaHero` → `ajustarFecho` (+ a cada `refreshInit`) → **cenas presas na ordem da página**: `saidaHero`, `iniciarProvas`, `iniciarEstrutura` → `iniciarTexto` e `iniciarFecho` (se não reduzido) → `iniciarDepoimentos` → `iniciarInscricao` → `iniciarDuvidas` → `iniciarMenu` → `ligarRolagem` (âncoras, barra, cordão, links ativos) → `iniciarAreaDoAluno` → `montarVideos` → `iniciarRedes` → `iniciarAplicativo` → `brasas` → `ScrollTrigger.refresh()` → `is-pronto` → salto ao destino do *hash*.
6. `document.fonts` `loadingdone` → `ScrollTrigger.refresh()`.

> A ordem das cenas presas importa: o ScrollTrigger calcula os espaçadores na ordem de criação.

### 13.3 Classes de estado no `<html>`

`js` · `toque` · `com-movimento` · `tem-cursor` · `lenis` (do Lenis) · `sem-carga` · `is-pronto` · `is-rolou` · `is-rolando` · `provas-presas` · `menu-aberto` · `portal-aberto` · `redes-aberto`.

### 13.4 Atributos de dados (API declarativa)

`data-titulo` · `data-surgir` · `data-destaque` · `data-contar` / `data-de` · `data-magnetico` · `data-inclinar` · `data-luz` · `data-cursor` · `data-copiar` · `data-falas` · `data-prova` · `data-abrir-material` · `data-progresso-de` · `data-abrir-redes` / `data-fechar-redes` / `data-redes-canto` / `data-redes-linha` / `data-redes-lista` · `data-aba` / `data-painel-de` · `data-kiwify` · `data-fechar-portal` · `data-lenis-prevent` · `data-janela-app` / `data-questao` / `data-letra` / `data-retorno` / `data-refazer` · leitor: `data-voltar`, `data-pag`, `data-zoom`, `data-painel`, `data-painel-aba`, `data-achado`.

### 13.5 Build

- `npm run build` → `dist/` (site completo, todas as bibliotecas no pacote). É o formato publicado: o `index-DsBXkgpX.js` (758 KB) contém three.js, GSAP e Lenis. O pdf.js é um *chunk* separado (`pdf.min-CFgnYaI8.js`), carregado sob demanda. **OBSERVADO.**
- `npm run build:artefato` → `dist-artefato/` (bibliotecas pelo jsDelivr, versões travadas; o leitor não oferece download).
- Vite reescreve `url('/marca/cdc-mascara.png')` do CSS para `../marca/cdc-mascara.png` (base relativa). **OBSERVADO** no CSS publicado.

---

## 14. Dependências

Documento próprio: **`TECHNICAL_DEPENDENCIES.md`**. Resumo:

| Tipo | Itens |
|---|---|
| Bibliotecas (npm, versões travadas) | gsap 3.15.0 · lenis 1.3.27 · three 0.186.1 · pdfjs-dist 5.7.284 |
| Ferramenta | vite 8.3.5 (*bundler* Rolldown e LightningCSS) |
| Serviços externos em tempo de execução | Google Fonts · WhatsApp (`wa.me`) · Kiwify · YouTube / ytimg · Google Maps · Instagram · Facebook · app no Lovable (link) |
| Hospedagem atual | Vercel (`cdc-cursos-kappa.vercel.app`) |
| **Lovable Cloud** | **não usado** por este site (só um link para o app separado) |
| **Supabase** | **não usado** (sem `@supabase`, sem chaves, sem chamadas) |
| Variáveis de ambiente | **nenhuma** (só `import.meta.env.MODE`, definido pelo Vite) |
| Armazenamento local | `localStorage`: `cdc-som`, `cdc-aluno-v1` |

---

## 15. Recursos e arquivos necessários

Inventário completo com caminho, formato, finalidade e risco: **`ASSETS_INVENTORY.md`**. Indispensáveis: `public/marca/cdc-mascara.png` (o logo de partículas, a abertura e todos os logos dependem dela), as 10 fotos, os 3 PDFs + capas + `indice.json`, `public/vendor/pdfjs/`, `og.jpg`, ícones, todo o `src/` e o `index.html`.

---

## 16. Regras de implementação (obrigatórias numa reconstrução)

**Manter:**

1. Um tema escuro só, com os tokens exatos de `tokens.css`.
2. As três famílias (Archivo variável com eixo `wdth`, Instrument Sans, IBM Plex Mono) e a hierarquia da §4.
3. A ordem das seções, os textos literais (§8), os links e os números de telefone.
4. O logo como máscara do PNG original. Nunca redesenhar o logotipo.
5. As experiências-assinatura com os parâmetros das fichas: abertura de metal fundido, logo de partículas com maçarico e arco, saída com a câmera, cordão de solda, cursor com rótulos, prova por prova presa, fita de fotos, fecho elástico, brasas, grão.
6. As condições de ativação (toque, ponteiro fino, movimento reduzido) e as saídas de movimento reduzido.
7. A ordem de inicialização (§13.2) e o relógio único GSAP → Lenis.
8. A área do aluno própria (portal, leitor, busca e progresso local). Nenhum botão leva ao site antigo. Só o login vai para a Kiwify.

**Proibido:**

- Transformar o site num *template* genérico ou trocar as seções por blocos comuns de *landing page*.
- Criar aparência artificial de site feito por IA: gradientes roxo-azul genéricos, ícones de biblioteca, ilustrações 3D de banco, *glassmorphism* sem função, textos genéricos.
- Substituir as peças personalizadas (cursor, cordão, logo de partículas, ilustrações SVG) por componentes prontos.
- Simplificar animações sem justificativa técnica registrada.
- Inventar textos, números, preços, depoimentos ou credenciais.
- Alterar a identidade visual ou modificar elementos que não foram pedidos.
- Usar fotos de banco de imagens no lugar das fotos reais do CT.

**Decisões a registrar** (efeitos colaterais do original, ver `CDC_DESIGN_LIBRARY_INDEX.md` §4): reproduzir ou não o encolhimento do cursor ao clicar, o recolhimento do WhatsApp depois do *hover*, o sumiço do lema e do "Role" ao voltar ao topo, o contador que pode parar em 090 e a rota animada no movimento reduzido.

---

## 17. Critérios de fidelidade visual

| Critério | Tolerância |
|---|---|
| Cores | HEX/RGBA idênticos aos tokens (diferença zero) |
| Tipos | família, peso, largura (`font-stretch`), espaçamento e `clamp` idênticos. Em 1440×900: h1 63,4 px, `.titulo` 83,5 px, fecho 115,17 px (±0,5 px) |
| Layout | posições do hero em 1440×900: conteúdo em x 64 px, y 270 px, largura 600 px. Logo centrado em x 994 px. Lema em y 577 px. Barra em x 64, y 12, 1 312 × 60 px (±2 px) |
| Alturas de rolagem | documento de 22 456 px em 1440×900 (±1 %); trava do hero de 1 tela; provas de 5,6 telas; fita de 2 813 px de deslocamento (±2 %) |
| Cursor | 6 / 38 / 58 / 76 / 120 px exatos; seguimento de 0,38 s |
| Cordão | 10 px × 34vh; ponta de 9 px; escamas a cada 7 px |
| Partículas | ~45,5 mil (computador) / ~23,3 mil (celular); pontos quadrados de ~2,3 px frios em 1440×900 |
| Tempos | durações e curvas das tabelas da §10 (sem tolerância no código) |
| Movimento reduzido | página de 17 445 px (±1 %), sem travas |
| Capturas de referência | comparar com o site publicado em 1440×900 e 390×664 (iPhone 13), no mesmo estado de rolagem. Recomendado: diferença de pixels média < 2 % fora do canvas das partículas, que tem componente aleatória |

---

## 18. Checklist de validação final

- [ ] Abertura: metal sobe de baixo para cima, contador de 3 dígitos, logo cresce 8 % e brilha, cortina recolhe de baixo para cima em 1 s.
- [ ] Hero: metal chega espalhado e branco e esfria da esquerda para a direita; arco automático aos ~2,15 s; título sobe palavra por palavra.
- [ ] Mouse no logo: anel de 120 px; pontos aquecem até o branco e o azul; passe rápido solta faíscas; o bloco inclina para o cursor.
- [ ] Clique no logo: clarão azulado, buraco aberto enquanto aperta, faíscas que quicam, tremor de 7 px, som (se ligado).
- [ ] Rolando: o hero fica preso 1 tela; a câmera entra no logo; o texto se desfaz; a vinheta fecha.
- [ ] Cursor: ponto exato com `difference`; anel com atraso; 58 px em links; disco "ABRIR/ENTRAR/LER/SOM" nos 7 elementos com `data-cursor`.
- [ ] Barra: vidro; sólida depois de 40 px; some ao descer (além de 110 % da tela) e volta ao subir; link da seção aceso; sublinhado de revenimento.
- [ ] Cordão de solda visível depois de 60 % de uma tela, com escamas, cores de revenimento perto da ponta, ponta tremulando e número 00–100.
- [ ] Manifesto acende com a rolagem; "2005," / "provas" / "provas," / "reprovação." ficam laranja.
- [ ] Números contam com dígitos embaralhando.
- [ ] Credenciais e planos inclinam e acendem; recursos com borda que acende.
- [ ] Prova por prova: presa por 5,6 telas; 8 provas; contador embaralha; índice enche; ilustrações animam.
- [ ] Rota com tracejado andando; fita de fotos horizontal com inclinação pela velocidade.
- [ ] Depoimentos trocam a cada 7 s com a seção na tela; pausam com o mouse.
- [ ] Acordeão anima; menu do celular em cortina.
- [ ] Portal abre em círculo a partir do clique; leitor abre os 3 PDFs; busca funciona sem acentos; progresso salvo.
- [ ] Vídeos tocam um por vez e param ao fechar.
- [ ] Prévia do app: certo em verde, errado em vermelho, "Tentar novamente".
- [ ] Fecho se estica de 62 % para 116 % e cabe exatamente na coluna; "competências." em metal fundido; brasas ao fundo.
- [ ] Pré-inscrição monta a mensagem; erro sem nome com tremor.
- [ ] Copiar e aviso; pop-up de redes; WhatsApp flutuante que expande.
- [ ] Toque: sem cursor, sem Lenis, sem cordão (≤ 760 px), provas em lista, fita com rolagem nativa.
- [ ] Movimento reduzido: sem abertura, sem cursor, sem travas, sem física; tudo visível.
- [ ] Todos os textos da §8 idênticos; todos os links da §12 corretos.
- [ ] Nenhum erro no console.

---

## 19. Fatos confirmados, inferências e limitações

**Confirmados no código e no site:** tudo o que está marcado EXATO e OBSERVADO.

**Inferências (marcadas como tal no texto):** causas dos efeitos colaterais (ARC-04 §6, CAR-01 §5); recomendações de uso nas seções "Como adaptar" das fichas; equivalências de HEX das cores lineares dos shaders.

**Limitações da análise:**

1. FPS e tempo de quadro reais **não foram medidos**: o ambiente usa WebGL por software.
2. O **som** não foi ouvido (sem saída de áudio). Os valores são do código.
3. Não foram acionados em execução: área de transferência, envio ao WhatsApp, abertura do portal, leitor, vídeos e acordeão (o código foi lido por completo).
4. O **contador da abertura** chegando a 100 em máquinas rápidas não foi verificado.
5. Configurações do projeto na Vercel (comando de *build*, versão do Node, domínios, variáveis) **não estão no repositório** e não puderam ser vistas: NÃO IDENTIFICADO. O site responde com `server: Vercel` e cache `public, max-age=0, must-revalidate` no HTML. Mesmo assim, o `npm run build` do commit `65c37e7`, refeito fora da Vercel (Node 22.23.4), gerou arquivos **idênticos byte a byte** aos publicados (`TECHNICAL_DEPENDENCIES.md` §11).
6. O domínio próprio `cdccursos.com.br` ainda aponta para o **site antigo no Wix** (resposta com cabeçalhos `x-wix-request-id`, OBSERVADO). O novo site só está no subdomínio da Vercel.
7. O conteúdo dos 3 PDFs não foi revisado página a página (fora do escopo visual).
8. O aplicativo no Lovable (`cdc-capacita-o-em-qualidade`) é outro projeto e não foi analisado.
