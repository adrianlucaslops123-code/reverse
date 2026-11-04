# TIP-03 · Manifesto que acende palavra por palavra com a rolagem (`data-destaque`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (palavras acesas e "provas," / "reprovação." em laranja na captura) |
| Portabilidade | Direta. A lista de palavras destacadas é específica do texto |
| Onde aparece | `p.manifesto__texto` da seção 01 "A CDC" |
| Arquivos de origem | `src/motor/texto.js` (bloco "manifesto") · `src/estilo/secoes.css` (`.manifesto__texto`) |
| Dependências | GSAP 3.15.0 + SplitText + ScrollTrigger |

## 1. Comportamento

O parágrafo é dividido em palavras. Todas começam quase apagadas (opacidade 0,13). Conforme a rolagem avança, elas **acendem uma a uma**, da primeira à última. Num segundo tempo da mesma linha do tempo, as palavras-chave ficam **laranja** (`#fb781e`).

## 2. Parâmetros (EXATO)

```js
const DESTAQUES = /^(2005|reprovação|provas)[.,]?$/i
const split = SplitText.create(el, { type: 'words', wordsClass: 'palavra' })
split.words.forEach((w) => { if (DESTAQUES.test(w.textContent.trim())) w.dataset.cor = '1' })
gsap.set(split.words, { opacity: 0.13 })
gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 82%', end: 'bottom 48%', scrub: 0.6 } })
  .to(split.words, { opacity: 1, stagger: 0.06, ease: 'none', duration: 0.3 }, 0)
  .to(split.words.filter((w) => w.dataset.cor), { color: '#fb781e', stagger: 0.06, duration: 0.3 }, 0.6)
```

| Parâmetro | Valor |
|---|---|
| Opacidade apagada | 0,13 |
| Janela de rolagem | do topo do parágrafo a 82 % da tela até a base a 48 % |
| Suavização do *scrub* | 0,6 s (a animação alcança a rolagem com 0,6 s de atraso) |
| Cascata | 0,06 por palavra, cada uma com 0,3 de duração, curva linear |
| Palavras em laranja | as que casam com `2005`, `reprovação` ou `provas` (com `.` ou `,` opcional). No texto atual são 4 palavras: "2005," · "provas" (em "as provas de qualificação.") · "provas," (em "essas provas,") · "reprovação." |
| Início do laranja | posição 0,6 da linha do tempo |
| Transição CSS extra | `.manifesto__texto .palavra { transition: color .2s }` |

> Na captura em 1440×900, "provas," e "reprovação." aparecem em laranja. **OBSERVADO.** As outras duas ocorrências ("2005," e o primeiro "provas") ficam fora do recorte da captura, mas casam com o padrão. **CALCULADO.**

## 3. Tipografia do manifesto (EXATO)

`640 clamp(30px, 4.4vw, 70px)/1.06 Archivo`, `font-stretch: 104%`, `letter-spacing: −0.022em`, `max-width: 26ch`, `margin-top: 34px`, `text-wrap: pretty`. Em 1440 px: 63,4 px. **CALCULADO.**

## 4. Movimento reduzido

Não é criado. O texto aparece inteiro, sem cor de destaque. **EXATO.**

## 5. Como adaptar

- Troque a expressão `DESTAQUES` pelas palavras-chave do novo texto.
- `start 82%` / `end 48%`: o parágrafo acende inteiro antes de chegar ao meio da tela. Para textos longos, use `end: 'bottom 30%'`.
