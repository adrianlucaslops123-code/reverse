# TIP-06 · Fecho tipográfico elástico: o lema se estica com a rolagem (fonte variável)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (valores intermediários e finais medidos) |
| Portabilidade | Depende de uma **fonte variável com eixo de largura** (`wdth`). Na CDC é a Archivo (62–125 %) |
| Onde aparece | Seção 11 "Contato": `h2.contato__titulo` com 3 linhas, "Com qualidade" / "desenvolvemos" / "competências." |
| Arquivos de origem | `src/cenas/contato.js` (`ajustarFecho`, `iniciarFecho`) · `src/estilo/fim.css` (`.contato__titulo`, `.contato__linha`, `.contato__linha--brasa`) · `src/main.js` (chama `ajustarFecho` na abertura e a cada `refreshInit` do ScrollTrigger) |
| Dependências | GSAP 3.15.0 + ScrollTrigger · Google Fonts (Archivo com eixo `wdth`) |

## 1. Comportamento

As três linhas do lema começam **comprimidas** (largura da fonte 62 %), **espaçadas** (+0,06 em), deslocadas para os lados (alternando −6 % e +6 %) e apagadas (25 %). Conforme a rolagem desce, elas **se esticam** até 116 % de largura, apertam o espaçamento (−0,035 em), centralizam e acendem, em cascata. A linha "competências." é de metal fundido (TIP-07).

## 2. Ajuste do tamanho para caber exatamente na coluna (EXATO)

```js
// mede a linha mais larga já na largura final da fonte (116 %) e acerta o tamanho
linhas.forEach((l) => { l.style.fontStretch = '116%'; l.style.letterSpacing = '-0.035em'; l.style.maxWidth = 'none' })
titulo.style.setProperty('--fecho', '100px')
const maior = Math.max(...linhas.map((l) => l.getBoundingClientRect().width))
const disponivel = titulo.clientWidth
titulo.style.setProperty('--fecho', `${Math.min(176, (100 * disponivel * 0.985) / maior).toFixed(2)}px`)
// restaura os estilos anteriores
```

- Tamanho = `100 px × (largura disponível × 0,985) / (largura da maior linha a 100 px)`, limitado a **176 px**.
- Valores medidos de `--fecho`: **115,17 px** (1440 e 2560 px de largura: coluna de 1 240 px), 106,99 px (1280×720), 85,63 px (1024×768), 64,18 px (768×1024), 32,60 px (iPhone 13, 390 px). **OBSERVADO.**
- Valor de reserva no CSS (antes do JS): `min(7.6vw, 116px)`.

## 3. Animação (EXATO)

```js
gsap.fromTo(linhas,
  { fontStretch: '62%', letterSpacing: '0.06em', xPercent: (i) => (i % 2 ? 6 : -6), opacity: 0.25 },
  { fontStretch: '116%', letterSpacing: '-0.035em', xPercent: 0, opacity: 1, ease: 'none', stagger: 0.12,
    scrollTrigger: { trigger: '.contato__titulo', start: 'top 92%', end: 'top 34%', scrub: 0.8 } })
```

| Propriedade | Início | Fim |
|---|---|---|
| `font-stretch` | 62 % | 116 % |
| `letter-spacing` | +0,06 em (6,91 px a 115,17 px) | −0,035 em (−4,03 px) |
| `xPercent` | linha 1: −6 % · linha 2: +6 % · linha 3: −6 % | 0 |
| `opacity` | 0,25 | 1 |
| Janela | topo do título a 92 % da tela → topo a 34 % | |
| Suavização | `scrub: 0.8` | |
| Cascata | 0,12 entre linhas (a 3.ª linha fica um pouco atrás) | |

Medição intermediária (400 px antes da seção): linha 1 em 102,5 % e opacidade 0,82; linha 2 em 89,75 % e 0,64; linha 3 em 76,75 % e 0,46. **OBSERVADO.**

## 4. Tipografia (EXATO)

`820 var(--fecho)/0.9 Archivo`, `font-stretch: 116%`, `letter-spacing: −0.035em`, `text-transform: uppercase`. Linhas em `display: block; white-space: nowrap`. Fundo da seção: `radial-gradient(70vmax 40vmax at 50% 0%, rgba(251,120,30,.14), transparent 70%)`, `radial-gradient(60vmax 40vmax at 90% 100%, rgba(63,114,212,.1), transparent 70%)` sobre `var(--aco-0)`, com brasas em canvas (FUN-02).

## 5. Movimento reduzido

`iniciarFecho` não roda. As linhas aparecem na forma final (116 %), já no tamanho ajustado. **EXATO.**

## 6. Como adaptar

- Precisa de uma fonte variável com `wdth` (Archivo, Roboto Flex, Anybody, Bricolage Grotesque etc.). Carregue o intervalo completo do eixo: na CDC, `Archivo:wdth,wght@62..125,100..900`.
- Sempre meça na largura **final** (116 %) para a linha mais longa nunca vazar.
- Chame o ajuste de novo quando as fontes terminarem de carregar e a cada redimensionamento (`refreshInit`).
