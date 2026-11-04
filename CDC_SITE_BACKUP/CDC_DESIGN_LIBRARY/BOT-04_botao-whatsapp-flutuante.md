# BOT-04 · Botão flutuante do WhatsApp (pílula que se expande, com anel pulsante)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado**, com o **efeito colateral** descrito em BOT-02 §4 |
| Portabilidade | Direta (troque o link e o rótulo) |
| Arquivos de origem | `index.html` (`a.zap`, linhas 738–741) · `src/estilo/topo.css` (bloco "botão flutuante do WhatsApp") · `src/motor/rolagem.js` (`zap.classList.toggle('is-visivel', y > innerHeight * 0.7)`) |
| Link | `https://wa.me/5521982570418?text=Olá, Rose! Vim pelo site da CDC.` (nova aba) |

## 1. Medidas e cores (EXATO)

| Propriedade | Computador | ≤ 760 px |
|---|---|---|
| Posição | `fixed`, `right: 20px`, `bottom: 20px` (+ *safe-area*) | `right: 14px`, `bottom: 14px` |
| Altura | 56 px | 52 px |
| Padding | `0 16px` | `0 14px` |
| Forma | pílula (`border-radius: 999px`) | igual |
| Cor | fundo `#fb781e`, texto `#1a0a02`, `600 15px` | igual |
| Sombra | `0 14px 34px -12px rgba(251,120,30,.8)` | igual |
| Ícone | SVG de 24 × 24 px (balão do WhatsApp em traço de 1,6 px) | igual |
| `z-index` | 44 | igual |

## 2. Estados e animações (EXATO)

| Estado | Comportamento |
|---|---|
| Escondido (topo da página) | `translate: 0 140%` (abaixo da borda da tela) |
| Visível (`scrollY > 70 % da altura da janela`) | `translate: 0 0`. Transição de **0,7 s** com `var(--mola)` = `cubic-bezier(0.34, 1.4, 0.64, 1)`: sobe e passa um pouco do lugar |
| Repouso | só o ícone. O texto "Agendar com a Rose" tem `max-width: 0; overflow: hidden` |
| Hover (sem toque) | `gap` 0 → 10 px (0,4 s `--entrada`) e o texto abre `max-width` 0 → 200 px (0,5 s `--entrada`). Largura medida aberta: **210 px** (OBSERVADO) |
| Anel pulsante (`::before`) | `animation: anel 2.6s var(--entrada) infinite`. `box-shadow` de `0 0 0 0 rgba(251,120,30,.55)` a `0 0 0 18px rgba(251,120,30,0)` em 70 % do ciclo; parado de 70 % a 100 % |
| Magnetismo | sim (BOT-02) |
| Movimento reduzido | sem anel pulsante (`animation: none !important`) |
| Portal aberto | `display: none` |

Ao carregar a página, o anel pulsante do botão escondido (18 px de expansão) chega a aparecer como um arco laranja fraco no canto inferior direito, porque o brilho passa da borda da tela. **OBSERVADO** na captura do hero.

## 3. Como adaptar

- Troque o número, a mensagem pronta (`?text=`) e o rótulo.
- O limiar de 70 % da janela evita disputa com os botões do hero.
- Para outro canal (telefone, chat), mantenha a pílula que se expande. O padrão é independente do WhatsApp.
