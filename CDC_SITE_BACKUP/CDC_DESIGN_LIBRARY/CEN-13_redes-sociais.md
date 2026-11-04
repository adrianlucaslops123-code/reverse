# CEN-13 · Redes sociais: ícones no canto, linha no rodapé e pop-up (`dialog`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (ícones do canto visíveis nas capturas). Pop-up: não aberto no teste |
| Portabilidade | Direta. **Um único lugar** com os links: `REDES` em `src/redes.js` |
| Arquivos de origem | `src/redes.js` · `src/estilo/redes.css` · `index.html` (`nav.redes-canto`, `dialog.redes-popup`, `p.redes-linha`, botão "Redes sociais ↗" no contato) |

## 1. Perfis (EXATO)

| Rede | Perfil | URL |
|---|---|---|
| Instagram | @deiwsonrosecdcoficial | https://www.instagram.com/deiwsonrosecdcoficial |
| Facebook | cdctreinamentos.com.br | https://www.facebook.com/cdctreinamentos.com.br |

Ícones SVG inline de 24 × 24 (desenhados em 18 px). Links em nova aba, com `aria-label` "<Rede> da CDC (abre em nova aba)".

## 2. Peças (EXATO)

| Peça | Comportamento |
|---|---|
| Canto inferior esquerdo (`.redes-canto`) | `fixed`, `left: 20px`, `bottom: 28px` (14 px / 22 px em ≤ 760 px). Círculos de vidro de 40 px (36 px no celular). Aparecem com `html.is-rolou` (opacidade + `translate 12px → 0`, 0,6 s `--entrada`). *Hover*: ícone e contorno em brasa. Escondidos com o portal aberto |
| Rodapé (`.redes-linha`) | ícone + nome, 14 px, `--texto-2`. *Hover* em brasa |
| Pop-up (`dialog.redes-popup`) | aberto por "Redes sociais ↗" (seção Contato) com `showModal()`. 380 px de largura máxima, vidro forte, raio 18. Entra com `redes-entra .45s` (opacidade 0 e `translate 0 14px`). Fundo atrás: `rgba(7,9,12,.6)` + `blur(4px)`. Cada perfil é um cartão com ícone num quadrado de 40 px, nome, perfil e seta ↗. Fecha com ×, Esc ou clique fora. Com o pop-up aberto, o cursor próprio é escondido e a rolagem trava |
