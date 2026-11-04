# FUN-01 · Grão de filme sobre a página inteira

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (textura presente em todas as capturas. Desligado no movimento reduzido: animação `none`, OBSERVADO) |
| Portabilidade | Direta (CSS puro, sem arquivo de imagem) |
| Arquivos de origem | `index.html` (`<div class="grao" aria-hidden="true">`) · `src/estilo/base.css` (bloco "grão de filme") |

## 1. Receita (EXATO)

```css
.grao {
  position: fixed; inset: -50%; z-index: 90; pointer-events: none; opacity: 0.07;
  background-image: url("data:image/svg+xml,…<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.2 0'/></filter><rect width='100%' height='100%' filter='url(#n)'/>…");
  animation: grao 0.9s steps(6) infinite;
}
@keyframes grao {
  0% { transform: translate(0, 0) } 20% { transform: translate(-4%, 3%) } 40% { transform: translate(3%, -5%) }
  60% { transform: translate(-6%, -2%) } 80% { transform: translate(5%, 4%) } 100% { transform: translate(0, 0) }
}
```

| Parâmetro | Valor |
|---|---|
| Ladrilho | SVG de 180 × 180 px gerado por `feTurbulence` (`fractalNoise`, frequência 0,9, 2 oitavas) |
| Cor | branco (a matriz zera RGB → 1 e usa o alfa do ruído × 1,2) |
| Opacidade da camada | 7 % |
| Área | `inset: −50%` (200 % da tela, para o deslocamento nunca mostrar borda) |
| Movimento | salta entre 6 posições a cada ciclo de 0,9 s (`steps(6)`), cerca de 6,7 trocas por segundo |
| Camada | `z-index: 90`, acima do conteúdo, abaixo do cursor (95) |
| Desligado | movimento reduzido (`animation: none`) e portal aberto (`display: none`) |

## 2. Como adaptar

Opacidade entre 4 % e 8 % em fundos escuros. Em fundos claros, troque a matriz para preto (`0 0 0 0 0 …`) e use 3–5 %.
