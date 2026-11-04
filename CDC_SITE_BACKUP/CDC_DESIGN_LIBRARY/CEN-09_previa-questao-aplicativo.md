# CEN-09 · Prévia interativa de uma questão do aplicativo (janela de app)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, parcialmente validado** (janela e alternativas capturadas durante a entrada. A resposta não foi clicada no teste) |
| Portabilidade | Direta (troque enunciado, alternativas, gabarito e explicações) |
| Onde aparece | Seção 10 "Aplicativo" |
| Arquivos de origem | `src/cenas/aplicativo.js` · `src/estilo/aplicativo.css` · `index.html` (linhas 623–666) |
| Serviço externo | link "Conhecer o aplicativo ↗" para `https://cdc-capacita-o-em-qualidade.lovable.app/` (app separado, hospedado no Lovable). A prévia **não** conversa com o app: nada é enviado nem salvo |

## 1. Janela (EXATO)

- `.janela-app`: raio 18, fundo `linear-gradient(180deg, #10141a, #0b0e12 46%)`, contorno `fio-forte` + filete de luz `inset 0 1px 0 rgba(255,255,255,.05)` + sombras `0 60px 110px -60px #000` e `0 40px 90px -70px rgba(251,120,30,.55)`. Luz que segue o mouse (CRT-01).
- Barra: logo de 44 px, caminho "QUESTÕES › INSPEÇÃO DE SOLDAGEM" (mono 11 px, `.12em`) e estado "● MODO ESTUDO" (ponto pulsante de 7 px, brasa).
- Questão: módulo "MÓDULO: INSPEÇÃO DE SOLDAGEM" (mono 12 px, `--brasa-quente`, quadradinho de 8 px), progresso "Questão demonstrativa · Inspeção visual", trilho de 3 px preenchido a **22 %** (vai a 100 % ao responder, 0,9 s `--entrada`).
- Enunciado: `600 clamp(17px, 1.3vw, 20px)/1.45` Instrument Sans.
- Alternativa (`.opcao`): botão de altura mínima 54 px, grade `34px 1fr 22px`, `gap: 14px`, raio 12, fundo `rgba(255,255,255,.025)`, contorno `fio-forte`, `500 15px/1.35`. Letra num quadrado de 34 px com raio 9.

## 2. Estados da alternativa (EXATO)

| Estado | Visual |
|---|---|
| Hover (antes de responder) | fundo `rgba(251,120,30,.06)`, contorno `rgba(251,120,30,.5)`, `translate: 4px 0`. A letra fica laranja com texto escuro |
| Pressionado | `translate: 2px 0`, fundo `rgba(251,120,30,.1)` |
| Correta | fundo `rgba(63,191,134,.1)`, contorno `rgba(63,191,134,.7)`. Letra `#3fbf86` com texto `#04140c`. Sinal ✓ (`#5fdca4`) aparece de `scale .5` com a mola |
| Escolhida e errada | fundo `rgba(240,88,74,.1)`, contorno `rgba(240,88,74,.75)`. Letra `#f0584a` com texto `#1a0503`. Sinal ✕ (`#ff7b6e`) |
| Demais, depois de responder | opacidade 0,42, `cursor: default`, `aria-disabled="true"` |

## 3. Lógica (EXATO)

- Gabarito: **C) Trinca.**
- Ao responder (uma vez só): marca a escolhida e a correta, mostra o retorno e o botão "Tentar novamente", toca "clique".
- Retorno certo: "Resposta correta." + explicação. Errado: "Resposta incorreta. A alternativa correta é a C) Trinca." + motivo da alternativa escolhida + explicação. Textos literais em `aplicativo.js` (`EXPLICACAO`, `MOTIVOS`) e na especificação mestre, §8.
- Animações: caixa de retorno abre (altura 0 → auto, `paddingTop` 14, `paddingBottom` 16, `marginTop` 18, 0,7 s `expo.out`). Acerto: a alternativa "pulsa" (`scale 0.985 → 1`, 0,6 s `elastic.out(1, 0.45)`). Erro: "balança" (`x −7 → 0`, 0,6 s `elastic.out(1.1, 0.3)`). Botão "Tentar novamente" entra de `x: 8`.
- "Tentar novamente": limpa tudo e devolve o foco à alternativa A.
- No fim, `ScrollTrigger.refresh()`, porque a página cresceu.
- Erros dentro da prévia são capturados (`try/catch`) e não afetam o resto da página.

## 4. Entrada (EXATO)

- Janela: de opacidade 0, `y: 72`, `rotateX: 11°`, `scale: 0.965`, perspectiva 1 400, origem embaixo, para o lugar em 1,4 s `expo.out`. Gatilho: topo a 86 % da tela, uma vez.
- Peças internas: de `y: 16` e opacidade 0, 0,9 s `expo.out`, cascata de 0,06 s, atraso de 0,3 s.

## 5. Responsividade (EXATO)

≤ 960 px: uma coluna (apresentação → janela → ação). ≤ 480 px: o texto "Modo estudo" some, a grade das alternativas vira `30px 1fr 20px` e a letra fica com 30 px.
