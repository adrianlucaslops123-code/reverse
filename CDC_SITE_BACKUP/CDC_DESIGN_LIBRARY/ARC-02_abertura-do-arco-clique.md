# ARC-02 · "Abrir o arco": clique no logo (clarão, explosão, tremor, som)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (sequência capturada a 90 ms, 340 ms e 1 240 ms do clique) |
| Portabilidade | Depende de ARC-01 (é um comportamento do sistema de partículas). O clarão em CSS (`.hero__flash`) e o tremor são reutilizáveis sozinhos |
| Gatilho | Clique (botão principal) ou toque no hero, **fora** de links, botões e campos, com a câmera ainda perto do início (`saida < 0,2`) |
| Arquivos de origem | `src/fogo/particulas.js` (`abrirArco`, ramo `if (clique)` e `if (apertado)` em `passo`, shaders `VERT_CLARAO`/`FRAG_CLARAO`) · `src/main.js` (`aoArco`) · `src/estilo/topo.css` (`.hero__flash`) · `src/motor/som.js` (`efeitos.arco`) |
| Dependências | three.js 0.186.1, GSAP 3.15.0 (flash CSS e tremor), Web Audio API (opcional) |

## 1. O que acontece, em ordem

No **quadro seguinte** ao `pointerdown`:

1. **Clarão WebGL** (ponto único, mistura aditiva) no ponto do cursor, em z = 0,6 (na frente do logo).
2. **Explosão**: todos os pontos a menos de **3,0 unidades** do cursor (≈ 181 px em 1440×900, CALCULADO) recebem um impulso para fora, mais forte no centro, e ficam incandescentes.
3. **Chuva de faíscas**: 240 faíscas com força 11 (ficha ARC-03).
4. **Clarão em CSS** sobre a tela (camada `.hero__flash`, `mix-blend-mode: screen`) centrado na projeção do ponto do clique.
5. **Tremor do palco** (só no clique do usuário).
6. **Som do arco**, se o som estiver ligado (SOM-01).

Enquanto o botão continua apertado, uma força contínua **mantém o buraco aberto** e continua aquecendo a borda. Ao soltar, a mola puxa o metal de volta e ele esfria.

## 2. Parâmetros

| Etapa | Parâmetro | Valor | Confiab. |
|---|---|---|---|
| Alcance | `raioArco` | 3,0 unidades | EXATO |
| Explosão | impulso | `f = (1 − d/3) × 24 × (0,6 + random × 0,8)` na direção radial (x, y) | EXATO |
| | impulso em z | `(random × 1,6 − 0,3) × f × 0,7` (a maioria vem para a frente) | EXATO |
| | calor imposto | `calor = max(calor, 1 − d/3)` (branco no centro) | EXATO |
| | velocidade máxima | 24 × 1,4 = 33,6 un/s ≈ 2 030 px/s (1440×900) | CALCULADO |
| Segurar | força contínua | `(1 − d/3) × 80 × dt`, radial | EXATO |
| | aquecimento contínuo | `+ (1 − d/3) × 2,4·dt × 0,6` | EXATO |
| Clarão WebGL | tamanho do sprite | `min(alturaTela, largura) × pixelRatio × 0,9` → 810 px em 1440×900, DPR 1 | EXATO, CALCULADO |
| | intensidade inicial | 1,0 (clique) · 0,6 (arco automático de abertura) | EXATO |
| | decaimento | `força *= e^(−11·dt)` → meia-vida ≈ 63 ms, −95 % em ≈ 272 ms | EXATO, CALCULADO |
| | perfil | `a = (e^(−5d²) + 0,35·e^(−60d²)) × força`. Halo largo mais um núcleo duro | EXATO |
| | cor | `vec3(0,86; 0,94; 1,0)` ≈ `#DBF0FF` (branco-azulado), aditiva, `depthTest:false`, `depthWrite:false` | EXATO, CALCULADO |
| Faíscas | quantidade e força | 240 com força 11 (clique) · 140 com força 8 (abertura automática) | EXATO |
| Clarão CSS | opacidade inicial `--flash` | 0,9 (clique) · 0,55 (abertura) | EXATO |
| | animação | `gsap.fromTo(flash, {'--flash': v}, {'--flash': 0, duration: 0.9, ease: 'expo.out', overwrite: true})` | EXATO |
| | gradiente | `radial-gradient(40vmax 34vmax at var(--fx) var(--fy), rgba(214,236,255,.85), rgba(120,180,255,.25) 40%, transparent 72%)` | EXATO |
| | posição | `--fx`, `--fy` = projeção do ponto do arco na tela, em % | EXATO |
| Tremor | deslocamento | `gsap.fromTo(palco, {x: 7, y: -4}, {x: 0, y: 0, duration: 0.45, ease: 'elastic.out(1.2, 0.25)', overwrite: true})`, só com `forte = true` | EXATO |

## 3. Sequência observada (site publicado)

| Instante após `pointerdown` | O que se vê | Confiab. |
|---|---|---|
| ~90 ms | Clarão branco-azulado cobrindo quase todo o logo. Pontos próximos brancos. Halo azul-acinzentado grande (camada CSS) | OBSERVADO |
| ~340 ms (ainda apertado) | Buraco aberto em volta do cursor. Anel de pontos brancos e amarelos na borda. Clarão já apagado | OBSERVADO |
| ~1 240 ms (900 ms depois de soltar) | Buraco fechando. Metal laranja-amarelo esfriando. Restam poucos pontos brancos | OBSERVADO |

## 4. Arco automático de abertura

- Uma vez, quando o relógio das partículas passa de **2,15 s** (e sem movimento reduzido): `abrirArco(0,6; −0,2; forte = false)`.
- Diferenças em relação ao clique: clarão 0,6, 140 faíscas de força 8, flash CSS 0,55, **sem tremor**, **sem explosão** dos pontos (a explosão só existe no ramo `clique && ativo`).
- Toca o som "arco" se o som estiver ligado. **EXATO.**

## 5. Regras de disparo

- `pointerdown` ignora botões que não sejam o principal (`e.button !== 0`) e alvos dentro de `a, button, input, select, textarea`. Clicar em "Ver treinamentos e valores" não abre o arco. **EXATO.**
- O clique só vale se `ativo` (mouse dentro do hero, posição projetada válida e `saida < 0,2`). Rolando mais de 20 % da saída do hero, o clique não faz nada. **EXATO.**
- No celular, o toque no logo também abre o arco. A dica do hero muda para "Toque no logo para abrir o arco". **EXATO.**

## 6. Como reproduzir só o clarão e o tremor (sem partículas)

```html
<div class="palco"></div>
<div class="flash" aria-hidden="true"></div>
```

```css
.flash { position:absolute; inset:0; pointer-events:none; opacity: var(--flash, 0); mix-blend-mode: screen;
  background: radial-gradient(40vmax 34vmax at var(--fx, 50%) var(--fy, 40%), rgba(214,236,255,.85), rgba(120,180,255,.25) 40%, transparent 72%) }
```

```js
function arco(xPct, yPct, forte = true) {
  flash.style.setProperty('--fx', `${xPct}%`)
  flash.style.setProperty('--fy', `${yPct}%`)
  gsap.fromTo(flash, { '--flash': forte ? 0.9 : 0.55 }, { '--flash': 0, duration: 0.9, ease: 'expo.out', overwrite: true })
  if (forte) gsap.fromTo(palco, { x: 7, y: -4 }, { x: 0, y: 0, duration: 0.45, ease: 'elastic.out(1.2, 0.25)', overwrite: true })
}
```

## 7. Como adaptar

- Cor do clarão: `vec3(0,86; 0,94; 1,0)` no shader e as duas cores do gradiente CSS. Na CDC é o azul do arco elétrico (`--arco: #a8d8ff`).
- Intensidade: 0,9 é forte. Para um projeto discreto, use 0,4–0,5 e duração de 0,6 s.
- O tremor de 7 px é perceptível sem incomodar. Acima de ~12 px vira "terremoto" (recomendação, não medida).
- Acessibilidade: o clarão é desligado com o movimento reduzido (as partículas não têm física). Mantenha isso em qualquer reutilização, porque clarões fortes podem incomodar pessoas fotossensíveis.
