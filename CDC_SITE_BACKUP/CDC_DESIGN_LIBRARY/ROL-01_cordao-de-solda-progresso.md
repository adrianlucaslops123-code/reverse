# ROL-01 · Cordão de solda: indicador de progresso da rolagem (o "scroll de eletrodo")

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (medido em 9 posições de rolagem, de 0 % a 100 %) |
| Portabilidade | Direta. A metáfora (cordão + ponta incandescente) é da CDC. A técnica serve para qualquer barra vertical de progresso |
| Onde aparece | Fixo na borda direita, centrado na vertical. Só aparece depois de 60 % de uma altura de janela rolada. Oculto em telas de até 760 px |
| Arquivos de origem | `index.html` (linhas 41–45) · `src/estilo/base.css` (bloco "progresso: cordão de solda", linhas 133–154) · `src/motor/rolagem.js` (`ligarRolagem`, `onUpdate`) |
| Dependências | GSAP ScrollTrigger (só para ler o progresso). O desenho é 100 % CSS |

## 1. O que é

Um **cordão de solda** desce por um trilho conforme a página rola. A parte já "soldada" é cinza-aço, com escamas como um cordão real. Perto da ponta, as **cores de revenimento** (azul, roxo, bronze) aparecem e esquentam até o laranja. Na frente vai uma **ponta incandescente** que tremula, como o eletrodo em operação. Embaixo, um número de 00 a 100 mostra a porcentagem.

## 2. Estrutura

```html
<div class="cordao" aria-hidden="true">
  <div class="cordao__trilho"><i class="cordao__solda"></i><i class="cordao__ponta"></i></div>
  <span class="cordao__num">00</span>
</div>
```

## 3. Geometria (desktop)

| Peça | Propriedade | Valor | Confiab. |
|---|---|---|---|
| `.cordao` | posição | `fixed`, `right: calc(18px + env(safe-area-inset-right))`, `top: 50%`, `translate: 0 -50%`, `z-index: 40`, `pointer-events: none` | EXATO |
| | layout | coluna (`flex-direction: column`), `align-items: center`, `gap: 12px` | EXATO |
| | caixa medida em 1440×900 | x 1407, y 286, 15 × 329 px (22,5 px de largura com "100") | OBSERVADO |
| `.cordao__trilho` | tamanho | **10 px × 34vh** (306 px em 900 px de altura) | EXATO, OBSERVADO |
| | forma e cor | `border-radius: 6px`, `background: rgba(168,194,222,.07)` | EXATO |
| `.cordao__solda` | altura | `calc(var(--p) * 100%)`, onde `--p` é o progresso de 0 a 1 | EXATO |
| | gradiente (de cima para baixo) | `#56616d 0` → `#7d8995` em `100% − 90px` → `--revenido-azul #3f72d4` em `100% − 64px` → `--revenido-roxo #6c4f9e` em `100% − 46px` → `--revenido-bronze #a8632e` em `100% − 28px` → `--brasa #fb781e` em `100% − 10px` → `--brasa-quente #ffb24a` em `100%` | EXATO |
| | máscara (escamas) | camada 1: `radial-gradient(ellipse 6px 4.5px at 50% 100%, #000 92%, transparent) 0 0 / 10px 7px repeat-y` (uma "escama" elíptica a cada **7 px**) · camada 2: `linear-gradient(#000, #000) 50% 0 / 4px 100% no-repeat` (alma contínua de **4 px** no centro) | EXATO |
| `.cordao__ponta` | tamanho | 9 × 9 px, círculo, `margin: -5px 0 0 -4.5px`, `left: 50%`, `top: calc(var(--p) * 100%)` | EXATO |
| | cor e brilho | `#fff6e0`. `box-shadow: 0 0 10px 3px rgba(255,178,74,.9), 0 0 26px 8px rgba(251,120,30,.45)` | EXATO |
| `.cordao__num` | texto | `500 11px/1 IBM Plex Mono`, `var(--texto-2)`, `letter-spacing .08em`, `tabular-nums` | EXATO |

**Como as cores "andam":** as paradas do gradiente são relativas à **altura atual** do cordão (`100% − Npx`). Por isso a faixa de revenimento (os últimos 90 px) acompanha sempre a ponta, e o resto do cordão fica cinza, como metal que já esfriou. **CALCULADO** a partir do CSS e conferido na captura de 50 %.

## 4. Animação

| Item | Valor | Confiab. |
|---|---|---|
| Fonte do progresso | `ScrollTrigger.create({ start: 0, end: 'max' })`, `self.progress` com 4 casas (`--p`) | EXATO |
| Número | `String(Math.round(progress × 100)).padStart(2, '0')` → 00…100 | EXATO, OBSERVADO |
| Frequência de atualização | a cada `onUpdate` do ScrollTrigger (cada quadro em que a rolagem muda; com Lenis, cada quadro do *ticker* do GSAP durante a rolagem) | EXATO |
| Suavização própria | nenhuma: o cordão acompanha a rolagem já suavizada pelo Lenis | EXATO |
| Tremulação da ponta | `animation: tremer .12s steps(2) infinite`. A 50 %, as sombras caem para `0 0 7px 2px rgba(255,178,74,.8), 0 0 20px 6px rgba(251,120,30,.35)`. Ciclo de 8,33 Hz, com troca brusca de estado (*steps*) | EXATO, CALCULADO |
| Aparecer e sumir | `opacity` 0 → 1 com transição de **0,6 s** quando `html.is-rolou` (`scrollY > 0,6 × innerHeight`) | EXATO, OBSERVADO |

Relação rolagem → progresso: linear sobre a altura **total** rolável (incluindo os espaçadores das cenas presas). Em 1440×900 a altura rolável é **21 556 px**: 1 % de cordão ≈ 216 px de rolagem e 1 px de cordão ≈ 70 px de rolagem. **OBSERVADO, CALCULADO.**

Medições (1440×900):

| `scrollY` | progresso | número | altura do cordão | topo da ponta |
|---|---|---|---|---|
| 1 700 | 0,0789 | 08 | 24,1 px | 305 |
| 4 099 | 0,1902 | 19 | 58,2 px | 339 |
| 10 778 | 0,5000 | 50 | 153 px | 434 |
| 17 007 | 0,7890 | 79 | 241,4 px | 522 |
| 21 556 | 1,0000 | 100 | 306 px | 587 |

(OBSERVADO)

## 5. Responsividade e diferentes alturas de tela

- O trilho tem **34 % da altura da janela**: 245 px em 720 px, 306 px em 900 px, 490 px em 1 440 px. **CALCULADO.**
- `max-width: 760px` → `.cordao { display: none }`. **EXATO, OBSERVADO** (iPhone).
- Com o portal da área do aluno aberto: escondido (`html.portal-aberto .cordao { display: none }`). **EXATO.**
- Movimento reduzido: o cordão continua funcionando, mas a ponta **não tremula** (`animation: none`). **EXATO.**

## 6. Como reproduzir

CSS do §3 (copiar de `base.css`) mais:

```js
ScrollTrigger.create({
  start: 0, end: 'max',
  onUpdate(self) {
    cordao.style.setProperty('--p', self.progress.toFixed(4))
    num.textContent = String(Math.round(self.progress * 100)).padStart(2, '0')
    document.documentElement.classList.toggle('is-rolou', scrollY > innerHeight * 0.6)
  },
})
```

Sem GSAP: `p = scrollY / (document.documentElement.scrollHeight − innerHeight)` num `scroll` passivo com `requestAnimationFrame`.

## 7. Como adaptar a outra identidade

- **Mesma técnica, outra metáfora:** a máscara repetida (`repeat-y` com `background-size: 10px 7px`) cria a textura e as paradas "relativas à ponta" criam o rastro de cor. Exemplos: um pavio aceso (cinza → brasa), um rastro de tinta, uma trilha de luz.
- Troque as 7 cores do gradiente e a cor da ponta.
- Mantenha `pointer-events: none` e `aria-hidden`: é decorativo, o número não é lido por leitores de tela.
