# ROL-03 · Barra de navegação: vidro flutuante, some ao descer, volta ao subir, seção atual acesa

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (sumiço a −84 px, retorno a 12 px e link "is-aqui" medidos) |
| Portabilidade | Direta |
| Arquivos de origem | `index.html` (`<header class="nav">`, linhas 47–64) · `src/estilo/topo.css` (bloco "nav") · `src/motor/rolagem.js` (`ligarRolagem`) · `src/motor/texto.js` (embaralhar letras, TIP-05) |
| Dependências | GSAP 3.15.0 + ScrollTrigger |

## 1. Anatomia

`header.nav` = logo (`a.nav__marca` com `i.logo`, 70 px de largura) · 6 links de seção (`nav.nav__links`: A CDC, Treinamentos, Provas, Estrutura, Depoimentos, Contato) · ações (`button.som`, `a.botao--vidro` "Área do aluno", `a.botao--brasa` "Inscreva-se" magnético, `button.menu-botao` só em telas menores).

| Propriedade | Valor | Confiab. |
|---|---|---|
| Posição | `fixed`, `top: calc(12px + safe-area-top)`, `left: 50%`, `translate: -50% 0`, `z-index: 50` | EXATO |
| Largura | `min(calc(100% − 2 × var(--gutter)), 1320px)` → 1 312 px em 1440 px; 1 080 px em 1200 px | EXATO, OBSERVADO |
| Altura | 60 px (56 px em ≤ 560 px) | EXATO |
| Padding | `0 8px 0 18px` (`padding-left: 14px` em ≤ 560 px) | EXATO |
| Raio | 16 px | EXATO |
| Fundo | `rgba(10,13,17,.55)` + `backdrop-filter: blur(18px) saturate(1.25)` + contorno `inset 0 0 0 1px var(--fio)` | EXATO |
| Estado sólido (`scrollY > 40`) | `rgba(10,13,17,.82)` + sombra `0 18px 40px -24px #000`. Transição de fundo e sombra: 0,4 s | EXATO |
| Links | `500 14px/1 Instrument Sans`, `var(--texto-2)`, espaço `clamp(14px, 1.8vw, 28px)`, `padding: 6px 0` | EXATO |
| Sublinhado | `::after` de 2 px, raio 2 px, `background: var(--revenido)` (palha → bronze → roxo → azul), `bottom: −2px`. Recolhido com `scale: 0 1` e origem à direita. No *hover* e no `.is-aqui`: `scale: 1 1` com origem à esquerda. Transição de 0,5 s `var(--entrada)` | EXATO |

O sublinhado **entra pela esquerda e sai pela direita**, porque a origem da transformação troca de lado entre os estados. **EXATO** (técnica de `transform-origin` alternado).

## 2. Some ao descer, volta ao subir (EXATO)

```js
const esconder = self.direction === 1 && y > innerHeight * 1.1
if (esconder !== escondida && !html.classList.contains('menu-aberto')) {
  escondida = esconder
  gsap.to(nav, { yPercent: esconder ? -160 : 0,
                 duration: esconder ? 0.45 : 0.7,
                 ease: esconder ? 'power2.in' : 'expo.out', overwrite: true })
}
```

| Estado | Deslocamento | Duração | Curva | Medido |
|---|---|---|---|---|
| Escondida (descendo, além de 110 % da altura da janela) | −160 % da própria altura (−96 px) | 0,45 s | `power2.in` (acelera para sair) | topo em −84 px (OBSERVADO) |
| Visível (qualquer subida) | 0 | 0,7 s | `expo.out` (chega rápido e assenta) | topo em 12 px (OBSERVADO) |

Com o menu do celular aberto a barra não se mexe.

## 3. Seção atual acesa

Para cada link, um ScrollTrigger na seção de destino com `start: 'top 55%'` e `end: 'bottom 55%'`. Quando ativo, o link recebe `.is-aqui` (texto `var(--texto)` e sublinhado cheio) e os outros perdem. A seção "Nossa equipe" e a "Área do aluno" não têm link na barra, então nenhum link fica aceso nelas. **EXATO, OBSERVADO.**

## 4. Outras microinterações da barra

- Logo: no *hover*, `filter: drop-shadow(0 0 8px rgba(251,120,30,.8))` em 0,3 s.
- Links: embaralham as letras (A–Z) por 0,55 s no `mouseenter` (TIP-05) e tocam "passe" se o som estiver ligado.
- "Inscreva-se": magnético (BOT-02), varredura de luz (BOT-01).
- Botão de som (BOT-05) e botão de menu (CEN-07).

## 5. Responsividade (EXATO)

| Largura | Mudança |
|---|---|
| ≤ 1080 px | some `.nav__links`, aparece `.menu-botao` (44 × 44 px) |
| ≤ 560 px | altura 56 px, some "Área do aluno", logo com 60 px, "Inscreva-se" com `padding 0 14px` |
| ≤ 380 px | some o botão de som |

## 6. Efeito colateral técnico (registrado)

O GSAP incorpora o `translate: -50% 0` do CSS ao `transform` inline e grava `translate: none` (estilo lido: `transform: translate(-50%, 0%)`). A centralização continua correta porque o valor é percentual. **OBSERVADO.**

## 7. Como adaptar

- Troque `--revenido` (o gradiente do sublinhado) por um gradiente da nova marca, ou por uma cor só.
- O limiar de 110 % da janela evita que a barra suma logo no início. Para páginas curtas, 60–80 %.
