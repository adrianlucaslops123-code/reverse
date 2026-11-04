# CEN-07 · Menu de tela cheia (celular e tablet): cortina que desce e links em cascata

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (iPhone 13) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (menu aberto capturado no iPhone 13) |
| Portabilidade | Direta |
| Onde aparece | Telas ≤ 1080 px (botão de duas barras na barra de navegação) |
| Arquivos de origem | `src/cenas/contato.js` (`iniciarMenu`) · `src/estilo/topo.css` (`.menu-botao`, `.menu`) · `index.html` (`#menu`, linhas 66–78) |

## 1. Estilo (EXATO)

- `.menu`: `fixed; inset: 0; z-index: 45` (abaixo da barra, que fica por cima), coluna centrada, `gap: 40px`, `padding-top: 96px` (+ *safe-area*), fundo `rgba(7,9,12,.985)` + `backdrop-filter: blur(24px)`.
- Links: `750 clamp(30px, 9vw, 52px)/1.05` Archivo 112 %, `letter-spacing −0.02em`, com o número da seção (01–07) em mono 12 px, brasa, `.1em`.
- Rodapé: "WhatsApp (21) 98257-0418" em mono 13 px, link em brasa.
- Itens: A CDC · Treinamentos · Provas · Estrutura · Depoimentos · Área do aluno · Contato.

## 2. Animação (EXATO)

| Ação | Valores |
|---|---|
| Abrir | `hidden = false`, `html.menu-aberto`, `aria-expanded=true`, rolagem travada. Cortina: `clip-path inset(0 0 100% 0)` → `inset(0 0 0 0)`, 0,7 s `expo.inOut` (desce de cima para baixo). Links: de `yPercent 60` e opacidade 0, 0,8 s `expo.out`, cascata 0,05 s, atraso 0,25 s. Foco no primeiro link |
| Fechar | cortina sobe (`inset(0 0 100% 0)`), 0,5 s `expo.inOut`. Depois `hidden = true` e rolagem liberada |
| Gatilhos para fechar | botão (agora um X), **Esc**, ou clique num link (a âncora rola até a seção) |
| Botão | as duas barras se deslocam ±3,75 px e giram ±45° em 0,4 s `var(--entrada)` |
| Barra de navegação | não se esconde com o menu aberto |

## 3. Como adaptar

A cortina por `clip-path` é leve (não move o layout). Para entrar de lado, use `inset(0 100% 0 0)`.
