# CEN-03 · Fita de fotos que anda na horizontal (cena presa, inclinação pela velocidade, paralaxe interno)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (deslocamento total, escala e paralaxe medidos) |
| Portabilidade | Direta para qualquer sequência de imagens |
| Onde aparece | Seção 06 "Estrutura e hospedagem", depois dos cartões: 10 fotos reais do CT |
| Arquivos de origem | `src/cenas/estrutura.js` · `src/estilo/secoes.css` (bloco "fita de fotos") · `index.html` (`.filme`, linhas 501–514) |
| Dependências | GSAP 3.15.0 + ScrollTrigger |

## 1. Computador (`(min-width: 761px) and (prefers-reduced-motion: no-preference)`, EXATO)

```js
const distancia = () => Math.max(0, trilho.scrollWidth - innerWidth)
const inclina = gsap.quickTo(fotos, 'skewX', { duration: 0.5, ease: 'power3.out' })
gsap.set(fotos, { scale: 1.12, transformOrigin: '50% 50%' })
gsap.timeline({ scrollTrigger: {
  trigger: filme, start: 'center center', end: () => `+=${distancia()}`,
  pin: true, scrub: 0.8, anticipatePin: 1, invalidateOnRefresh: true,
  onUpdate(self) { inclina(gsap.utils.clamp(-7, 7, self.getVelocity() / -320)) },
  onScrubComplete: () => inclina(0),
}})
.to(trilho, { x: () => -distancia(), ease: 'none' }, 0)
.fromTo(fotos, { xPercent: 5 }, { xPercent: -5, ease: 'none' }, 0)
```

| Parâmetro | Valor | Confiab. |
|---|---|---|
| Início da trava | centro da fita no centro da tela | EXATO |
| Comprimento | largura do trilho − largura da janela. Em 1440 px: 4 253 − 1 440 = **2 813 px** de rolagem para **2 813 px** de deslocamento (1:1) | OBSERVADO |
| Suavização | `scrub: 0.8` | EXATO |
| Inclinação pela velocidade | `skewX = clamp(−7°, 7°, −velocidade/320)`. A 2 240 px/s de rolagem chega a 7°. Volta a 0 quando o *scrub* termina | EXATO, CALCULADO |
| Paralaxe interno | cada `img` com `scale: 1.12` desliza de `xPercent: +5` a `−5` dentro do próprio quadro (±18,2 px numa foto de ~365 px) | EXATO, OBSERVADO |
| Recalcular | `invalidateOnRefresh: true` (a distância é medida de novo a cada redimensionamento) | EXATO |

## 2. Geometria dos quadros (EXATO)

- Altura de todas as fotos: `--alto: clamp(300px, 54vh, 520px)` (486 px em 900 px de altura). A largura sai da proporção real de cada foto (`aspect-ratio: var(--ar)`, ex.: `825 / 1100`), com `max-width: 86vw`.
- Raio `var(--r-peca)` = 10 px. Sombra `0 30px 60px -36px #000`. Fundo `--aco-2` enquanto carrega.
- Espaço entre quadros: `clamp(14px, 1.6vw, 24px)`. Margens laterais iguais ao `--gutter`.
- **Tratamento de imagem**: `filter: grayscale(.35) contrast(1.08) saturate(.9) brightness(.92)` + camada `::after` com `linear-gradient(160deg, rgba(63,114,212,.22), transparent 45%, rgba(251,120,30,.2))` em `mix-blend-mode: soft-light` (sombras frias e luzes quentes) e contorno interno de 1 px branco a 6 %.
- Legenda: número mono 12 px em brasa + texto 15 px, `margin-top: 14px`.

## 3. Celular (≤ 760 px, EXATO)

Sem trava: a fita vira **rolagem horizontal nativa com encaixe** (`overflow-x: auto; scroll-snap-type: x mandatory`, `scroll-snap-align: center`), sem barra de rolagem, e `--alto: min(64vh, 112vw)`. **OBSERVADO** (iPhone 13).

## 4. Movimento reduzido

Sem trava e sem inclinação. A fita fica estática (com rolagem horizontal só se a tela for ≤ 760 px). **EXATO.**

## 5. Como adaptar

- Para fotos de produto, reduza a inclinação para ±4° e mantenha o paralaxe.
- A regra "altura fixa, largura pela proporção" preserva o enquadramento original de cada foto. Não force todas à mesma proporção.
