# CUR-02 · Rótulo contextual do cursor (o círculo laranja "ABRIR")

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (rótulos "Abrir" e "Som" observados no navegador) |
| Portabilidade | Direta. Funciona em qualquer elemento com o atributo `data-cursor="Texto"` |
| Arquivos de origem | `src/motor/interacao.js` (estado `is-rotulo`) · `src/estilo/base.css` (`.cursor.is-rotulo`, `.cursor__rotulo`) · `src/motor/som.js` (`atualizar()` troca "Som"/"Mudo") · `index.html` (atributos `data-cursor`) |
| Dependências | CUR-01 (cursor próprio). Sem o cursor próprio (toque ou movimento reduzido) o rótulo não existe |

## 1. O que é

Quando o ponteiro está sobre um elemento com `data-cursor`, o anel do cursor vira um **disco laranja cheio de 76 px** com o texto do atributo no centro, em caixa alta e fonte mono. É o "indicador circular laranja com a palavra ABRIR".

## 2. Onde está no site (inventário completo)

| Elemento | Local | `data-cursor` | O que o clique faz |
|---|---|---|---|
| `a.acesso` "Área comum · Vídeos" | Seção 08 Área do aluno | `Abrir` | Abre o portal na aba de vídeos (`#area-comum-videos`), com cortina circular a partir do ponto do clique |
| `a.acesso` "Área comum · Material" | Seção 08 | `Abrir` | Abre o portal na biblioteca de materiais (`#area-comum`) |
| `a.acesso.acesso--curso` "Área do curso · Faça seu login" | Seção 08 | `Entrar` | Abre `https://dashboard.kiwify.com.br/login` em nova aba |
| `a.estante__item` (×3: Apostila teórica, Procedimento de recertificação, Procedimentos de provas práticas) | Seção 08, estante | `Ler` | Abre o portal direto no leitor de PDF (`#ler-<id>`) |
| `button.som` | Barra de navegação | `Som` (desligado) / `Mudo` (ligado) | Liga ou desliga o som sintetizado (SOM-01) |

São 7 elementos no total: 2 "Abrir", 1 "Entrar", 3 "Ler", 1 "Som/Mudo". **EXATO.**

## 3. Geometria, cor e tipografia do estado

| Propriedade | Valor | Confiab. |
|---|---|---|
| Diâmetro do disco | 76 px (margem −38 px, centrado no ponteiro) | EXATO, OBSERVADO |
| Preenchimento | `var(--brasa)` = `#fb781e` | EXATO, OBSERVADO (`rgb(251,120,30)`) |
| Contorno | nenhum (`box-shadow: none`) | EXATO |
| Texto | `500 10px/1 'IBM Plex Mono'`, `letter-spacing: .1em` (= 1 px), `text-transform: uppercase` | EXATO |
| Cor do texto | `var(--brasa-texto)` = `#1a0a02` | EXATO |
| Centralização | `display:grid; place-items:center` no anel | EXATO |
| Ponto central | continua visível, com `difference` sobre o laranja: aparece **azul** `#0d79d6` no meio do disco | CALCULADO, OBSERVADO |
| Largura do texto "ABRIR" | ≈ 31 px (5 caracteres de 10 px mono, mais 4 espaços de 1 px) | ESTIMATIVA |

## 4. Linha do tempo completa (entrar, clicar, sair, voltar)

Valores de tempo e curva são EXATOS (CSS), salvo indicação.

**Entrada (hover):**
1. No primeiro `pointermove` dentro do elemento, `.cursor` ganha `is-rotulo` e o texto do rótulo é trocado.
2. O anel cresce de 38 px (ou de 58 px, se vinha de um link) para **76 px** em **0,35 s**, `cubic-bezier(0.16, 1, 0.3, 1)`. Cresce a partir do centro porque a margem anima junto.
3. O fundo passa de transparente a laranja em **0,3 s** (`ease`). O contorno some em 0,3 s.
4. O texto aparece por opacidade 0→1 em **0,2 s**.
5. O anel continua seguindo o ponteiro com 0,38 s de inércia (CUR-01).
6. Ao mesmo tempo, o próprio cartão reage (efeitos do cartão, não do cursor):
   - `.acesso` com `data-luz`: um brilho radial de 300 px, `rgba(251,120,30,.16)`, segue o mouse (`--mx`, `--my`) e aparece com `opacity` 0→1 em 0,35 s (ficha CRT-01).
   - A seta `.acesso__seta` se desloca `translate: 4px -4px` em 0,4 s com `var(--mola)` = `cubic-bezier(0.34, 1.4, 0.64, 1)` (tem *overshoot*).
   - `.estante__item`: fundo vai para `var(--aco-2)` e o contorno para `inset 0 0 0 1px rgba(251,120,30,.45)`, em 0,3 s.

**Clique:**
1. `pointerdown` coloca `is-apertado` no cursor. O CSS pediria `scale .8`, mas **não há efeito visível** (CUR-01 §10). **OBSERVADO.**
2. Não há onda (*ripple*): a onda só existe em `.botao` (BOT-03). Os cartões `.acesso` e `.estante__item` não são `.botao`. **EXATO.**
3. "Abrir" e "Ler": o clique é capturado (fase de captura) por `portal.js`, que guarda o ponto do clique como origem da cortina e abre o portal. A cortina vai de `clip-path: circle(0px at x y)` até `circle(R at x y)`, com R = distância até o canto mais longe da janela, em **0,9 s** `expo.inOut`. Junto, o som "virada" (se ligado) e a entrada em cascata do conteúdo do portal (y 26→0, opacidade 0→1, 0,9 s `expo.out`, atraso 0,35 s, *stagger* 0,05 s). Ficha CEN-10.
4. Com o portal aberto, o cursor próprio é escondido e o cursor do sistema volta (`html.portal-aberto .cursor { display:none }`).
5. "Entrar": abre a Kiwify em nova aba. A página fica onde estava.

**Saída:**
1. No primeiro `pointermove` fora do elemento, `is-rotulo` sai. O anel volta a 38 px (ou vai para 58 px se o novo alvo for link) em 0,35 s. O fundo volta a transparente em 0,3 s e o texto some em 0,2 s.
2. O texto do rótulo **permanece** no DOM com opacidade 0 até o próximo elemento com rótulo. **OBSERVADO.**
3. O brilho do cartão apaga (`--brilho: 0`, 0,35 s) e a seta volta (0,4 s, mola).

**Retorno:** ao entrar de novo, a sequência de entrada se repete por inteiro. Não há memória de estado nem atraso adicional.

**Retorno do portal:** ao fechar o portal (botão "Voltar ao site", Esc ou voltar do navegador), a cortina circular se fecha de volta no mesmo ponto de origem (0,6 s `expo.inOut`) e o cursor próprio reaparece no próximo movimento do mouse.

## 5. Gatilhos e regras

- Prioridade máxima: `[data-cursor]` vence `a/button/summary/label/select` e vence o estado de calor do hero.
- Basta o atributo estar num ancestral do alvo (`closest('[data-cursor]')`). Assim, `span` internos herdam o rótulo.
- O texto vem de `dataset.cursor`. Mudar o atributo em tempo real (como faz o botão de som) muda o rótulo no próximo `pointermove`.

## 6. Responsividade e acessibilidade

- Inexistente em toque, celular, tablet e movimento reduzido (o cursor próprio não é criado).
- O rótulo é só decorativo (`aria-hidden` no cursor). Os destinos têm texto próprio: "Vídeos", "Material", "Faça seu login", título do material.
- Tamanho fixo de 76 px em qualquer resolução. **EXATO.**

## 7. Como reproduzir

1. Ter o CUR-01 implementado (as regras `.cursor.is-rotulo ...` já estão nele).
2. Marcar os alvos: `<a href="..." data-cursor="Abrir">…</a>`.
3. Para rótulo dinâmico: `botao.dataset.cursor = ligado ? 'Mudo' : 'Som'`.

## 8. Como adaptar a outra identidade

- Cor do disco: troque `--brasa`. Cor do texto: `--brasa-texto`. Garanta contraste mínimo de 4,5:1 entre os dois (na CDC, `#1a0a02` sobre `#fb781e` = 7,17:1, CALCULADO pela fórmula WCAG).
- Textos curtos (até ~7 caracteres) cabem em 76 px com 10 px de fonte mono. Para palavras maiores, aumente o disco (ex.: 88 px) e mantenha a transição de 0,35 s.
- Em projetos sem cursor próprio, o equivalente acessível é um selo visível dentro do cartão.
