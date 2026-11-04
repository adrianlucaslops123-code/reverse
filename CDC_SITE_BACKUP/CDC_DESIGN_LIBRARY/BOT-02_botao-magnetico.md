# BOT-02 · Botões magnéticos (`data-magnetico`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (deslocamento medido), com **efeito colateral observado** no botão flutuante (§4) |
| Portabilidade | Direta |
| Onde aparece | 9 elementos: os 2 botões do hero, "Inscreva-se" (barra), "Comprar o curso" e os 2 "Agendar com a Rose" (planos), "Conhecer o aplicativo", "Abrir no WhatsApp" (pré-inscrição) e o botão flutuante do WhatsApp (`.zap`) |
| Arquivos de origem | `src/motor/interacao.js` (bloco "botões magnéticos", linhas 62–77) |
| Dependências | GSAP 3.15.0 (`quickTo`) |

## 1. Comportamento (EXATO)

```js
const mx = gsap.quickTo(el, 'x', { duration: 0.5, ease: 'power3.out' })
const my = gsap.quickTo(el, 'y', { duration: 0.5, ease: 'power3.out' })
el.addEventListener('pointermove', (e) => {
  const r = el.getBoundingClientRect()
  mx((e.clientX - (r.left + r.width / 2)) * 0.28)
  my((e.clientY - (r.top + r.height / 2)) * 0.36)
})
el.addEventListener('pointerenter', () => som?.tocar('passe'))
el.addEventListener('pointerleave', () => gsap.to(el, { x: 0, y: 0, duration: 0.9, ease: 'elastic.out(1, 0.4)', overwrite: true }))
```

| Parâmetro | Valor |
|---|---|
| Fator horizontal | 0,28 da distância do ponteiro ao centro |
| Fator vertical | 0,36 (o botão "acompanha" mais na vertical) |
| Deslocamento máximo (botão grande do hero, 250 × 54 px) | ±35 px em x, ±9,7 px em y, com o ponteiro na borda |
| Seguimento | 0,5 s `power3.out` |
| Soltura | 0,9 s `elastic.out(1, 0.4)`: volta passando um pouco do centro e oscila |
| Som | "passe" ao entrar (se ligado, com limite de 1 a cada 60 ms) |
| Condição | `(hover: hover) and (pointer: fine)` e sem movimento reduzido |

Medido: com o ponteiro perto do centro do botão "Ver treinamentos e valores", o botão ficou em `translate(−1,92 px; 1,07 px)`. **OBSERVADO.** O deslocamento máximo do botão grande é **CALCULADO** (125 × 0,28; 27 × 0,36).

## 2. Interação com o cursor

O cursor vai para `is-link` (anel de 58 px laranja). Como o botão se aproxima do ponteiro, o anel (atraso de 0,38 s) e o botão (0,5 s) chegam juntos ao mesmo ponto. É o efeito "imã".

## 3. Interação com outros efeitos

- Varredura de luz (BOT-01) e onda no clique (BOT-03) acontecem dentro do botão deslocado.
- O deslocamento usa `transform` (x/y). O tamanho do botão não muda.

## 4. Efeito colateral observado (não corrigir no site, só registrar)

No `.zap`, o CSS usa `translate: 0 140%` (escondido) e `translate: 0 0` (`.is-visivel`). Na primeira vez que o mouse passa sobre o `.zap`, o GSAP grava inline `translate: none`. A partir daí o botão **não se esconde mais** ao voltar para o topo da página (medido: topo do botão em 824 px com `scrollY = 0`, sem `.is-visivel`). **OBSERVADO.**

> Reconstrução fiel ao comportamento: o `.zap` passa a ficar sempre visível depois do primeiro *hover*. Reconstrução fiel à intenção: esconder e mostrar o `.zap` com `y`/`yPercent` do GSAP, ou envolver o botão num contêiner que recebe o `translate`. Registre a escolha.

## 5. Como adaptar

- Fatores entre 0,2 e 0,4 parecem naturais. Acima de 0,5 o botão "foge" do ponteiro.
- Não aplique a botões pequenos (< 40 px) nem a links de texto: o deslocamento atrapalha a mira.
- Regra geral para reutilizar: **não misture** a propriedade CSS `translate` com `x/y` do GSAP no mesmo elemento.
