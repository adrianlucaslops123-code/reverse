# BOT-06 · Botão "Copiar" e aviso flutuante (*toast*)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (código lido. A área de transferência não foi acionada no teste) |
| Portabilidade | Direta |
| Onde aparece | Seção Contato: ao lado dos 2 telefones e dos 2 e-mails (`data-copiar`) |
| Arquivos de origem | `src/motor/interacao.js` (`aviso`, bloco "copiar") · `src/estilo/fim.css` (`.copiar`) · `src/estilo/base.css` (`.aviso`) · `index.html` (`div.aviso`, linha 841) |

## 1. Botão `.copiar` (EXATO)

- `min-height: 32px; padding: 0 10px; border-radius: 8px`, fundo `rgba(255,255,255,.05)`, contorno `fio-forte`.
- `500 11px/1 IBM Plex Mono`, `letter-spacing .08em`, caixa alta, `var(--texto-2)`. Transição `background .2s, color .2s`.
- Hover: fundo brasa, texto `brasa-texto`.
- Feito (`.is-feito`): fundo `rgba(168,216,255,.16)`, texto `var(--arco)`, rótulo "Copiado" por **1,8 s**. Depois volta a "Copiar".

## 2. Lógica

1. `navigator.clipboard.writeText(data-copiar)`.
2. Se der certo: "Copiado" e aviso `Copiado: <valor>`.
3. Se falhar (sem permissão ou contexto inseguro): seleciona o texto do elemento anterior (o link) e mostra o aviso "Selecionei para você. Use Ctrl+C ou Copiar."

## 3. Aviso `.aviso` (EXATO)

- `fixed`, `left: 50%`, `bottom: 24px` (+ *safe-area*), `z-index: 96`, `max-width: calc(100% − 32px)`, `padding: 12px 18px`, raio 12 px.
- Vidro: `var(--vidro-forte)` + `backdrop-filter`, contorno `fio-forte`, sombra `0 20px 50px -20px #000`, 14 px.
- Escondido: `translate: −50% 140%; opacity: 0`. Visível: `translate: −50% 0; opacity: 1`. Transição `translate .6s var(--mola), opacity .3s`.
- Fica **2,6 s** visível. Chamadas seguidas reiniciam o tempo.
- `role="status" aria-live="polite"`: o leitor de tela anuncia a mensagem.

## 4. Como adaptar

O aviso é genérico: `aviso('mensagem')` pode ser reaproveitado para qualquer confirmação curta.
