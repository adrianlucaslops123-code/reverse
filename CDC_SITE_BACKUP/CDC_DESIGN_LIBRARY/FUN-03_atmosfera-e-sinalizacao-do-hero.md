# FUN-03 · Atmosfera e sinalização do hero (fundo, lema, dica, indicador "Role")

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (com o efeito colateral do lema e do "Role" descrito em ARC-04 §6) |
| Portabilidade | Direta |
| Arquivos de origem | `src/estilo/topo.css` (bloco "hero") · `index.html` (linhas 88–106) |

## 1. Fundo do hero (EXATO)

```css
.hero {
  position: relative; height: 100vh; height: 100svh; min-height: 620px; overflow: clip;
  background:
    radial-gradient(70vmax 46vmax at 50% 38%, rgba(63, 114, 212, 0.13), transparent 70%),   /* luz azul do arco */
    radial-gradient(54vmax 30vmax at 50% 70%, rgba(251, 120, 30, 0.12), transparent 70%),   /* brasa embaixo */
    linear-gradient(to bottom, #0a0d12, var(--aco-0));
}
```

Mais a vinheta `::after` (ARC-04 §4) e o clarão `.hero__flash` (ARC-02).

## 2. Camadas (EXATO)

| Camada | `z-index` | Papel |
|---|---|---|
| `.hero__palco` (canvas WebGL) | auto (0) | logo de partículas, `inset: 0` |
| `.hero__flash` | auto | clarão em `screen` |
| `.hero::after` | 1 | vinheta |
| `.hero__lema`, `.hero__dica`, `.hero__rolar` | 2 | sinalização |
| `.hero__conteudo` | 3 | texto e botões (`pointer-events: none` no bloco; `auto` em links e selo) |

## 3. Texto do hero (EXATO)

- Bloco: `left: gutter`, `top: 50%`, `translate: 0 −44%`, largura `min(600px, 44vw)`, coluna com `gap: 18px` (14 px em ≤ 860 px).
- Tela estreita (`max-width: 899px` ou proporção < 11/10): o bloco desce para `bottom: 64px` (+ *safe-area*), largura `min(640px, 100% − 2·gutter)`, e o lema some.
- Selo: "● INSPETOR DE SOLDAGEM N1 · FBTS" (FUN-04).
- Título `h1`: `780 clamp(34px, 4.4vw, 70px)/0.98` Archivo 108 %, `letter-spacing −0.025em`, `text-wrap: balance`, sombra `0 2px 30px rgba(0,0,0,.6)`. Medido: 56,32 px em 1280; 45,06 px em 1024; 34 px em 768 e em 390; 70 px em 2560 (**OBSERVADO**). Em 1440: 63,36 px (**CALCULADO**).
- Texto: `clamp(15px, 1.15vw, 18px)`, `--texto-2`, `max-width: 52ch`, sombra `0 1px 16px rgba(0,0,0,.8)`. Some em ≤ 860 px de largura **e** ≤ 700 px de altura.
- Ações: `gap: 10px`, `margin-top: 6px`. Em ≤ 860 px os botões ocupam a largura (`flex: 1 1 220px`).

## 4. Sinalização (EXATO)

| Peça | Estilo | Comportamento |
|---|---|---|
| Lema "Capacitação em qualidade" | `600 clamp(11px, 1vw, 14px)/1` Archivo **125 %**, `letter-spacing .42em` (.3em em ≤ 860 px), caixa alta, `--ouro #c99f53` | posicionado pelo JS 26 px abaixo da base do logo e centrado nele (`--lema-x/--lema-y`). Escondido em telas estreitas |
| Dica | `500 11px/1.5` mono, `.1em`, caixa alta, `--texto-2`, alinhada à direita, `max-width: 320px`, `right: gutter`, `bottom: 52px` | opacidade 0 → 0,85 com `is-pronto` (transição de 1 s com 0,4 s de atraso). Texto: "Passe o mouse para aquecer o metal · clique para abrir o arco". No toque: "Toque no logo para abrir o arco". Some em ≤ 860 px |
| Indicador "Role" | `500 10px/1` mono, `.2em`, caixa alta, `--texto-3`, centrado embaixo (`bottom: 18px`) | linha de 1 × 28 px (gradiente `--texto-2` → transparente) que **cresce de cima** e **recolhe para baixo** em 2 s `var(--suave)`, para sempre (`@keyframes rolar`, troca do `transform-origin` em 50 %/51 %). Parado no movimento reduzido |

## 5. Como adaptar

- As duas manchas radiais (azul em cima, laranja embaixo) dão a luz de oficina. Troque pelas cores de acento da nova marca, mantendo a opacidade em 10–15 %.
- O indicador "Role" com troca de origem é uma técnica limpa para "linha que escorre". Reutilizável em qualquer projeto.
