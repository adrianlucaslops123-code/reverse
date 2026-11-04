# CEN-12 · Vídeos da área comum: capa que vira player do YouTube (sem cookies)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** |
| Portabilidade | Direta |
| Arquivos de origem | `src/aluno/videos.js` · `src/aluno/materiais.js` (`VIDEOS`) · `src/estilo/videos.css` |
| Serviços externos | `i.ytimg.com` (capas `sddefault.jpg`) · `www.youtube-nocookie.com/embed/<id>` (player) · links "Assistir no YouTube ↗" |

## 1. Vídeos cadastrados (EXATO)

| # | Título (original do YouTube) | Canal | ID | Início |
|---|---|---|---|---|
| 01 | prova teorica n1 solda fbts Video aula Capitulo 1 introdução N1 | Deiwson Ribeiro | `F6voYaovgi4` | n/a |
| 02 | Video prova teorica n1 solda fbts aula Capitulo 4 processos e cortes N1 | Deiwson Ribeiro | `31SkkrD4Lcs` | 9 s |
| 03 | Video deformações N1  prova teorica fbts ,inspetor N1 solda, snqc petrobras | Deiwson Ribeiro | `EgpWC61ftYs` | n/a |

> O HTML estático ainda diz "Vídeos **0**" na aba e traz o aviso "Ainda não há vídeos na área comum.". O script `montarVideos` esconde o aviso e acrescenta os 3 vídeos. A contagem da aba é atualizada pelo `portal.js` quando a biblioteca é montada (`VIDEOS.length` = 3). **EXATO.**

## 2. Comportamento (EXATO)

- Grade `repeat(auto-fill, minmax(min(100%, 320px), 1fr))`, `gap: 16px`.
- Cartão: tela 16:9 com capa (`filter: saturate(.9) brightness(.84)`) e gradiente inferior. Botão de *play* circular de 64 px em brasa. *Hover*: a capa aproxima (`scale 1.04`, 0,7 s) e clareia, o *play* cresce (`scale 1.08`, 0,45 s mola).
- Clique: troca a capa por um `iframe` `youtube-nocookie` com `autoplay=1&rel=0&playsinline=1` (e `&start=` quando há início). **Um vídeo por vez**: os outros voltam para a capa.
- O vídeo para (volta à capa) quando a aba de vídeos ou o portal são fechados (`MutationObserver` no atributo `hidden`).
- Erros são capturados e não afetam o resto da página.
