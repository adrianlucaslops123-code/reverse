# CEN-11 · Leitor de PDF próprio (pdf.js): rolagem contínua, virtualização, zoom, sumário, miniaturas e busca

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (código lido. Os PDFs e o *worker* respondem no site publicado) |
| Portabilidade | Direta para qualquer PDF |
| Arquivos de origem | `src/aluno/leitor.js` · `src/estilo/aluno.css` (bloco "leitor") · `public/vendor/pdfjs/` (*worker* e fontes padrão) |
| Dependências | `pdfjs-dist` 5.7.284, versão **legacy** (`pdfjs-dist/legacy/build/pdf.min.mjs`), carregada sob demanda (`import()`, *chunk* `pdf.min-*.js`) |

## 1. Parâmetros (EXATO)

| Item | Valor |
|---|---|
| Zooms | 50, 67, 80, 100, 115, 130, 150, 175, 200, 250, 300 % |
| Largura base | largura disponível − 64 px (− 20 px em < 700 px), entre 240 e **980 px** |
| Espaço entre páginas | 18 px (no CSS do trilho) |
| Resolução | `min(DPR, 2)`, limitada a **5 milhões de pixels** por página no celular (< 700 px) e **12 milhões** no computador |
| Virtualização | desenha as páginas a menos de **140 %** da altura visível (`IntersectionObserver rootMargin '140% 0px'`). **Libera** as que passam de **450 %** |
| Fila | até **2 páginas** desenhando ao mesmo tempo, priorizando as mais próximas da página atual |
| Texto selecionável | camada de texto do pdf.js nos PDFs pesquisáveis |
| Página atual | a que cruza 30 % da altura visível (busca binária nos topos) |
| Progresso | avisa a página atual 350 ms depois de parar |
| Pré-carregamento | o módulo do pdf.js começa a carregar quando o ponteiro entra na seção "Área do aluno" ou quando o portal abre |
| Painel | Sumário (com atalho, ex.: "Ir para o gabarito · pág. 165"), Páginas (miniaturas de 110 px de largura) e Buscar. Abre sozinho em telas ≥ 1 200 px se houver sumário. Em < 900 px vira gaveta inferior (`height: min(74%, 560px)`, raio 18 no topo) |
| Teclado | ← / PageUp, → / PageDown, Home, End, + / =, −, Ctrl/Cmd + F (abre a busca) |
| Erro | mensagem com "Tentar de novo" e "Abrir o PDF ↗" |
| Download | "Baixar" com nome `CDC - <título>.pdf` (escondido no modo "artefato") |

## 2. Materiais cadastrados (`materiais.js`, EXATO)

| id | Título | Páginas | Tamanho | Pesquisável | Atalho |
|---|---|---|---|---|---|
| `apostila-teorica` | Apostila teórica | 168 | 5,4 MB | sim | Ir para o gabarito (p. 165) |
| `procedimento-recertificacao` | Procedimento de recertificação (IB-024 · FBTS) | 39 | 7,5 MB | **não** (escaneado) | Ir para o critério de aprovação (p. 8) |
| `procedimentos-provas-praticas` | Procedimentos de provas práticas | 5 | 0,6 MB | sim | n/a |

Sumários completos em `materiais.js` e na especificação mestre, §8.

## 3. Estilo (EXATO, resumo)

Barra de ferramentas com botões de 40 px (raio 10), número da página editável (58 × 40 px, mono), zoom em mono. Páginas com fundo branco, raio 2 px e sombra `0 22px 44px -24px rgba(0,0,0,.85)`. Fundo `radial-gradient(70% 50% at 50% 0%, #121820, --aco-0 70%)`. Destaque da busca nas páginas: `rgba(255,150,40,.38)`. Seleção: `rgba(63,114,212,.32)`.
