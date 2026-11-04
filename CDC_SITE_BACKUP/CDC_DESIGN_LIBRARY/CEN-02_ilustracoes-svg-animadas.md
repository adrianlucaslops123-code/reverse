# CEN-02 · Ilustrações técnicas em SVG com linha do tempo própria (8 ilustrações)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (estados finais de "Teórica", "Acompanhamento" e "Recertificação" vistos) |
| Portabilidade | O desenho é específico da CDC. As técnicas (desenhar traço, ponto seguindo curva com leitura, lupa com recorte, carimbo, ponteiro) são reutilizáveis |
| Arquivos de origem | `index.html` (SVGs inline, `viewBox="0 0 480 320"`) · `src/cenas/provas.js` (`ANIMACOES`, `desenharTraco`) · `src/estilo/provas.css` (bloco "ilustrações (SVG)") |
| Dependências | GSAP 3.15.0 |

## 1. Moldura comum (`.prova__fig`, EXATO)

- `padding: clamp(14px, 2vw, 26px)`, raio 18 px, fundo `radial-gradient(120% 90% at 50% 0%, #121a23, #0b0f14 70%)`, contorno `fio` + sombra `0 40px 80px -50px #000`.
- **Marcas de canto de visor**: `::before` com `inset: 12px` e 8 gradientes lineares de 14 × 1 px e 1 × 14 px em cada canto (`var(--fio-forte)`).
- Legenda: `500 11px/1` mono, caixa alta, `letter-spacing .12em`, `var(--texto-3)`, alinhada à direita.
- Textos SVG: `500 13px` mono, `var(--texto-2)`. `.ilus__leg` 12 px `var(--texto-3)`. `.ilus__cota` 15 px `var(--brasa-quente)`.

## 2. Ajudante `desenharTraco` (EXATO)

Mede `getTotalLength()`, define `strokeDasharray = strokeDashoffset = L` e anima `strokeDashoffset → 0` em 0,9 s `power2.inOut`, cascata de 0,18 s.

## 3. As 8 linhas do tempo (EXATO)

| Prova | Desenho | Animação |
|---|---|---|
| `teorica` | folha de respostas: 5 linhas com 5 bolhas (r 9) e marcações laranja (r 6, brilho) | linhas entram de x −12 com opacidade 0 (0,5 s `power2.out`, cascata 0,08) → marcações de `scale 0` a 1 (0,5 s `back.out(3)`, cascata 0,22, começa 0,1 s antes do fim) |
| `documentos` | duas chapas com chanfro, seta de referência, bandeira de campo (triângulo laranja), cota "6" e "EPS" | chapas sobem 10 px (0,5 s) → traços se desenham (`desenharTraco`) → cotas e legenda aparecem (0,4 s, cascata 0,1) |
| `termico` | gráfico de tratamento térmico (aquecimento, patamar, resfriamento) | um ponto percorre a curva em **3,2 s** linear, desenhando o traço atrás dele. A **leitura de temperatura** acompanha: `temp = round(25 + (250 − y) × 575 / 155)` °C (escala de exemplo: y 250 → 25 °C, y 95 → 600 °C), posicionada a (+12, −14) do ponto. Legendas aparecem a partir de 0,3 s |
| `acompanhamento` | 3 colunas (Antes, Durante, Depois) com 3 itens cada e uma linha de progresso | itens entram de x −10 (0,4 s, cascata 0,07) → vistos se desenham (0,3 s, cascata 0,16) → ponto corre de x 40 a 440 em 1,6 s `power1.inOut` (começa em 0,4 s) |
| `visual` | cordão de solda com escamas (padrão SVG) e lupa com recorte (`clipPath`). Dentro da lente o cordão aparece mais claro (`#56636f`) e mostra poros e uma mordedura, que não aparecem fora dela (não há ampliação, só a troca de camada) | lupa vai de x 120 a 172 (1,1 s `power2.inOut`) → rótulo "porosidade" aparece (0,3 s) → pausa de 0,3 s → lupa vai a 314 (1,3 s) → rótulo "mordedura". O cabo da lupa é recalculado a cada quadro: `M(x+44) 204 L(x+90) 250` |
| `dureza` | chapa com 3 impressões: redonda, ovalizada (marcada com X) e redonda | cada batida "carimba" (de `scale 1.6` e opacidade 0 para 1, 0,45 s `expo.out`) a cada 0,75 s, com legenda 0,2 s depois. O X da batida ovalizada se desenha em 0,35 s |
| `estufas` | estufa verde com 7 eletrodos, mostrador e termômetro | eletrodos crescem de baixo (`scaleY 0`, 0,5 s `back.out(2)`, cascata 0,06) → termômetro enche (`scaleX` 0 → 1, 1,6 s `power2.inOut`) junto com o ponteiro girando de −120° a 70° em volta de (190, 246) → brilho interno pisca (opacidade 1, 0,6 s, `yoyo`, 3 repetições, `sine.inOut`) |
| `recertificacao` | linha com 3 etapas: Visual de ajuste de junta · Inspeção durante a soldagem · Visual final de solda | etapas sobem 12 px (0,5 s, cascata 0,12) → etapa 1 acende → linha laranja enche até a metade (0,9 s) → etapa 2 → enche o resto (0,9 s) → etapa 3. "Acesa" = círculo laranja com brilho `drop-shadow(0 0 10px rgba(251,120,30,.8))` |

Cada vez que a prova volta a ficar ativa, a linha do tempo anterior é descartada (`kill`) e uma nova começa do zero.

## 4. Paleta própria das ilustrações (EXATO)

| Uso | Valor |
|---|---|
| Linhas de grade e contornos | `rgba(168,194,222,.28)` (`--linha`) |
| Papel | `#10161d` |
| Chapa | `#18202a` |
| Cordão | `#3b4652` (ampliado `#56636f`), escamas `rgba(10,13,17,.6)` |
| Estufa | `#0f3b2c` com contorno `#1d6b4e`, porta `#0a1f18`, mostrador com contorno `#6fb898` |
| Eletrodos | `#a9b4bf`, 5 px |
| Destaques | `--brasa`, `--brasa-quente`, `#fff3dc` (ponto que corre, com `drop-shadow 0 0 8px rgba(255,178,74,.95)`) |

## 5. Como adaptar

- Técnica "ponto que percorre a curva com leitura numérica": `path.getPointAtLength(p × L)` a cada `onUpdate`, com uma escala linear entre y e o valor exibido.
- Técnica "lupa": `clipPath` com o mesmo círculo da lente e, dentro do recorte, uma cópia mais clara do desenho com os detalhes que só a lente revela. Mova os dois `cx` juntos. Para ampliar de verdade, aplique `transform: scale()` na cópia, com origem no centro da lente (adaptação, não existe no site).
