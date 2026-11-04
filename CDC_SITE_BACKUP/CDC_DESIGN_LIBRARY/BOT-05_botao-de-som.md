# BOT-05 · Botão de som (quatro barras que dançam)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | Botão **implementado e validado** (visual e rótulo "Som" observados). O som em si: ver SOM-01 (não validado por audição) |
| Portabilidade | Direta |
| Arquivos de origem | `index.html` (`button.som`, linhas 58–60) · `src/estilo/topo.css` (bloco "botão de som") · `src/motor/som.js` (`atualizar`, `definir`) |

## 1. Medidas (EXATO)

- 44 × 44 px, raio 12 px, fundo transparente, contorno `inset 0 0 0 1px var(--fio)`.
- 4 barras (`<i>`) de 2 × 6 px, raio 2 px, `gap: 3px`, cor `var(--texto-2)`, transição `height .3s, background .3s`.
- Ligado (`aria-pressed="true"`): barras `var(--brasa)` com `animation: barra .9s ease-in-out infinite` (5 px → 16 px → 5 px). Atrasos das barras: 0, −0,3 s, −0,6 s, −0,15 s.
- Some em ≤ 380 px de largura.
- Movimento reduzido: barras paradas (`animation: none !important`).

## 2. Comportamento (EXATO)

- Clique: liga ou desliga. Ao ligar, cria o `AudioContext` (só depois de um gesto, como exigem os navegadores), começa o zumbido ambiente e toca "clique".
- Acessibilidade: `aria-pressed` (true/false) e `aria-label` "Ligar o som da página" / "Desligar o som da página".
- Rótulo do cursor: `data-cursor` "Som" (desligado) / "Mudo" (ligado). Ver CUR-02.
- Memória: guarda `localStorage['cdc-som'] = '1' | '0'`. Se ficou ligado na visita anterior, religa no **primeiro gesto** da pessoa (`pointerdown` ou `keydown`, em captura), menos quando o gesto é no próprio botão.
- O som sempre começa desligado. Nada toca sem gesto. **EXATO.**

## 3. Como adaptar

Troque as cores das barras. Mantenha o padrão "desligado por padrão + `aria-pressed`".
