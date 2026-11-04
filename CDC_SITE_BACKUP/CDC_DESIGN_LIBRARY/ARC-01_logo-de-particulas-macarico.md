# ARC-01 · Logo de partículas de metal com "maçarico" (aquecimento pelo mouse)

> Legenda: **EXATO** (código) · **CALCULADO** (fórmula do código) · **OBSERVADO** (site publicado, Chromium headless com WebGL por software/SwiftShader, 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (montagem, aquecimento, inclinação e enquadramento observados) |
| Portabilidade | **Depende de adaptação**: precisa de uma máscara PNG do logotipo do novo projeto (branco sobre transparente) e da paleta de calor |
| Onde aparece | Hero (`section.hero#inicio`), dentro de `.hero__palco` |
| Arquivos de origem | `src/fogo/particulas.js` (inteiro) · `src/main.js` (bloco "logo de partículas") · `public/marca/cdc-mascara.png` (1400×717) · `src/estilo/topo.css` (`.hero__palco`, `.hero.sem-webgl`) |
| Dependências | three.js 0.186.1 (`WebGLRenderer`, `PerspectiveCamera`, `Points`, `LineSegments`, `ShaderMaterial`, `BufferGeometry`, `Raycaster`, `Plane`) |
| Fichas relacionadas | ARC-02 (arco no clique), ARC-03 (faíscas), ARC-04 (saída com a câmera), CAR-01 (abertura) |

## 1. O que é

O logotipo real da CDC vira uma **nuvem 3D de pontos quadrados**, em 7 camadas de profundidade, como uma peça de chapa. O mouse funciona como um **maçarico**: perto do cursor os pontos são empurrados, seguem o movimento do mouse e **aquecem** (laranja → amarelo → branco → azul do arco). Longe do cursor eles esfriam e voltam para casa por uma mola pouco amortecida ("ímã": passam do lugar e balançam). O bloco inteiro tomba suavemente na direção do cursor.

## 2. Amostragem da máscara (geração procedural)

Algoritmo `amostrar(img, alvoPontos)`:

1. Desenha a máscara num `canvas` 2D (`willReadFrequently: true`) e lê o canal alfa. "Cheio" = alfa > 127.
2. **Área**: percorre a imagem de 2 em 2 px e soma 4 por pixel cheio. Na máscara da CDC: 487 640 px² de tinta, 48,6 % da imagem. **CALCULADO.**
3. `L = 7` camadas. `pesoTotal = 2 + (L − 2) × 0,2 = 3` (as 2 faces são cheias e as 5 camadas do meio só têm borda, com peso estimado de 20 %).
4. `passo = max(1,4; √(área × pesoTotal / alvoPontos))` px. `borda = passo × 1,6`.
5. Grade de `passo` em `passo` px com jitter de ±35 % do passo (`(random − 0,5) × passo × 0,7`).
6. Um ponto é "de borda" se algum vizinho a `borda` px (direita, esquerda, baixo, cima) estiver vazio.
7. Para cada ponto da grade: camadas 0 e 6 (faces) sempre recebem ponto. As camadas 1 a 5 recebem só se for borda.
8. Coordenadas no mundo: largura do logo = **10 unidades**. `pxPorUnidade = 1400 / 10 = 140`. `x = (px − W/2)/140`, `y = −(py − H/2)/140`, `z = mix(−0,45; +0,45; l/6)` (espessura 0,9).

| Parâmetro | Computador | Celular (`(hover: none), (max-width: 760px)`) | Confiab. |
|---|---|---|---|
| `alvoPontos` (configuração) | 52 000 | 24 000 | EXATO |
| `passo` resultante | 5,304 px | 7,807 px | CALCULADO |
| Tamanho base do ponto (mundo) | 0,03789 | 0,05577 | CALCULADO |
| **Pontos realmente gerados** | **≈ 45 450 a 45 610** (varia com o jitter) | **≈ 23 250 a 23 430** | CALCULADO (algoritmo replicado sobre a máscara real, 3 sementes) |
| Altura do logo no mundo | 717/140 = 5,1214 | igual | CALCULADO |

> O README do projeto fala em "~50 mil partículas (24 mil no celular)". Esse é o valor configurado. O número real gerado é menor, ~45,5 mil no computador, por causa da ponderação das camadas.

## 3. Cor de cada ponto (cor "fria")

| Regra | Valor | Confiab. |
|---|---|---|
| Gradiente vertical (`v` = y/H) | `v < 0,45`: `#ffd38a` → `#fb781e`; depois `#fb781e` → `#b23a0c` | EXATO |
| Variação de luz | `luz = 0,9 + random × 0,2` | EXATO |
| Face da frente (camada 1,0, voltada para a câmera) | borda: `luz × 1,16` | EXATO |
| Face de trás (camada 0) | `lerp` para o aço `#2c3d52` em 62 %, `luz × 0,5` | EXATO |
| Camadas do meio (só borda) | `lerp` para o aço em 35 %, `luz × 0,72` | EXATO |
| Limite | cada canal `min(1, canal × luz)` | EXATO |

## 4. Shader dos pontos (cor quente, tamanho, forma)

**Vertex** (`VERT`): calor `t = clamp(aCalor, 0, 1)`.

- Tamanho: `gl_PointSize = clamp(aTam × uPx / profundidade × (1 + t × 0,75), 1, 24)` px. Com `uPx = alturaTela × pixelRatio / (2 × tan(fov/2))`.
- Em 1440×900, DPR 1: ponto frio ≈ **2,3 px**, ponto em brasa ≈ **4,1 px** (+75 %). **CALCULADO.**
- `aTam = tamanho × (0,85 + random × 0,35)`.
- Rampa de calor `rampa(t)` (cores lineares do shader convertidas para HEX):

| Faixa de `t` | De | Para | HEX aproximado |
|---|---|---|---|
| 0 → 0,40 | (1,00; 0,46; 0,10) | (1,00; 0,76; 0,32) | `#FF751A` → `#FFC252` |
| 0,40 → 0,82 | (1,00; 0,76; 0,32) | (1,00; 0,96; 0,84) | `#FFC252` → `#FFF5D6` |
| 0,82 → 1,00 | (1,00; 0,96; 0,84) | (0,84; 0,93; 1,00) | `#FFF5D6` → `#D6EDFF` (azul do arco) |

- Mistura com a cor fria: `mix(aCor, rampa(t), smoothstep(0, 0,28, t))`. Com 28 % de calor o ponto já está todo na rampa.
- Transparência: `smoothstep(0,35; 2,4; profundidade) × (1 − uSome)`. O ponto some quando chega muito perto da lente.

**Fragment** (`FRAG`): ponto **quadrado**. Descarta se `max(|x|, |y|) > 0,45` na coordenada do sprite (quadrado de 90 % do sprite). Sem textura, sem brilho próprio. `transparent: true`, mistura normal.

## 5. Câmera, enquadramento e responsividade

| Item | Valor | Confiab. |
|---|---|---|
| Câmera | `PerspectiveCamera(fov 32°, near 0,05, far 200)` | EXATO |
| Renderer | `WebGLRenderer({ antialias:false, alpha:true, powerPreference:'high-performance' })`, `setClearColor(0x000000, 0)` | EXATO |
| Pixel ratio | `min(devicePixelRatio, 2)` | EXATO, OBSERVADO (iPhone DPR 3 → canvas 780×1328 para 390×664) |
| Tela "deitada" (largura ≥ 900 e proporção ≥ 1,1) | o logo ocupa até **42 %** da largura e **46 %** da altura, centro em **(69 %, 44 %)** da tela | EXATO |
| Tela "em pé" ou estreita | ocupa até **84 %** da largura e **24 %** da altura, centro em **(50 %, 27 %)** | EXATO |
| Distância da câmera | `max(10/ocupaL/(2·tan16°·aspecto), 5,1214/ocupaA/(2·tan16°))` | EXATO |
| Em 1440×900 | distância 25,95. Visível 14,88 × 23,81 unidades. **60,5 px por unidade**. Logo com **605 px** de largura, centro em x = 994 px | CALCULADO, OBSERVADO (`--lema-x: 994px`) |
| Lema "Capacitação em qualidade" | posicionado pelo JS: `top = base do logo + 26 px`, `left = centro` (`--lema-y`, `--lema-x`). Em 1440×900: 577 px / 994 px | EXATO, OBSERVADO |
| Redimensionamento | `ResizeObserver` no palco chama `medir()` | EXATO |

## 6. Física do maçarico (função `passo(dt)`)

`dt` = tempo real do quadro limitado a **[1/240 s; 1/30 s]**. **EXATO.**

### 6.1 Constantes (`AJUSTE`, EXATO)

| Chave | Valor | Significado |
|---|---|---|
| `raio` | 1,05 un. (≈ 63,5 px em 1440×900, CALCULADO) | alcance do mouse |
| `pega` | 14 | quanto o ponto copia a velocidade do mouse (`1 − e^(−14·dt)`) |
| `empurra` | 22 | empurrão para fora do cursor |
| `aquece` | 2,4 /s | calor ganho por segundo sob o cursor |
| `esfria` | 1,1 s | constante de tempo do resfriamento (perde ~63 % em 1,1 s) |
| `mola` | 55 | rigidez da volta para casa |
| `atrito` | 2,6 | amortecimento (começa em 7 na abertura e cai para 2,6 em 3 s) |
| `inclina` | 0,32 rad | inclinação máxima do bloco para o cursor (≈ 18,3°) |

### 6.2 Por ponto, a cada quadro (equações exatas do código)

```
ativo = mouse dentro do hero && raio projetado ok && saida < 0,2
mv = velocidade do mouse no plano do logo (un/s), suavizada (k = 1 − e^(−18·dt)), limitada a ±60
se ativo e distância d < raio (1,05):
   f = (1 − d/raio)²
   v += (mv − v) · pega · f              // o "pente": copia o movimento do mouse
   e = 22 · f · dt
   v.xy += direção_para_fora · e ; v.z += e · 0,8
   calor = min(1, calor + f · 2,4·dt · (1 + |mv| · 0,08))   // mais rápido = mais quente
mola:   v = (v − deslocamento · 55·dt) · e^(−atrito·dt)
        deslocamento += v · dt
calor *= e^(−dt/1,1)
se |v|² > 4:  calor = max(calor, min(0,85; |v| · 0,035))    // ponto rápido brilha
respiração: z += 0,03 · sin(t·1,3 + x·0,7 + y·0,4)
```

| Grandeza derivada | Valor | Confiab. |
|---|---|---|
| Frequência natural da mola | √55 = 7,42 rad/s ≈ 1,18 Hz | CALCULADO |
| Fator de amortecimento (ζ) em regime | 2,6 / (2·7,42) ≈ **0,175** (sub-amortecida: passa do lugar e oscila) | CALCULADO |
| ζ na abertura (t = 0) | 7 / 14,84 ≈ 0,47 | CALCULADO |
| Respiração | amplitude 0,03 un. (≈ 1,8 px em 1440×900), período 2π/1,3 ≈ 4,8 s | CALCULADO |

### 6.3 Inclinação do bloco (mola com embalo)

- Com mouse ativo e movimento nos últimos **2,5 s**: alvo `rotY = ndc.x × 0,32`, `rotX = −ndc.y × 0,32 × 0,6`.
- Parado ou fora: balanço ocioso `rotY = sin(t·0,42) × 0,14`, `rotX = sin(t·0,31) × 0,05`.
- Mola: `vel += ((alvo − giro)·26 − vel·6,5)·dt`. ω = √26 ≈ 5,10 rad/s (0,81 Hz), ζ ≈ 0,64. **CALCULADO.**
- Rotação aplicada: `(giro.x·(1−s), giro.y·(1−s), s·0,2)`, onde `s` é a saída do hero (ARC-04).

### 6.4 Montagem inicial ("metal branco de quente chega espalhado e esfria no lugar")

- Cada ponto começa deslocado numa casca esférica de raio **6 a 16 unidades** (y × 0,6; z × 0,5 + 4, isto é, vem da frente).
- Calor inicial = 1 (branco-azulado). Esfria com τ = 1,1 s.
- Atraso individual: `0,05 + u × 0,75 + random × 0,55` s (u = posição horizontal 0 a 1). A montagem varre da **esquerda para a direita** entre 0,05 s e 1,35 s.
- O relógio só começa quando a cortina da abertura sobe (`logo.comecar()`, ficha CAR-01).
- Em **t > 2,15 s** acontece um "arco de abertura" automático, fraco, em (0,6; −0,2) do logo (ficha ARC-02).

## 7. Eventos de mouse e toque

| Evento | Onde | Efeito | Confiab. |
|---|---|---|---|
| `pointermove` (passivo) | `section.hero` | atualiza a posição em NDC, `dentro = true`, marca o último movimento | EXATO |
| `pointerdown` | `section.hero` | só botão principal (`button 0`) e **fora** de `a, button, input, select, textarea`: `apertado = true`, `clique = true` (ARC-02) | EXATO |
| `pointerleave` | `section.hero` | `dentro = false`, `apertado = false` | EXATO |
| `pointerup` / `pointercancel` | `window` | `apertado = false`. Em toque (`hover: none`) também `dentro = false` | EXATO |
| `blur` | `window` | como `pointerleave` | EXATO |
| Projeção do mouse | n/a | `Raycaster` da câmera contra o plano z = 0 **no espaço local do grupo** (já inclinado) | EXATO |
| Toque | `.hero__palco` | `touch-action: pan-y`: a rolagem vertical continua livre e o toque no logo aquece e abre o arco | EXATO |

## 8. Desempenho e laço

- Um `requestAnimationFrame` próprio. O loop **para de calcular** quando o palco sai da tela (`IntersectionObserver`), quando a saída do hero passa de 0,999 e quando o portal da área do aluno está aberto.
- Atributos dinâmicos (`position`, `aCalor`) com `DynamicDrawUsage`. Cor e tamanho são estáticos.
- `boundingSphere` fixa de raio 80, para evitar recalcular.
- **Qualidade adaptativa:** depois de t > 3 s, mede 120 quadros. Se a média passar de 25 ms (< 40 fps) e o DPR máximo for > 1, baixa para DPR 1 e remede. **EXATO.**
- FPS real no hardware do usuário: **NÃO IDENTIFICADO**. O ambiente de verificação usa WebGL por software, então a medição de FPS não é representativa.

## 9. Movimento reduzido e falhas

- `prefers-reduced-motion: reduce`: sem física e sem montagem. Os pontos são desenhados parados em casa e redesenhados só quando o tamanho muda. A saída do hero só altera a opacidade do canvas (`1 − saida`). **EXATO.**
- Sem WebGL (erro ao criar o renderer ou ao carregar a máscara): `hero.sem-webgl` mostra o logo como máscara CSS pintada com `linear-gradient(to bottom, #ffd38a, var(--brasa) 45%, #b23a0c)`, em `inset: 14% 22% auto; height: 46%`. **EXATO.**

## 10. Como reproduzir em outro projeto

1. Gere uma máscara PNG do logotipo: **branco sobre transparente**, ~1400 px de largura (o código só usa o alfa).
2. Copie `src/fogo/particulas.js` como está. Ele é autocontido e só importa `three`.
3. Chame:

```js
import { particulas } from './particulas.js'
const logo = await particulas({
  alvo: document.querySelector('.hero__palco'),  // recebe o <canvas>
  eventos: document.querySelector('.hero'),      // recebe os eventos do mouse
  mascara: new URL('marca/sua-mascara.png', document.baseURI).href,
  reduzido: matchMedia('(prefers-reduced-motion: reduce)').matches,
  aoPronto: () => {},                            // primeiro quadro desenhado
  aoMedir: ({ base, centro, estreita }) => {},   // para posicionar textos junto do logo
  aoArco: ({ x, y, forte }) => {},               // ver ARC-02
})
logo.comecar()        // inicia o relógio (montagem)
logo.saida(p)         // 0..1 ligado à rolagem (ARC-04)
logo.arco()           // dispara um arco no centro
logo.destruir()       // libera GPU e eventos
```

4. CSS mínimo: `.hero__palco { position:absolute; inset:0; touch-action: pan-y } .hero__palco canvas { display:block; width:100%; height:100% }`.

## 11. Como adaptar a outra identidade

- **Cores frias:** `AJUSTE.cores` (3 paradas, de cima para baixo) e `AJUSTE.aco` (tom das laterais e do fundo).
- **Rampa de calor:** as 4 cores `a, b, c, d` em `VERT`. Para outra marca, mantenha a lógica "cor da marca → claro → branco → acento frio" e troque os valores.
- **Densidade:** `pontosPC` e `pontosCel`. Mantenha a proporção ~2:1 para o celular.
- **Comportamento:** `raio`, `aquece`, `esfria`, `mola`, `atrito`. Para algo mais calmo: `atrito` 4–5 e `empurra` 12. Para algo mais elástico: `atrito` ~2.
- **Enquadramento:** `ocupaL`, `ocupaA`, `cx`, `cy` em `medir()` decidem onde o logo fica em relação ao texto.
