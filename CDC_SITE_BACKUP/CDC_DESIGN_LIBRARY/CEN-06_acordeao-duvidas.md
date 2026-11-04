# CEN-06 · Perguntas frequentes: acordeão com altura animada (`details`/`summary`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (lista capturada fechada. Abertura não acionada no teste) |
| Portabilidade | Direta. Usa HTML nativo (`details`), que funciona sem JS |
| Arquivos de origem | `src/cenas/contato.js` (`iniciarDuvidas`) · `src/estilo/secoes.css` (bloco "dúvidas") · `index.html` (linhas 587–620) |

## 1. Estilo (EXATO)

- Grade da seção: `0.8fr / 1.2fr` (título à esquerda, perguntas à direita), `gap: clamp(32px, 6vw, 96px)`. Uma coluna em ≤ 900 px.
- Cada `details.pergunta` com divisórias de 1 px (`var(--fio)`).
- `summary`: `640 clamp(18px, 1.5vw, 22px)/1.3` Archivo 104 %, `padding: 24px 52px 24px 0`, sem marcador nativo.
- Ícone "+": duas barras de 16 × 1,5 px em brasa, à direita (`right: 8px`). Aberto: a barra vertical gira de 90° para 0°, formando "−", em 0,45 s `var(--mola)`.
- Resposta: `var(--texto-2)`, `padding: 0 52px 26px 0`, `max-width: 62ch`. Links em brasa.

## 2. Animação (EXATO)

- Abrir: `d.open = true` e altura de 0 para `auto` com opacidade 0 → 1, 0,6 s `expo.out`. No fim, `ScrollTrigger.refresh()` (a página cresceu).
- Fechar: altura → 0 e opacidade → 0, 0,45 s `power3.inOut`. No fim, `d.open = false`.
- Movimento reduzido: o clique segue o comportamento nativo do `details` (abre e fecha sem animação).

## 3. Conteúdo

6 perguntas (texto literal na especificação mestre, §8): agendamento · local · hospedagem · curso N1 · cobrança da qualificação · acesso ao material.
