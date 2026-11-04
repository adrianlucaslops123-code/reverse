# TIP-02 · Blocos que surgem do desfoque, em lotes (`data-surgir`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** |
| Portabilidade | Direta |
| Onde aparece | Todos os `[data-surgir]` fora do hero: rótulos de seção, parágrafos de introdução, números, cartões, itens de lista, formulário, canais de contato |
| Arquivos de origem | `src/motor/texto.js` (`ScrollTrigger.batch`) · `src/cenas/hero.js` (versão do hero) · `src/estilo/base.css` (`html.com-movimento [data-surgir] { opacity: 0 }`) |
| Dependências | GSAP 3.15.0 + ScrollTrigger |

## 1. Parâmetros (EXATO)

| Item | Seções | Hero (`entradaHero`) |
|---|---|---|
| Estado inicial | `opacity 0`, `y 26px`, `filter: blur(8px)` | `opacity 0`, `y 22px`, `blur(8px)` |
| Estado final | `opacity 1`, `y 0`, `blur(0)` | igual |
| Duração | 1,05 s | 1,1 s |
| Curva | `expo.out` | `expo.out` |
| Cascata | 0,09 s dentro de cada lote | 0,1 s, com atraso de 0,45 s |
| Gatilho | `ScrollTrigger.batch(..., { start: 'top 90%', once: true })`: os elementos que entram juntos na tela formam um lote | logo após a abertura |
| Limpeza | `clearProps: 'filter'` (remove o `filter` no fim, para não pesar na composição) | igual |
| Alvos no hero | n/a | `.selo`, `[data-surgir]` (texto e botões), `.hero__lema`, `.hero__rolar` |

## 2. Por que em lotes

`ScrollTrigger.batch` junta os elementos que cruzam a linha de 90 % no mesmo instante. Uma grade de cartões entra em cascata da esquerda para a direita, e um item que entra sozinho anima sozinho, sem esperar os outros. **EXATO** (comportamento documentado do `batch`).

## 3. Movimento reduzido

Não roda e os elementos ficam visíveis (o CSS de opacidade 0 só vale com `html.com-movimento`). **EXATO.**

## 4. Como adaptar

- 26 px de subida com 8 px de desfoque é a assinatura "sair da névoa". Para uma marca mais sóbria: 16 px e 4 px de desfoque.
- Evite `blur` acima de 10 px em blocos grandes no celular: o custo de pintura cresce com a área (recomendação).
