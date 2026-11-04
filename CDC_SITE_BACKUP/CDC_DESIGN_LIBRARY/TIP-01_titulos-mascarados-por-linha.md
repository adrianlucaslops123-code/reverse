# TIP-01 · Títulos que sobem por linha, saindo de uma máscara (`data-titulo`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (títulos visíveis depois da entrada em todas as capturas) |
| Portabilidade | Direta. Funciona com qualquer fonte |
| Onde aparece | Todos os elementos com `data-titulo`: o `h1` do hero e os `h2.titulo` das seções (Equipe, Treinamentos, Provas, Material, Estrutura, Área do aluno, Dúvidas, Aplicativo) |
| Arquivos de origem | `src/motor/texto.js` (`dividirTitulo`) · `src/cenas/hero.js` (entrada do `h1`) · `src/estilo/base.css` (estados iniciais) |
| Dependências | GSAP 3.15.0 + SplitText + ScrollTrigger |

## 1. Comportamento

O título é dividido em **linhas** e **palavras**. Cada linha vira uma máscara (`overflow: clip`). As palavras começam **118 % abaixo** da própria altura, giradas **3°**, e sobem para o lugar, em cascata de **40 ms** por palavra, com `expo.out` de **1,15 s**.

## 2. Parâmetros (EXATO)

```js
SplitText.create(el, {
  type: 'lines,words', mask: 'lines', linesClass: 'linha-mascara', autoSplit: true,
  onSplit(self) {
    gsap.set(el, { visibility: 'visible' })
    return gsap.from(self.words, {
      yPercent: 118, rotate: 3, duration: 1.15, delay: atraso, ease: 'expo.out', stagger: 0.04,
      paused: !aoScroll,
      scrollTrigger: aoScroll ? { trigger: el, start: 'top 88%', once: true } : undefined,
    })
  },
})
```

| Parâmetro | Valor |
|---|---|
| Deslocamento inicial | `yPercent: 118` (a palavra começa totalmente abaixo da linha) |
| Rotação inicial | 3° (sentido horário), volta a 0° |
| Duração por palavra | 1,15 s |
| Curva | `expo.out` |
| Cascata | 0,04 s por palavra (um título de 8 palavras termina em 1,15 + 0,28 = 1,43 s, CALCULADO) |
| Gatilho nas seções | topo do título a 88 % da altura da janela, uma vez só (`once: true`) |
| Hero | sem gatilho de rolagem: toca na abertura com `atraso: 0,15 s` |
| `autoSplit: true` | redivide e refaz a animação quando a largura muda (troca de linhas) ou a fonte carrega |

CSS de apoio (EXATO):

```css
html.com-movimento [data-titulo] { visibility: hidden }      /* evita o "piscar" antes da divisão */
html.com-movimento .linha-mascara { overflow: clip; padding-bottom: 0.08em; margin-bottom: -0.08em }
```

O `padding-bottom` de 0,08 em com margem negativa igual evita cortar as descendentes (g, p, ç) dentro da máscara sem mudar o espaçamento. **EXATO.**

## 3. Movimento reduzido e falhas

- Movimento reduzido: `iniciarTexto` nem é chamado. Os títulos aparecem normais. **EXATO.**
- Rede de segurança: sem `com-movimento` (depois de 8 s de falha), nada fica escondido.

## 4. Como adaptar

- Para títulos curtos e pesados, mantenha 118 %. Para fontes com descendentes longas, aumente o `padding-bottom` da máscara para 0,12 em.
- Sem SplitText: divida manualmente em `<span class="linha"><span class="palavra">`, com `overflow: clip` na linha.
- Licença: o SplitText faz parte do GSAP 3.13+ e é gratuito ("GSAP no-charge license"). Confira os termos atuais da GSAP antes de usar em outro projeto.
