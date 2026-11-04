# CEN-10 · Portal da área do aluno: cortina circular a partir do clique, biblioteca, busca e progresso

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (a seção da página foi capturada. O portal não foi aberto no teste) |
| Portabilidade | Direta para qualquer "biblioteca" de PDFs. Os dados ficam em `MATERIAIS` (`materiais.js`) |
| Arquivos de origem | `src/aluno/portal.js` · `src/aluno/materiais.js` · `src/aluno/busca.js` · `src/estilo/aluno.css` · `index.html` (`#portal`, linhas 744–829) |
| Dependências | GSAP 3.15.0 · `public/materiais/indice.json` (texto das páginas, para a busca) · `localStorage` |

## 1. Rotas por *hash* (EXATO)

| Hash | Abre |
|---|---|
| `#area-comum` | biblioteca, aba Materiais |
| `#area-comum-videos` | biblioteca, aba Vídeos (CEN-12) |
| `#ler-<id>` e `#ler-<id>-p<N>` | leitor de PDF (CEN-11), opcionalmente na página N |

- Abrir o portal cria **uma** entrada no histórico. Trocas internas usam `history.replaceState`. Assim, o "voltar" do navegador fecha o portal.
- Abrir a página com um desses *hashes* já abre o portal.

## 2. Cortina circular (EXATO)

- Origem: o ponto do clique (capturado na fase de captura do evento) ou o centro do campo de busca da seção.
- Abrir: `clip-path: circle(0px at x y)` → `circle(R at x y)`, com `R = hypot(max(x, larguraJanela − x), max(y, alturaJanela − y))` (distância até o canto mais longe), **0,9 s** `expo.inOut`. Conteúdo (`.portal__topo`, cabeça da biblioteca, cartões e "continuar") entra de `y: 26` e opacidade 0, 0,9 s `expo.out`, cascata 0,05 s, atraso 0,35 s.
- Fechar: círculo volta a 0 no mesmo ponto, **0,6 s** `expo.inOut`. Depois `hidden`, rolagem liberada e foco devolvido ao elemento que abriu o portal.
- Movimento reduzido: abre e fecha sem cortina.
- Com o portal aberto: rolagem da página parada; grão de filme, cursor próprio, cordão e WhatsApp escondidos; o laço das partículas e das brasas pausa.
- Fechar: botão "← Voltar ao site", **Esc** (no leitor, Esc volta à biblioteca; com o painel aberto em < 900 px, Esc não faz nada) ou voltar do navegador.

## 3. Biblioteca (EXATO)

- Cabeça: rótulo "CDC Área comum", título "Materiais de estudo" (`760 clamp(34px, 5vw, 72px)/0.96`), introdução, abas Materiais/Vídeos com contagem (sublinhado brasa de 2 px que cresce em 0,45 s) e busca.
- **"Continue de onde parou"**: aparece se houver progresso salvo. Mostra o material lido por último, a página e uma barra de 4 px.
- Cartão de material: capa 3:4 (`clamp(110px, 16vw, 190px)` de largura, fundo branco, zoom de 1,05 no *hover* em 0,7 s), selo "PDF · N pág.", prova + código, título, resumo, metadados ("N páginas · tamanho · pesquisável/escaneado"), barra de progresso e ações: "Ler agora" ou "Continuar na pág. N", atalho (ex.: "Ir para o gabarito") e "Baixar PDF".

## 4. Busca em todos os materiais (EXATO)

- Ignora acentos e maiúsculas (normalização NFD). Mínimo de 2 letras. Espera **240 ms** depois da última tecla.
- Baixa `materiais/indice.json` (280 KB, texto de cada página) só na primeira busca.
- Resultados agrupados por material, até 80 achados, com trecho de 70 caracteres antes e 90 depois e o termo marcado (`mark` com fundo `rgba(251,120,30,.3)`).
- O material escaneado (Procedimento de recertificação, `pesquisavel: false`) fica fora, com uma nota.
- O campo de busca da seção da página abre o portal já com os resultados.

## 5. Progresso de leitura

`localStorage['cdc-aluno-v1'] = { <id>: { pagina, total, quando } }`. É gravado 350 ms depois de parar numa página. A seção da página mostra uma barra de 3 px na estante (`.estante__lido`). Os dados ficam só no navegador do aluno: não há conta nem servidor.

## 6. Serviço externo

Só "Área do curso" / "Faça seu login" sai do site: `https://dashboard.kiwify.com.br/login` (nova aba).
