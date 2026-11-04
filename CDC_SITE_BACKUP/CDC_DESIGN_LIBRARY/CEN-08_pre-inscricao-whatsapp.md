# CEN-08 · Pré-inscrição pelo WhatsApp (formulário sem servidor)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (formulário capturado. Envio não acionado no teste) |
| Portabilidade | Direta (troque o número) |
| Arquivos de origem | `src/cenas/contato.js` (`iniciarInscricao`) · `src/estilo/fim.css` (`.inscricao`) · `index.html` (linhas 675–694) |
| Serviços | `https://wa.me/5521982570418` (WhatsApp). Nenhum dado vai para servidor próprio |

## 1. Comportamento (EXATO)

- A cada digitação, o link do botão "Abrir no WhatsApp" é **remontado**: `https://wa.me/5521982570418?text=` + mensagem codificada:
  ```
  Olá, Rose! Meu nome é <nome ou "…">.
  Tenho interesse em: <treinamento escolhido>.
  <mensagem opcional>
  ```
- Clique sem nome: impede a abertura, reinicia a animação de erro (classe `is-erro`), mostra "Escreva o seu nome para a Rose saber com quem está falando." e foca o campo.
- Clique com nome: abre o WhatsApp numa nova aba e mostra "O WhatsApp abre numa nova aba com a sua mensagem. Se não abrir, escreva para (21) 98257-0418."
- Enter no formulário: dispara o clique do botão.

## 2. Estilo (EXATO)

- Caixa de vidro: padding `clamp(24px, 3vw, 40px)`, raio 18, `var(--vidro-forte)` + `backdrop-filter`, contorno `fio-forte`, sombra `0 40px 90px -50px #000`.
- Rótulos: `500 12px` mono, caixa alta, `.1em`, `--texto-2` ("(opcional)" sem caixa alta, `--texto-3`).
- Campos: altura mínima 50 px, `padding 12px 14px`, raio 12, fundo `rgba(255,255,255,.05)`, contorno `fio-forte`, `400 16px/1.4` (16 px evita o zoom automático do iOS). Seleção com seta desenhada por dois gradientes. Área de texto com altura mínima de 90 px.
- Foco: fundo `rgba(255,255,255,.07)` + contorno `--arco` + halo `0 0 0 4px rgba(168,216,255,.14)`.
- Erro: contorno brasa + halo `rgba(251,120,30,.16)` no campo nome e **tremor** do formulário: `treme .42s` (±7 px em 20 %, 40 %, 60 % e 80 % do tempo).
- Mensagem de retorno: 14 px, `--brasa-quente`, `aria-live="polite"`.

## 3. Opções do campo "Treinamento" (literais)

Curso Inspetor de Soldagem Nível 1 (semipresencial) · Qualificação: documentos técnicos + tratamento térmico · Qualificação: diárias de retreinamento · Recertificação Nível 1 (2 dias) · Recertificação Nível 1 (3 dias) · Hospedagem · Tenho uma dúvida
