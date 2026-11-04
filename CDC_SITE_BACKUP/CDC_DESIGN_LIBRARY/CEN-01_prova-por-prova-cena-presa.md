# CEN-01 · "Prova por prova": cena presa que troca um módulo por passo de rolagem

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (provas 1, 4 e 8 capturadas, com contador e barras do índice) |
| Portabilidade | Direta para qualquer conteúdo em N passos (o código lê `.prova` e `.provas__indice li`) |
| Arquivos de origem | `src/cenas/provas.js` (`iniciarProvas`) · `src/estilo/provas.css` · `index.html` (seção `#provas`, linhas 221–428) |
| Dependências | GSAP 3.15.0 + ScrollTrigger + ScrambleTextPlugin |

## 1. Dois modos (`gsap.matchMedia`, EXATO)

| Modo | Condição | Comportamento |
|---|---|---|
| **Preso** | `(min-width: 901px) and (min-height: 620px) and (prefers-reduced-motion: no-preference)` | A cena fica presa. Uma prova visível por vez. Troca a cada 0,7 altura de janela |
| **Lista** | `(max-width: 900px), (max-height: 619px), (prefers-reduced-motion: reduce)` | Provas empilhadas. Cada ilustração anima uma vez quando o topo dela chega a 80 % da tela (sem animação no movimento reduzido) |

## 2. Modo preso: estrutura e geometria (EXATO)

- `html.provas-presas` ativa o CSS do modo.
- Palco com `height: 100svh`, `display: flex; flex-direction: column`, `padding-top: clamp(92px, 12vh, 130px)`, `padding-bottom: 96px`.
- Cabeça: grade `1fr auto` com rótulo "04 Prova por prova", título "Cada prova tem um método." e contador à direita: `<b>01</b> / 08`. O número tem `800 clamp(40px, 4vw, 64px)/0.8` Archivo 112 %. O "/ 08" tem `500 14px` mono, `var(--texto-3)`.
- Lista: `position: relative; flex: 1`. Cada `.prova` com `position: absolute; inset: 0; visibility: hidden` e `.is-ativa { visibility: visible }`.
- Prova: grade de 2 colunas `0.95fr / 1.05fr`, `gap: clamp(28px, 5vw, 80px)`, centrada na vertical. Ilustração com `max-height: calc(100svh − 440px)` e `min-height: 220px`.
- **Índice** no rodapé do palco: 8 colunas iguais, `gap 8px`, `bottom: 34px`. Cada item tem `500 11px/1.2` mono, `var(--texto-3)`, reticências, `padding-top: 14px`, uma linha de 2 px (`var(--fio)`) e, por cima, a **barra que enche**: `width: calc(var(--enchido) * 100%)`, `linear-gradient(90deg, --brasa, --brasa-quente)`, brilho `0 0 10px rgba(251,120,30,.7)`. Item ativo com texto `var(--texto)`.

## 3. Rolagem → prova (EXATO)

```js
ScrollTrigger.create({
  trigger: palco, start: 'top top', end: () => `+=${n * 0.7 * innerHeight}`,   // n = 8
  pin: true, anticipatePin: 1,
  onUpdate(self) {
    const p = self.progress * n
    itens.forEach((li, k) => li.style.setProperty('--enchido', clamp(p - k, 0, 1).toFixed(3)))
    const i = clamp(Math.floor(p), 0, n - 1)
    if (i !== atual) mostrar(i, i > atual ? 1 : -1)
  },
})
```

| Medida | Valor | Confiab. |
|---|---|---|
| Comprimento da trava | 8 × 0,7 × altura da janela = 5,6 telas (5 040 px em 900 px; espaçador de 5 940 px) | EXATO, OBSERVADO |
| Rolagem por prova | 0,7 tela (630 px em 900 px) | CALCULADO |
| Barras do índice | enchem continuamente: no meio da prova 4, `--enchido` = 1, 1, 1, 0,5, 0, 0, 0, 0 | OBSERVADO |
| Clique num item do índice | rola até o **meio** do trecho da prova: `start + (k + 0,5)/n × (end − start)`, com `irPara` (1,7 s) | EXATO |

## 4. Transição entre provas (`mostrar(i, sentido)`, EXATO)

`sentido` = +1 descendo, −1 subindo.

| Elemento | Saída (prova anterior) | Entrada (prova nova) |
|---|---|---|
| Textos (`.prova__texto > *`) | `y: −28 × sentido`, opacidade 0, `blur(6px)`, 0,32 s `power2.in`, cascata de 0,025 s | de `y: 40 × sentido`, opacidade 0, `blur(10px)` para o lugar, 0,95 s `expo.out`, cascata de 0,06 s, atraso de 0,18 s |
| Ilustração (`.prova__fig`) | opacidade 0, `scale: 0.97`, 0,34 s `power2.in`. No fim perde `.is-ativa` (se não for a atual) | de opacidade 0, `scale: 1.04`, `clip-path: inset(0% 0% 100% 0% round 18px)` para opacidade 1, `scale: 1`, `inset(0% 0% 0% 0% round 18px)`: **revela de cima para baixo**, 1,05 s `expo.inOut`, atraso de 0,1 s. No fim inicia a animação da ilustração (CEN-02) |
| Contador | `scrambleText` com dígitos, 0,5 s, `speed: 1` | |
| Índice | `.is-ativa` no item da prova | |
| Som | "virada" (se ligado) | |

Os textos saem **para cima** ao descer e **para baixo** ao subir. A entrada vem do lado oposto. A sensação é de "folhear" na direção da rolagem.

## 5. Conteúdo (as 8 provas)

01 Teórica · 02 Documentos técnicos · 03 Tratamento térmico · 04 Acompanhamento de soldagem (dado: **95%** de aprovação) · 05 Visual e dimensional · 06 Dureza · 07 Estufas e consumíveis (dado: **99%**) · 08 Recertificação. Textos literais em `CDC_SITE_MASTER_SPECIFICATION.md`, §8.

## 6. Responsividade

| Viewport | Modo | Confiab. |
|---|---|---|
| 1440×900, 1280×720, 2560×1440, 1024×768 | preso | OBSERVADO |
| 768×1024 (tablet em pé), 390×664 (celular) | lista | OBSERVADO |
| Altura < 620 px (ex.: notebook com a janela baixa) | lista | EXATO |
| ≤ 760 px de altura no modo preso | títulos menores: `h3` `clamp(30px, 3vw, 46px)` e parágrafos com 15 px | EXATO |

## 7. Como reproduzir

Copie `provas.css` (modo preso e modo lista) e `iniciarProvas` com `ANIMACOES` (CEN-02). A marcação precisa de `.provas__palco`, `.provas__indice li` (um por passo), `.provas__contador b` e `.prova[data-prova]` com `.prova__texto` e `.prova__fig svg`.

## 8. Como adaptar

- Funciona para "passo a passo", "módulos", "etapas de serviço" etc. Mude `0.7` para dar mais ou menos rolagem por passo.
- Com mais de ~10 passos, o índice de rodapé fica apertado. Troque por pontos ou por uma linha contínua.
