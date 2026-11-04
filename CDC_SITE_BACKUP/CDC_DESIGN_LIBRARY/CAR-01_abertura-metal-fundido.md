# CAR-01 · Abertura: o logo enche de metal fundido enquanto a página carrega

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado**, com **uma variação de tempo observada** no contador (§5) |
| Portabilidade | Direta. Troque a máscara do logo e o texto do rodapé da tela |
| Arquivos de origem | `src/motor/carga.js` · `index.html` (bloco `<div class="carga">`, linhas 32–36) · `src/estilo/topo.css` (bloco "abertura (carga)") · `src/main.js` (`abrir({ tarefas: [document.fonts.ready, logoPronto] })`) |
| Dependências | GSAP 3.15.0 · `public/marca/cdc-mascara.png` |

## 1. O que é

Uma cortina preta de tela cheia mostra o logotipo da CDC como silhueta de aço escuro. Ele **se enche de metal fundido de baixo para cima** conforme as fontes e o logo de partículas ficam prontos. Um contador de três dígitos (000 → 100) acompanha. No fim, o logo brilha, cresce 8 % e a cortina **recolhe de baixo para cima** revelando a página.

## 2. Estrutura e estilo

```html
<div class="carga" aria-hidden="true">
  <div class="carga__marca"><i class="carga__fundido"></i></div>
  <p class="carga__info"><span>CDC · Capacitação em Qualidade</span><span class="carga__num">000</span></p>
</div>
```

| Peça | Valor | Confiab. |
|---|---|---|
| `.carga` | `position: fixed; inset: 0; z-index: 99; display: grid; place-items: center; background: var(--aco-0)` (`#07090c`); `pointer-events: none` | EXATO |
| `.carga__marca` | largura `min(46vw, 340px)`, `aspect-ratio: 1400/717` (340 × 174 px em telas largas), fundo `rgba(168,194,222,.08)`, recortado pela máscara do logo (`mask: url(/marca/cdc-mascara.png) center / contain no-repeat`) | EXATO |
| `.carga__fundido` | ancorado embaixo, `height: calc(var(--carga) * 100%)`. Gradiente `to top: var(--brasa-escura) → var(--brasa) 40% → var(--brasa-quente) 85% → #fff4dc`. Brilho na superfície do metal: `box-shadow: 0 -2px 18px 2px rgba(255,210,140,.9)` | EXATO |
| `.carga__info` | rodapé da tela: `left/right: var(--gutter)`, `bottom: 28px + safe-area`, `display:flex; justify-content: space-between`. `500 12px/1 IBM Plex Mono`, `letter-spacing .14em`, caixa alta, `var(--texto-2)` | EXATO |
| `.carga__num` | `var(--texto)`, `font-variant-numeric: tabular-nums`, 3 dígitos (`padStart(3,'0')`) | EXATO |

## 3. Lógica de progresso (EXATO)

| Fase | Ação |
|---|---|
| Início | anda sozinho até **30 %** em 0,9 s (`power2.out`), "para nunca parecer travado" |
| Cada tarefa concluída | vai para `0,3 + (feitas/total) × 0,6` em 0,6 s (`power2.out`, `overwrite: true`). Com 2 tarefas: 60 % e depois 90 % |
| Tarefas | `document.fonts.ready` e "logo de partículas pronto" (primeiro quadro desenhado) |
| Tempo mínimo | 1,0 s (`Promise.all([tudo, espera(1000)])`) |
| Tempo máximo | 3,2 s (`Promise.race([..., espera(3200)])`): passa mesmo se algo travar |
| Final (linha do tempo) | `estado.p → 1` em 0,45 s (`power2.inOut`) · `.carga__marca` → `scale 1.08` e `filter: drop-shadow(0 0 28px rgba(255,178,74,.9))` em 0,35 s (`power2.out`) · **aqui a página é liberada** (`ok()`: rolagem, entrada do hero, montagem das partículas) · depois de +0,05 s a cortina vai a `clip-path: inset(0% 0% 100% 0%)` em **1,0 s** `expo.inOut` · ao mesmo tempo o logo sobe 60 px e some (`opacity 0`, 0,6 s, `power2.in`) |
| Fim | o elemento `.carga` é removido do DOM |

Clip-path medido durante a subida: `inset(0 0 5,28%)` → `inset(0 0 53,3%)` → `inset(0 0 93,4%)`. A cortina é cortada **de baixo para cima**, como uma persiana subindo. **OBSERVADO.**

## 4. Quando não aparece

- Sem JavaScript (`html:not(.js)`) ou com `html.sem-carga`: `display: none`. **EXATO.**
- Movimento reduzido: `sem-carga` e espera as tarefas por no máximo 1,5 s cada (`Promise.race([t, espera(1500)])`). **EXATO, OBSERVADO.**
- Rede de segurança em `main.js`: se em **8 s** nada tiver terminado, `com-movimento` é removido para nada ficar escondido. **EXATO.**

## 5. Variação observada no contador

No ambiente de verificação, o logo ficou pronto **depois** do tempo mínimo de 1 s. O contador subiu até 095, **voltou para 090** e a cortina subiu mostrando 090. Ele não chegou a 100. **OBSERVADO.**

Causa (lida no código): a animação "+ uma tarefa → 90 %" (0,6 s, `overwrite: true`) e a animação final "→ 100 %" (0,45 s) correm juntas sobre a mesma variável. A final termina primeiro e a de 90 % termina depois, deixando 90. Em máquinas rápidas, em que o logo fica pronto antes de 1 s, o contador deve chegar a 100. Esse caso **não foi verificado**.

## 6. Como reproduzir

Copie `carga.js`, o HTML do §2 e o CSS de `topo.css`. Uso:

```js
abrir({ tarefas: [document.fonts.ready, cenaPronta], reduzido }).then(() => {
  // a cortina começou a subir: ligue rolagem, entradas e cenas aqui
})
```

## 7. Como adaptar a outra identidade

- Troque a máscara (`mask: url(...)`) pelo logotipo do projeto e o `aspect-ratio` pela proporção dele.
- O gradiente do "líquido" pode ser água (azul → ciano → branco), tinta, luz etc. Mantenha o brilho na superfície (`box-shadow` negativo em y).
- Mantenha o mínimo de 1 s e o máximo de ~3 s. Menos do que isso parece um piscar. Mais do que isso irrita.
