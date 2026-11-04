# CEN-05 · Depoimentos: carrossel com troca automática e fala que entra palavra por palavra

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (estado inicial "1 de 3" capturado). Troca automática: EXATO, não cronometrada |
| Portabilidade | Direta |
| Arquivos de origem | `src/cenas/depoimentos.js` · `src/estilo/secoes.css` (bloco "depoimentos") · `index.html` (linhas 518–542) |
| Dependências | GSAP 3.15.0 + SplitText + ScrollTrigger |

## 1. Estrutura e estilo (EXATO)

- `.falas` é uma grade com todas as falas na mesma célula (`grid-area: 1 / 1`). Só a `.is-ativa` fica visível (`opacity` e `visibility`, transição de 0,6 s).
- Citação: `600 clamp(28px, 3.8vw, 60px)/1.1` Archivo 102 %, `letter-spacing −0.02em`, `max-width: 30ch`. Aspas de abertura "“" em brasa, a 1,8 em, como `::before` (altura 0,5 em).
- Autor: nome 18 px em negrito e status (`500 12px` mono, caixa alta, `.12em`, `--brasa-quente`).
- Controles: setas circulares de 52 px (BOT-01 §5) e posição "**1** de 3" (`500 13px` mono, `tabular-nums`, `aria-live="polite"`).

## 2. Comportamento (EXATO)

| Item | Valor |
|---|---|
| Troca automática | a cada **7 s**, só com a seção na tela (`top 70%` → `bottom 30%`) e sem pausa. Não há troca automática no movimento reduzido |
| Pausa | mouse sobre a seção (`pointerenter`) ou foco dentro dela (`focusin`). Volta com `pointerleave` / `focusout` |
| Setas | anterior / próximo, em ciclo |
| Teclado | caixa com `tabindex="0"`: ← e → |
| Arrastar | diferença horizontal de mais de **50 px** entre `pointerdown` e `pointerup` (esquerda = próximo) |
| Entrada da fala nova | palavras de `y: 18`, opacidade 0, `blur(6px)` para o lugar, 0,8 s `expo.out`, cascata de 0,025 s |
| Entrada do autor | de `x: −14`, opacidade 0, 0,7 s `expo.out`, atraso de 0,3 s |
| Som | "passe" (se ligado) |
| Acessibilidade | `aria-roledescription="carrossel"` na caixa e `"depoimento"` em cada fala |

## 3. Conteúdo

3 depoimentos reais (texto literal em `CDC_SITE_MASTER_SPECIFICATION.md`, §8): Geraldo Feliciano Ferreira (Aprovado no exame), Maurilio Knop (Recertificado), Oswaldo Teles (Recertificado).

## 4. Como adaptar

Funciona com qualquer número de falas. Para falas longas, reduza o `clamp` para `24px, 3vw, 44px`.
