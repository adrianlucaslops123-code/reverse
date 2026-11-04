# CUR-01 · Cursor próprio (ponto exato + anel com atraso)

> Ficha da **CDC Design Library**. Legenda de confiabilidade: **EXATO** (lido no código) · **CALCULADO** (derivado de fórmula do código) · **OBSERVADO** (medido no site publicado, Chromium 1440×900, DPR 1) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado**, com **uma divergência observada** (o estado "apertado" não encolhe o anel; ver §10) |
| Portabilidade | Direta. Trocar só cores e fontes (tokens) |
| Onde aparece | Página inteira, exceto quando o portal da área do aluno ou o pop-up de redes está aberto |
| Arquivos de origem | `src/motor/interacao.js` (bloco `// ---------- cursor ----------`, linhas 22–60) · `src/estilo/base.css` (bloco `/* ---------- cursor ---------- */`, linhas 110–131) · `index.html` (linha 39) · `src/estilo/aluno.css` linha 38 · `src/estilo/redes.css` (últimas 3 regras) |
| Dependências | GSAP 3.15.0 (`gsap.quickSetter`, `gsap.quickTo`, `gsap.set`) |
| Fichas relacionadas | CUR-02 (rótulo contextual "ABRIR"), ARC-01 (o anel de calor sobre o logo), BOT-02 (magnetismo) |

## 1. O que é

O cursor do sistema é escondido e substituído por **duas peças independentes**:

1. **Ponto**: um círculo de 6 px que segue o ponteiro **sem atraso**, com `mix-blend-mode: difference`, por isso muda de cor conforme o fundo.
2. **Anel**: um círculo de contorno fino de 1 px que segue o ponteiro **com inércia** (0,38 s, `power3.out`). Ele muda de tamanho e de preenchimento conforme o elemento sob o mouse e pode exibir um rótulo de texto (ficha CUR-02).

> **Nota de fidelidade (importante):** o código **não desenha** uma "ponta de arco elétrico" no cursor. O conjunto é só ponto + anel. O efeito de "ponta incandescente" que se vê sobre o logo do hero vem das **partículas do logo aquecidas sob o cursor** (ficha ARC-01). O cursor apenas muda para o estado de calor (anel de 120 px). Sobre botões laranja, o ponto aparece **azul** (efeito `difference`, ver §3). Isso pode ser lido como "faísca azul de arco", mas não existe desenho de ponta de arco no código. A única peça em forma de ponta luminosa do sistema é a ponta do cordão de solda (ficha ROL-01).

## 2. Estrutura (HTML)

```html
<div class="cursor" aria-hidden="true">
  <i class="cursor__ponto"></i>
  <i class="cursor__anel"><span class="cursor__rotulo"></span></i>
</div>
```

Posição no documento: logo depois do `<div class="grao">`, antes do `.cordao` e do `<header class="nav">`.

## 3. Geometria e cores

| Peça | Propriedade | Valor | Confiab. |
|---|---|---|---|
| `.cursor__ponto` | largura × altura | 6 × 6 px | EXATO |
| | margem (centraliza no ponteiro) | `-3px 0 0 -3px` | EXATO |
| | cor | `var(--texto)` = `#eef1f4` | EXATO |
| | mistura | `mix-blend-mode: difference` | EXATO |
| | cor resultante sobre `#07090c` (fundo) | ≈ `#e7e8e8` (quase branco) | CALCULADO |
| | cor resultante sobre `#fb781e` (botão brasa) | `#0d79d6` (azul) | CALCULADO, OBSERVADO |
| `.cursor__anel` (repouso) | largura × altura | 38 × 38 px | EXATO |
| | margem | `-19px 0 0 -19px` | EXATO |
| | contorno | `box-shadow: inset 0 0 0 1px rgba(238,241,244,.5)` (1 px por dentro) | EXATO |
| | fundo | transparente | EXATO |
| | layout interno | `display:grid; place-items:center` (centraliza o rótulo) | EXATO |
| Ambos | `position: fixed; left:0; top:0; z-index: 95; pointer-events:none; border-radius:50%` | | EXATO |

Camadas: o cursor (z 95) fica acima da navegação (z 50), do menu (z 45), do cordão (z 40), do grão de filme (z 90) e do portal (z 80). Fica abaixo só do aviso/toast (z 96), da abertura `.carga` (z 99) e do link "pular" (z 100). **EXATO.**

## 4. Movimento

| Item | Valor | Confiab. |
|---|---|---|
| Ponto: método | `gsap.quickSetter(ponto, 'x'/'y', 'px')`. Aplica a posição no mesmo evento, sem interpolação | EXATO |
| Anel: método | `gsap.quickTo(anel, 'x'/'y', { duration: 0.38, ease: 'power3.out' })` | EXATO |
| Latência do anel (salto de 400 px) | 54 % do caminho em ~57 ms · 77 % em ~107 ms · 90 % em ~157 ms · 96,5 % em ~207 ms · 99 % em ~257 ms · 100 % em ~307 ms | OBSERVADO |
| Posição inicial | centro da janela (`innerWidth/2`, `innerHeight/2`), oculto (`is-oculto`) até o primeiro `pointermove` de mouse | EXATO |
| Evento | `pointermove` na `window`, `{ passive: true }`. Ignora `pointerType !== 'mouse'` (caneta e toque não movem o cursor) | EXATO |
| Transformação aplicada | `transform: translate(Xpx, Ypx)` (o GSAP também grava `translate:none; rotate:none; scale:none` inline) | OBSERVADO |

## 5. Estados e transições

A cada `pointermove` o código decide o estado, nesta **ordem de prioridade**:

| Prioridade | Classe em `.cursor` | Condição (exata) | Anel | Rótulo |
|---|---|---|---|---|
| 1 | `is-rotulo` | `alvo.closest('[data-cursor]')` existe | 76 × 76 px, margem −38 px, fundo `var(--brasa)` `#fb781e`, sem contorno | visível (opacidade 1), texto = `data-cursor` |
| 2 | `is-link` | sem rótulo e `alvo.closest('a, button, summary, label, select')` | 58 × 58 px, margem −29 px, contorno `inset 0 0 0 1px var(--brasa)`, fundo transparente | oculto |
| 3 | `is-calor` | sem rótulo, sem link, `alvo.closest('.hero__palco, .hero')` **e** `scrollY < innerHeight × 0,5` | 120 × 120 px, margem −60 px, contorno `inset 0 0 0 1px rgba(255,178,74,.55)`, fundo `radial-gradient(circle, rgba(255,178,74,.12), transparent 70%)` | oculto |
| 4 | (nenhuma) | demais casos | 38 px, contorno branco 50 % | oculto |
| modificador | `is-apertado` | entre `pointerdown` e `pointerup` (qualquer botão do mouse, em qualquer lugar) | CSS pede `scale: .8`, mas **não tem efeito** (ver §10) | n/a |
| modificador | `is-oculto` | `document` `pointerleave` ou `window` `blur`. Sai no próximo `pointermove` de mouse | `opacity: 0` imediata (não há `transition` em `.cursor`) | n/a |

Transições do anel (valores EXATOS):

- `width`, `height`, `margin`: **0,35 s** `var(--entrada)` = `cubic-bezier(0.16, 1, 0.3, 1)`. A margem anima junto, então o anel cresce **a partir do centro**.
- `background`: **0,3 s** (curva padrão `ease`).
- `box-shadow`: **0,3 s** (`ease`).
- Rótulo (`.cursor__rotulo`): `opacity` **0,2 s** (`ease`).

Comportamento ao **sair** de um elemento com rótulo: o texto do rótulo **não é apagado**. Ele só some por opacidade (0,2 s) enquanto o anel encolhe (0,35 s). Ao entrar em outro elemento com rótulo, o texto troca na hora. **OBSERVADO** (depois de sair do botão de som, o rótulo continuava "Som", com opacidade 0).

## 6. Interação especial com o logo CDC (hero)

- Sobre o hero (fora de links e botões) e com a página no topo (`scrollY < 50 % da altura da janela`), o anel vira o **anel de calor** de 120 px. O diâmetro do anel corresponde ao alcance do "maçarico" das partículas: raio 1,05 unidade do mundo 3D ≈ **63,5 px** em 1440×900 (CALCULADO), ou seja ≈ 127 px de diâmetro. Por isso o anel de 120 px praticamente contorna a área que aquece.
- O cursor em si não aquece nada. O aquecimento é feito pelo sistema de partículas, que lê o mesmo `pointermove` no elemento `.hero` (ficha ARC-01).
- Durante o clique no hero, o "arco" (clarão, explosão, faíscas) é desenhado pelas partículas (ficha ARC-02). O anel continua no estado de calor.
- `.hero__palco` tem `cursor: crosshair` como reserva. Com o cursor próprio ativo, vira `cursor: none` (`html.tem-cursor .hero__palco`).
- Logo da navegação (`.nav__marca`): por ser um `<a>`, o anel vai para `is-link` (58 px, contorno laranja). Ao mesmo tempo o logo ganha `filter: drop-shadow(0 0 8px rgba(251,120,30,.8))` com transição de 0,3 s (`topo.css`). **EXATO.**

## 7. Quando o cursor próprio existe (responsividade, toque e movimento reduzido)

| Condição | Resultado | Confiab. |
|---|---|---|
| `matchMedia('(hover: hover) and (pointer: fine)')` verdadeiro **e** sem `prefers-reduced-motion: reduce` | `html.tem-cursor`. O cursor do sistema some com `cursor: none !important` em `html` e em `*` | EXATO |
| Campos `input`, `textarea`, `select` | voltam a `cursor: text !important` (o anel próprio continua por cima) | EXATO |
| Toque (`hover: none`), celular e tablet | sem cursor próprio (`.cursor { display:none }`) | EXATO, OBSERVADO (iPhone 13, iPad) |
| Movimento reduzido | sem cursor próprio, cursor do sistema normal | EXATO, OBSERVADO |
| Portal da área do aluno aberto (`html.portal-aberto`) | `.cursor{display:none}`, cursor do sistema volta | EXATO |
| Pop-up de redes aberto (`html.redes-aberto`) | `.cursor{display:none}`, `cursor:auto` em tudo, `pointer` nos links e botões do pop-up | EXATO |
| Resolução | os diâmetros (6/38/58/76/120 px) **não mudam** com a largura da tela nem com o DPR | EXATO |

## 8. Desempenho

- Um único `pointermove` passivo e duas propriedades de `transform` por peça. Não há leitura de layout dentro do evento, além de `closest()` nos ancestrais.
- As mudanças de estado animam `width/height/margin`, o que provoca layout e pintura só no anel, que é um elemento `fixed` isolado. Custo baixo. **ESTIMATIVA.**
- Sem `will-change` declarado. **EXATO.**

## 9. Acessibilidade

- `aria-hidden="true"` no contêiner.
- O foco por teclado não depende do cursor. `:focus-visible` usa `outline: 2px solid var(--arco)` (`#a8d8ff`) com `outline-offset: 3px`.
- O cursor próprio é desligado no movimento reduzido.

## 10. Divergências e efeitos colaterais observados (não corrigir no site, só registrar)

1. **`is-apertado` não encolhe o anel.** O CSS diz `.cursor.is-apertado .cursor__anel { scale: .8 }`, mas o GSAP grava `scale: none` inline no anel (estilo inline vence a regra). Medido: classe presente, `scale` computado = `none`, largura continua 120 px. **OBSERVADO.** Uma reconstrução fiel ao **comportamento** não deve encolher o anel. Uma reconstrução fiel à **intenção do código** aplicaria o `scale .8` (por exemplo animando `scale` com o próprio GSAP). Registre a escolha.
2. O tamanho do anel não acompanha a forma do alvo (é sempre um círculo).

## 11. Como reproduzir

1. Coloque o HTML do §2 no fim do `<body>` (ou no início, como no original).
2. CSS (copiado do original):

```css
.cursor { display: none }
html.tem-cursor .cursor { display: block }
html.tem-cursor:not(.portal-aberto), html.tem-cursor:not(.portal-aberto) * { cursor: none !important }
html.tem-cursor:not(.portal-aberto) input, html.tem-cursor:not(.portal-aberto) textarea, html.tem-cursor:not(.portal-aberto) select { cursor: text !important }
.cursor__ponto, .cursor__anel { position: fixed; z-index: 95; left: 0; top: 0; pointer-events: none; border-radius: 50% }
.cursor__ponto { width: 6px; height: 6px; margin: -3px 0 0 -3px; background: var(--texto); mix-blend-mode: difference }
.cursor__anel {
  width: 38px; height: 38px; margin: -19px 0 0 -19px;
  box-shadow: inset 0 0 0 1px rgba(238, 241, 244, 0.5);
  display: grid; place-items: center;
  transition: width 0.35s var(--entrada), height 0.35s var(--entrada), margin 0.35s var(--entrada), background 0.3s, box-shadow 0.3s;
}
.cursor__rotulo { font: 500 10px/1 var(--mono); letter-spacing: 0.1em; text-transform: uppercase; color: var(--brasa-texto); opacity: 0; transition: opacity 0.2s }
.cursor.is-link .cursor__anel { width: 58px; height: 58px; margin: -29px 0 0 -29px; box-shadow: inset 0 0 0 1px var(--brasa) }
.cursor.is-rotulo .cursor__anel { width: 76px; height: 76px; margin: -38px 0 0 -38px; background: var(--brasa); box-shadow: none }
.cursor.is-rotulo .cursor__rotulo { opacity: 1 }
.cursor.is-calor .cursor__anel { width: 120px; height: 120px; margin: -60px 0 0 -60px; box-shadow: inset 0 0 0 1px rgba(255, 178, 74, 0.55); background: radial-gradient(circle, rgba(255, 178, 74, 0.12), transparent 70%) }
.cursor.is-apertado .cursor__anel { scale: 0.8 }
.cursor.is-oculto { opacity: 0 }
```

3. JS (essência do original, `interacao.js`):

```js
const fino = matchMedia('(hover: hover) and (pointer: fine)').matches
if (fino && !reduzido) {
  html.classList.add('tem-cursor')
  const pX = gsap.quickSetter(ponto, 'x', 'px'), pY = gsap.quickSetter(ponto, 'y', 'px')
  const aX = gsap.quickTo(anel, 'x', { duration: 0.38, ease: 'power3.out' })
  const aY = gsap.quickTo(anel, 'y', { duration: 0.38, ease: 'power3.out' })
  gsap.set([ponto, anel], { x: innerWidth / 2, y: innerHeight / 2 })
  cursor.classList.add('is-oculto')
  addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return
    cursor.classList.remove('is-oculto')
    pX(e.clientX); pY(e.clientY); aX(e.clientX); aY(e.clientY)
    const alvo = e.target.closest ? e.target : null
    const comRotulo = alvo?.closest('[data-cursor]')
    const link = alvo?.closest('a, button, summary, label, select')
    const calor = !link && alvo?.closest('.hero__palco, .hero')
    cursor.classList.toggle('is-rotulo', !!comRotulo)
    cursor.classList.toggle('is-link', !comRotulo && !!link)
    cursor.classList.toggle('is-calor', !comRotulo && !link && !!calor && scrollY < innerHeight * 0.5)
    if (comRotulo) rotulo.textContent = comRotulo.dataset.cursor
  }, { passive: true })
  addEventListener('pointerdown', () => cursor.classList.add('is-apertado'))
  addEventListener('pointerup', () => cursor.classList.remove('is-apertado'))
  document.addEventListener('pointerleave', () => cursor.classList.add('is-oculto'))
  addEventListener('blur', () => cursor.classList.add('is-oculto'))
}
```

4. Tokens necessários: `--texto`, `--brasa`, `--brasa-texto`, `--mono`, `--entrada` (ver `CDC_DESIGN_SYSTEM.md`).

## 12. Como adaptar a outra identidade

- Troque `--brasa` (cor de destaque do link e do rótulo) e `--brasa-texto` (texto do rótulo).
- O estado `is-calor` é específico do hero da CDC. Num projeto sem cena interativa, remova a linha `calor` ou aponte o seletor para a área "quente" do novo projeto, mantendo a regra de só ativar perto do topo, se fizer sentido.
- Para um projeto minimalista, mantenha só ponto + anel de repouso + `is-link`.
- Não aumente a duração do anel acima de ~0,5 s: o atraso começa a parecer "arrastado" (recomendação de uso, não medida).
