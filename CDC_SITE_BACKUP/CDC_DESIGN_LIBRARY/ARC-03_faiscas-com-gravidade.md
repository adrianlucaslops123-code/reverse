# ARC-03 · Faíscas com gravidade, rastro e quique no chão

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, parcialmente validado**: a sequência do clique foi observada (ARC-02), mas as faíscas não foram isoladas nem medidas nas capturas. Os valores abaixo são EXATOS do código |
| Portabilidade | Direta para qualquer cena three.js (o bloco é independente do logo). Em 2D, ver o §6 |
| Arquivos de origem | `src/fogo/particulas.js`: bloco `// ---------- faíscas ----------` (estoque, `emitir`) e trecho `// faíscas` em `passo` · shaders `VERT_FAISCA` / `FRAG_FAISCA` |
| Dependências | three.js 0.186.1 (`LineSegments`, `ShaderMaterial`, `AdditiveBlending`) |

## 1. O que é

Riscos curtos de luz (segmentos de linha) que nascem num ponto, sobem, caem com gravidade, perdem velocidade no ar, **quicam no "chão"** logo abaixo do logo e se apagam. A cor vai do branco-amarelado (vivas) ao laranja (morrendo). A cabeça de cada risco é opaca e a cauda é transparente.

## 2. Três fontes de emissão

| Fonte | Quando | Quantidade | Força | Velocidade herdada | Confiab. |
|---|---|---|---|---|---|
| Arco (clique) | `pointerdown` válido (ARC-02) | 240 | 11 | 0 | EXATO |
| Arco de abertura | relógio > 2,15 s, uma vez | 140 | 8 | 0 | EXATO |
| **Esmerilhar** (passe rápido) | por quadro, se `ativo`, **mais de 20 pontos** sob o cursor **e** velocidade do mouse > 6 un/s | `min(6, round((rapidez − 6) × 0,35))` | `4 + rapidez × 0,12` | `vx0 = −mvx × 0,15`, `vy0 = −mvy × 0,05` (saem para trás do movimento) | EXATO |

A velocidade de 6 un/s ≈ 363 px/s em 1440×900. O máximo de 6 faíscas por quadro é atingido a partir de ≈ 21,7 un/s ≈ 1 310 px/s. **CALCULADO.**

## 3. Física (por faísca, por quadro)

| Etapa | Fórmula / valor | Confiab. |
|---|---|---|
| Estoque | anel circular de **1 400** faíscas (computador) ou **700** (celular). Cada emissão reaproveita a próxima posição | EXATO |
| Direção inicial | ângulo `a` aleatório. `vx = cos(a)·f + vx0`, `vy = sobe·f + vy0`, `vz = sin(a)·f·0,7 + 1,5`, com `sobe ∈ [0,25; 1,15]` e `f = força × [0,35; 1,10]` | EXATO |
| Gravidade | 16 un/s² (≈ 968 px/s² em 1440×900) | EXATO, CALCULADO |
| Arrasto do ar | `v *= e^(−0,9·dt)` nos 3 eixos | EXATO |
| Chão | `y = −altura_do_logo/2 − 0,3` = −2,861 un. (no espaço do logo) | EXATO, CALCULADO |
| Quique | ao cruzar o chão descendo: `y = chão`, `vy *= −0,32`, `vx, vz *= 0,7` | EXATO |
| Vida | começa em 1. Perde `1/(0,45 + random × 1,1)` por segundo → dura **0,45 a 1,55 s** | EXATO, CALCULADO |
| Rastro | segmento da posição atual até `posição − velocidade × 0,03` (30 ms de trajetória) | EXATO |
| Laço | só roda enquanto houver faíscas vivas (`faiscasVivas > 0`) | EXATO |

## 4. Aparência (shader)

- **Cor**: `mix((1,00; 0,36; 0,05), (1,00; 0,95; 0,82), vida²)` → de `#FF5C0D` (fim da vida) a `#FFF2D1` (início). **CALCULADO.**
- **Alfa**: `vida × mix(0,1; 1,0; cabeça)`. O vértice da cabeça tem `aCab = 1` e o da cauda `aCab = 0`, o que cria o degradê ao longo do risco.
- **Saída**: cor pré-multiplicada (`cor × alfa`), `AdditiveBlending`, `depthWrite: false`. Faíscas sobrepostas somam luz.
- Some junto com o logo na saída do hero (`uSome`, ARC-04).
- Espessura: linha WebGL de 1 px (o `LineSegments` padrão não tem largura configurável). **EXATO** (não há `linewidth` no material).

## 5. Como reproduzir (three.js)

Copie o bloco do original. Esqueleto:

```js
const NF = 1400
const fPos = new Float32Array(NF*3), fVel = new Float32Array(NF*3), fVida = new Float32Array(NF), fQueda = new Float32Array(NF)
const fVert = new Float32Array(NF*6), fVidaVert = new Float32Array(NF*2), fCab = new Float32Array(NF*2)
for (let i = 0; i < NF; i++) fCab[i*2] = 1            // cabeça = 1, cauda = 0
// geometria LineSegments com atributos position (fVert), aVida (fVidaVert), aCab (fCab)
function emitir(x, y, z, n, forca, vx0 = 0, vy0 = 0) { /* ver §3 */ }
// por quadro: gravidade 16, arrasto e^(-0.9dt), quique -0.32 no chão, vida -= queda·dt,
// rastro: [pos, pos - vel·0.03]
```

## 6. Versão 2D (adaptação, não existe no site)

Os mesmos números funcionam num `canvas` 2D se a unidade for convertida em pixels: multiplique distâncias e velocidades por ~60 (o fator px/un da CDC em 1440×900). Desenhe cada faísca com `lineTo` e `globalCompositeOperation = 'lighter'`. Isso é uma **adaptação proposta**, não um recurso implementado.

## 7. Como adaptar a outra identidade

- Cores: as duas cores do `FRAG_FAISCA` (laranja de fim, creme de início).
- Para "pó mágico" em vez de solda: gravidade 2–4, arrasto 2, sem quique.
- Para chuva de metal mais pesada: gravidade 24, quique −0,2, vida 0,3–0,9 s.
- Mantenha o estoque fixo (anel). Não crie objetos por faísca.
