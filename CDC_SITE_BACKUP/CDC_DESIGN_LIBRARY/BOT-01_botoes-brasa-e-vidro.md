# BOT-01 · Botões "brasa" e "vidro" (com varredura de luz) e seus estados

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** |
| Portabilidade | Direta (CSS puro, com tokens) |
| Arquivos de origem | `src/estilo/base.css` (bloco "botões", linhas 70–97) · `src/estilo/topo.css` (`.nav__aluno`, `.nav__cta`) |
| Fichas relacionadas | BOT-02 (magnetismo), BOT-03 (onda no clique), CUR-01 (o anel vira `is-link`) |

## 1. Base `.botao` (EXATO)

| Propriedade | Valor |
|---|---|
| Caixa | `display: inline-flex; align-items: center; justify-content: center; gap: 10px` |
| Altura mínima | **46 px** (padrão) · **54 px** (`--grande`) · **44 px** (`.nav__aluno`, `.nav__cta`, `.portal__curso`) |
| Padding horizontal | 20 px · 26 px (`--grande`) · 16 px (barra; 14 px em ≤ 560 px) |
| Raio | `var(--r-botao)` = **12 px** |
| Borda | `0` (contornos são `box-shadow inset`) |
| Fonte | `600 15px/1.1 'Instrument Sans'`, `letter-spacing: −0.005em` (16 px no `--grande`, 14 px na barra) |
| Empilhamento | `position: relative; isolation: isolate; overflow: hidden` (a varredura e a onda ficam dentro do botão, atrás do texto) |
| Transições | `background .25s, box-shadow .25s, color .25s` |
| Ícone | `.icone` 20 × 20 px, `flex: none` |

## 2. Variante `.botao--brasa` (ação principal)

| Estado | Valor |
|---|---|
| Repouso | fundo `#fb781e`, texto `#1a0a02` (contraste 7,17:1), sombra `0 10px 30px -12px rgba(251,120,30,.7)` |
| Varredura de luz (`::before`) | `linear-gradient(105deg, transparent 32%, rgba(255,246,225,.75) 50%, transparent 68%)`, `inset: 0`, `z-index: −1`, `translate: −120% 0`, transição `translate .8s var(--entrada)` |
| Hover (sem toque) | fundo `#ff8a36`. A varredura vai a `translate: 120% 0`: uma faixa de luz atravessa o botão **da esquerda para a direita** em 0,8 s. Ao sair, ela **volta da direita para a esquerda** (a transição vale nos dois sentidos) |
| Pressionado | não há regra `:active`. O retorno visual é a onda (BOT-03) e, nos magnéticos, o deslocamento (BOT-02) |
| Foco por teclado | `:focus-visible { outline: 2px solid var(--arco) (#a8d8ff); outline-offset: 3px; border-radius: 6px }` |
| Desativado | **não existe** estilo de desativado para `.botao` no código (nenhum botão do site fica desativado) |

## 3. Variante `.botao--vidro` (ação secundária)

| Estado | Valor |
|---|---|
| Repouso | fundo `rgba(255,255,255,.06)`, texto `var(--texto)`, contorno `inset 0 0 0 1px var(--fio-forte)` (`rgba(168,194,222,.22)`), `backdrop-filter: blur(18px) saturate(1.25)` |
| Hover (sem toque) | fundo `rgba(255,255,255,.12)`, contorno `inset 0 0 0 1px rgba(168,216,255,.45)` (azul do arco) |
| Foco, pressionado, desativado | como na brasa |

## 4. Regra de hover

Todos os *hovers* usam `:where(html:not(.toque))`. Em telas de toque, o estado de hover nunca "gruda" depois de um toque. A classe `toque` é colocada por um script no `<head>`, antes do CSS, se `matchMedia('(hover: none)')`. **EXATO.**

## 5. Outros "botões" do sistema (resumo, valores EXATOS)

| Componente | Medidas e estados |
|---|---|
| `.falas__seta` (depoimentos) | círculo de 52 px, fonte 20 px, fundo `rgba(255,255,255,.05)`, contorno `fio-forte`. Hover: fundo brasa, texto `brasa-texto`, sem contorno (0,25 s) |
| `.copiar` | ver BOT-06 |
| `.som` | ver BOT-05 |
| `.menu-botao` | 44 × 44 px, raio 12, duas barras de 18 × 1,5 px com 6 px de espaço. Aberto: barras deslocadas 3,75 px e giradas ±45° (0,4 s `var(--entrada)`), formando um X |
| `.questao__refazer` | 36 px de altura, raio 9, `600 13px`. Hover brasa |
| `.opcao` (prévia do app) | ver CEN-09 |
| `.portal__sair` | 44 px, raio 12, `600 14px`. Hover `rgba(255,255,255,.1)` |
| Barra do leitor | 40 px de altura, raio 10, `600 14px`. Pressionado (`aria-pressed=true`): fundo `rgba(251,120,30,.16)`, contorno `rgba(251,120,30,.55)`, texto `brasa-quente` |
| `.link-seta` | texto `var(--brasa)`, 600. Hover: sublinhado com `text-underline-offset: 4px` |

## 6. Como reproduzir

Copie o bloco de `base.css` e os tokens `--brasa`, `--brasa-texto`, `--texto`, `--fio-forte`, `--desfoque`, `--r-botao`, `--entrada`, `--arco`.

## 7. Como adaptar

- A varredura combina com marcas "de metal e luz". Para marcas calmas, remova o `::before` e deixe só a troca de fundo.
- Mantenha o contraste de 4,5:1 no texto do botão principal.
