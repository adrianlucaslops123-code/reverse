# TIP-04 · Números que contam com os dígitos embaralhando (`data-contar`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (valores finais 2005, 95, 99, 10 nas capturas) |
| Portabilidade | Direta |
| Onde aparece | Seção 01 "A CDC", grade `.numeros`: 2005 (começa de 1990), 95 %, 99 %, 10 min |
| Arquivos de origem | `src/motor/texto.js` (bloco "números que contam") · `index.html` (`data-contar`, `data-de`) · `src/estilo/secoes.css` (`.numeros`, `.numero`) |
| Dependências | GSAP 3.15.0 + ScrollTrigger |

## 1. Comportamento

Ao entrar na tela, o número vai do valor inicial (`data-de`, padrão 0) ao final (`data-contar`) em **2 s**, com `expo.out`: corre no começo e assenta devagar no fim. Nos primeiros **55 %** do tempo, os dígitos ainda "instáveis" são sorteados a cada quadro, como um mostrador mecânico acertando. Da direita para a esquerda, um dígito por vez vai se fixando.

## 2. Algoritmo (EXATO)

```js
gsap.to(obj, { v: fim, duration: 2, ease: 'expo.out',
  onUpdate() {
    const atual = Math.round(obj.v), progresso = this.progress()
    if (progresso < 0.55 && atual !== fim) {
      const s = String(atual)
      const fixos = Math.max(0, s.length - 1 - Math.floor((0.55 - progresso) * 4))
      el.textContent = s.slice(0, fixos) + s.slice(fixos).replace(/\d/g, () => String((Math.random() * 10) | 0))
    } else el.textContent = String(atual)
  },
  onComplete: () => (el.textContent = String(fim)),
})
```

| Parâmetro | Valor |
|---|---|
| Gatilho | `start: 'top 88%'`, uma vez |
| Duração | 2 s, `expo.out` |
| Fase embaralhada | progresso < 0,55 |
| Dígitos fixos | `comprimento − 1 − floor((0,55 − progresso) × 4)`, nunca menor que 0. Número de 4 dígitos (1990 → 2005): 1 dígito fixo até 5 % do tempo, 2 até 30 %, 3 até 55 %. Número de 2 dígitos (95, 99, 10): nenhum fixo até 30 %, 1 até 55 %. O último dígito sempre embaralha até 55 %. Depois todos ficam fixos (CALCULADO) |
| Largura estável | `font-variant-numeric: tabular-nums` no `dd` (os dígitos têm a mesma largura e o número não "dança") |

## 3. Tipografia dos números (EXATO)

- Valor (`dd`): `800 clamp(48px, 6vw, 96px)/0.9 Archivo`, `font-stretch: 112%`, `letter-spacing: −0.03em`, `white-space: nowrap`. Em 1440 px: 86,4 px. **CALCULADO.**
- Unidade (`small`: %, min): `0.42em`, peso 600, `var(--brasa)`, `margin-left: 4px`.
- Legenda (`dt`): `14px`, `line-height 1.4`, `var(--texto-2)`, `max-width: 24ch`. Fica **acima** do número no HTML, mas aparece **abaixo** por causa de `flex-direction: column-reverse`.
- Grade: 4 colunas com divisórias de 1 px (`var(--fio)`) e `border-top`. Em ≤ 900 px vira 2 × 2.

## 4. Movimento reduzido

Não roda: o número final já está no HTML. **EXATO.**

## 5. Como adaptar

- Use `data-de` para começar perto do valor final em anos (1990 → 2005), o que evita uma contagem longa e sem sentido a partir de 0.
- O embaralhamento combina com marcas técnicas e industriais. Para uma marca delicada, remova o ramo `progresso < 0.55`.
