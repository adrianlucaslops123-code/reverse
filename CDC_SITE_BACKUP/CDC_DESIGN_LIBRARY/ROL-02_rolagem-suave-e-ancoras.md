# ROL-02 · Rolagem suave (Lenis) sincronizada com o ScrollTrigger, e âncoras internas

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (`html.lenis` presente no computador e ausente no toque) |
| Portabilidade | Direta |
| Arquivos de origem | `src/motor/rolagem.js` (`criarRolagem`, primeiro bloco de `ligarRolagem`) · `src/estilo/base.css` (regras `.lenis`) · `src/main.js` |
| Dependências | Lenis 1.3.27 · GSAP 3.15.0 + ScrollTrigger |

## 1. Configuração (EXATO)

```js
if (!reduzido && !toque) {
  lenis = new Lenis({ lerp: 0.085, wheelMultiplier: 0.95, smoothWheel: true })
  lenis.on('scroll', ScrollTrigger.update)
  gsap.ticker.add((tempo) => lenis.raf(tempo * 1000))
  gsap.ticker.lagSmoothing(0)
}
ScrollTrigger.config({ ignoreMobileResize: true })
```

| Parâmetro | Valor | Efeito |
|---|---|---|
| `lerp` | 0,085 | a cada quadro a posição percorre 8,5 % da distância até o alvo. A 60 fps chega a 90 % em ~26 quadros (≈ 0,43 s), CALCULADO |
| `wheelMultiplier` | 0,95 | a roda do mouse anda 5 % menos que o padrão |
| `smoothWheel` | `true` | suaviza só a roda. O toque nunca usa Lenis neste site |
| Relógio | o *ticker* do GSAP alimenta o Lenis (um único `requestAnimationFrame` para tudo) | sincronia exata entre rolagem e animações |
| `lagSmoothing(0)` | desligado | o GSAP não "pula" tempo depois de travadas |
| `ignoreMobileResize` | `true` | a barra de endereço do celular não recalcula os gatilhos |

**Quando não há Lenis:** toque (`hover: none`) ou movimento reduzido. Nesses casos a rolagem é nativa. **EXATO, OBSERVADO.**

CSS de apoio (EXATO):

```css
html.lenis, html.lenis body { height: auto }
.lenis.lenis-smooth { scroll-behavior: auto !important }
.lenis.lenis-stopped { overflow: clip }
```

Áreas com rolagem própria usam `data-lenis-prevent`: corpo do portal, painel do leitor e páginas do leitor.

## 2. Ir para um ponto (`irPara`)

```js
lenis.scrollTo(alvo, { immediate, duration: 1.7,
  easing: (x) => (x < 0.5 ? 8 * x ** 4 : 1 - Math.pow(-2 * x + 2, 4) / 2) })
```

- **Duração: 1,7 s.** Curva: *ease-in-out quart* (aceleração x⁴ até a metade e desaceleração simétrica). **EXATO.**
- Sem Lenis: `scrollTo({ behavior: 'smooth' })` ou `scrollIntoView` (ou `'auto'` no movimento reduzido).
- Aceita elemento ou número em px. Exposto em `window.__rolagem` (usado pelo índice das provas).

## 3. Âncoras internas

- Um clique em qualquer `a[href^="#"]` com destino existente: `preventDefault`, fecha o menu do celular, rola com `irPara` (1,7 s), coloca `tabindex="-1"` no destino, dá foco sem rolar (`focus({ preventScroll: true })`) e toca o som "clique".
- Exceções capturadas antes por `portal.js`: `#area-comum…` e `#ler-…` abrem o portal (CEN-10).
- Abertura com *hash* na URL (ex.: `/#contato`): o navegador começa no topo (`history.scrollRestoration = 'manual'`, `scrollTo(0,0)`). Depois da abertura, o código salta direto ao destino (`irPara(destino, true)`). **EXATO.**

## 4. Travar a rolagem

`parar()`: `lenis.stop()` + `html { overflow: hidden }`. `seguir()`: o inverso. Usados durante a abertura, com o menu do celular aberto, com o portal aberto e com o pop-up de redes aberto.

## 5. "Hover desligado enquanto rola"

Cada atualização de rolagem coloca `html.is-rolando`, que é retirada **160 ms** depois da última atualização. Os links da navegação só reagem ao *hover* com `html:not(.is-rolando)`. Assim o cursor parado sobre a barra não "acende" links enquanto a página passa. **EXATO.**

## 6. Como adaptar

- `lerp` entre 0,07 (mais "pesado") e 0,12 (mais rápido). Fora disso fica mole demais ou quase nativo.
- Mantenha o Lenis desligado no toque: a rolagem nativa do celular já tem inércia.
