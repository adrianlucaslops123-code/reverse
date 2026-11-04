# BOT-03 · Onda no clique (*ripple*) dos botões

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado visualmente** (código lido. A onda dura 0,7 s e não foi capturada em quadro) |
| Portabilidade | Direta |
| Onde aparece | Qualquer `.botao`, inclusive no toque |
| Arquivos de origem | `src/motor/interacao.js` (bloco "onda no clique", linhas 79–91) · `src/estilo/base.css` (`.onda`, `@keyframes onda`) |

## 1. Comportamento (EXATO)

No `pointerdown` em qualquer lugar do documento, se o alvo estiver dentro de um `.botao` e não houver movimento reduzido:

1. cria um `span.onda` na posição do ponteiro, relativa ao botão;
2. a onda é um círculo de **12 px**, branco a 45 % (`rgba(255,255,255,.45)`), centrado (`margin: −6px 0 0 −6px`), atrás do texto (`z-index: −1`) e dentro do botão (`overflow: hidden` + `isolation: isolate`);
3. anima `transform: scale(40)` e `opacity: 0` em **0,7 s** com `var(--entrada)` = `cubic-bezier(0.16, 1, 0.3, 1)`, `forwards`. O diâmetro final é **480 px** (CALCULADO);
4. o `span` é removido em **750 ms**;
5. toca o som "clique" (se ligado).

```css
.onda { position: absolute; z-index: -1; border-radius: 50%; pointer-events: none;
  width: 12px; height: 12px; margin: -6px 0 0 -6px; background: rgba(255, 255, 255, 0.45);
  animation: onda 0.7s var(--entrada) forwards }
@keyframes onda { to { transform: scale(40); opacity: 0 } }
```

## 2. Observações

- Funciona no toque, porque usa `pointerdown` e não depende de `hover`.
- Vários cliques rápidos criam várias ondas sobrepostas.
- Os cartões (`.acesso`, `.estante__item`) **não** têm onda, porque não são `.botao`.

## 3. Como adaptar

- Para fundos claros, use uma onda escura (`rgba(0,0,0,.12)`).
- 40× de 12 px cobre botões de até ~480 px. Para botões maiores, aumente o fator.
