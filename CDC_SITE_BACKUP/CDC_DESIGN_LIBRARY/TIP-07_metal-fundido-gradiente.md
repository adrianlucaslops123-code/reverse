# TIP-07 · Metal fundido: gradiente que corre dentro do texto e do logo

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (visível em "competências." e no logo do rodapé) |
| Portabilidade | Direta (CSS puro) |
| Onde aparece | `.contato__linha--brasa` ("competências.") · `.logo--fundido` (logo grande do rodapé) |
| Arquivos de origem | `src/estilo/base.css` (`.logo--fundido`, `@keyframes fundir`) · `src/estilo/fim.css` (`.contato__linha--brasa`) |
| Dependências | nenhuma |

## 1. Receita (EXATO)

```css
background: linear-gradient(100deg,
  var(--brasa-escura) 0%, var(--brasa) 30%, var(--brasa-quente) 46%,
  #fff3d6 50%, var(--brasa-quente) 54%, var(--brasa) 70%, var(--ouro) 100%);
background-size: 220% 100%;
animation: fundir 7s linear infinite;
@keyframes fundir { from { background-position: 110% 0 } to { background-position: -110% 0 } }
```

- No texto: `-webkit-background-clip: text; background-clip: text; color: transparent`.
- No logo: o elemento `.logo` é um bloco com `mask: url('/marca/cdc-mascara.png') center / contain no-repeat` e `aspect-ratio: 1400 / 717`. O gradiente aparece só onde a máscara tem tinta.

| Parâmetro | Valor |
|---|---|
| Ângulo | 100° |
| Paradas | `#c2410c` 0 · `#fb781e` 30 % · `#ffb24a` 46 % · `#fff3d6` 50 % (o "brilho" branco-creme) · `#ffb24a` 54 % · `#fb781e` 70 % · `#c99f53` 100 % (ouro) |
| Tamanho | 220 % da largura (o brilho percorre o texto sem sumir nas pontas) |
| Ciclo | 7 s, linear, infinito. Da direita para a esquerda (`110%` → `−110%`) |
| Movimento reduzido | `animation: none` (fica parado) |

## 2. Logo pintável (base)

`.logo` padrão: mesmo recurso de máscara, preenchido com `var(--brasa)`. Usos: navegação (70 px de largura, 60 px em ≤ 560 px), barra da janela do app (44 px), portal (56 px), rodapé (`min(64vw, 620px)`, versão fundida). **EXATO.**

## 3. Como adaptar

- Troque as 7 paradas pela paleta da marca, mantendo um ponto claro no meio (50 %) para dar o efeito de reflexo.
- A técnica de **logo como máscara** permite recolorir o logotipo só com CSS, em qualquer cor ou gradiente.
