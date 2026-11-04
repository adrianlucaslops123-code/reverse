# FUN-02 · Brasas subindo devagar (canvas 2D determinístico)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (brasas visíveis atrás do fecho, no computador e no celular) |
| Portabilidade | Direta. É um módulo isolado, sem dependências |
| Onde aparece | Fundo da seção 11 "Contato" (`.contato__palco`, opacidade 0,9) |
| Arquivos de origem | `src/fogo/brasas.js` · `src/estilo/fim.css` (`.contato__palco`) |

## 1. Parâmetros (EXATO)

| Item | Valor |
|---|---|
| Quantidade | 140 brasas |
| Gerador | `mulberry32` com **semente 2005** (o ano de fundação). A cena é **sempre a mesma** ao recarregar |
| Posição inicial | x e y aleatórios na área (0–1). As que renascem entram por baixo (y 1,05–1,15) |
| Raio | 0,6–2,4 (o halo desenhado tem raio × 5, ou seja 3–12 px) |
| Subida | 0,012–0,047 da altura por segundo |
| Ondulação | `x += sin(t·0,8 + fase) × amplitude`, amplitude 0,004–0,016 da largura |
| Calor | 0,4–1,0, perde 0,04 por segundo. Renasce ao sair por cima ou com calor ≤ 0,05. Vida pelo calor: 8,8 a 23,8 s, então a maioria renasce embaixo antes de cruzar a seção (CALCULADO) |
| Cintilação | `brilho = calor × (0,65 + 0,35 × sin(t × pisca + fase))`, `pisca` de 2 a 7 rad/s |
| Desenho | `createRadialGradient` por brasa: `rgba(255,214,150, .9·b)` no centro → `rgba(251,120,30, .45·b)` a 25 % → transparente. Mistura `globalCompositeOperation = 'lighter'` |
| Resolução | `min(DPR, 2)`. Redimensiona por `ResizeObserver` |
| Laço | `requestAnimationFrame` com `dt` ≤ 0,05 s. Só desenha quando a seção está na tela (`IntersectionObserver`) e o portal está fechado |
| Movimento reduzido | desenha **um quadro parado** quando a seção entra na tela |

## 2. Como reproduzir

```js
import { brasas } from './brasas.js'
const fundo = brasas({ alvo: document.querySelector('.contato__palco'), quantidade: 140, reduzido })
// fundo.destruir()
```

CSS: `.contato__palco { position: absolute; inset: 0; pointer-events: none; opacity: .9 } .contato__palco canvas { display:block; width:100%; height:100% }`.

## 3. Como adaptar

Troque as duas cores do gradiente (bolhas, pólen, neve, poeira de luz). Para um fundo mais calmo, use 60–80 brasas e cintilação de 1 a 3 rad/s.
