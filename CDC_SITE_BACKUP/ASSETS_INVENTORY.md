# ASSETS_INVENTORY: inventário de recursos do site CDC

Todos os recursos de que o site `https://cdc-cursos-kappa.vercel.app/` precisa para funcionar e para ser reconstruído, com o caminho original, o formato, a finalidade e se estão guardados no repositório ou dependem de um serviço externo.

- **Repositório de origem:** `https://github.com/adrianlucaslops123-code/landing-page-cdc` (público), commit `65c37e7`. Caminhos abaixo relativos à raiz dele.
- **Pasta pública:** tudo o que está em `public/` é copiado como está para a raiz do site publicado (ex.: `public/fotos/x.webp` → `https://cdc-cursos-kappa.vercel.app/fotos/x.webp`).
- **Verificação:** dimensões lidas nos arquivos. Disponibilidade dos arquivos publicados e dos serviços externos testada em 3 nov. 2026 (HTTP 200 / 206). **OBSERVADO.**
- **Git LFS:** não é usado (não há `.gitattributes`). Todos os binários estão dentro do Git. O pacote do repositório tem 11,08 MiB.

> Este inventário **não duplica** os arquivos. Ele aponta onde estão. O **backup real** dos arquivos é o próprio repositório `landing-page-cdc` (ver `README.md`, §7).

---

## 1. Marca

| Recurso | Caminho | Formato | Dimensões / tamanho | Finalidade | Armazenamento |
|---|---|---|---|---|---|
| Máscara do logotipo CDC | `public/marca/cdc-mascara.png` | PNG com alfa (branco sobre transparente) | 1400 × 717 px · 65,9 KB | **Recurso mais crítico.** Fonte do logo de partículas (amostrado pixel a pixel), da abertura, do logo da barra, do portal, da janela do app e do logo fundido do rodapé (todos via `mask`), e do logo de reserva sem WebGL | local (repositório) |
| Favicon | `public/marca/favicon.png` | PNG | 64 × 64 px · 2,3 KB | ícone da aba | local |
| Ícone Apple | `public/marca/apple-touch-icon.png` | PNG | 180 × 180 px · 6,8 KB | ícone na tela inicial do iOS | local |
| Imagem de compartilhamento | `public/og.jpg` | JPEG | 1200 × 630 px · 128,7 KB | `og:image` (prévia em WhatsApp e redes) | local |

> **Não está no repositório:** o arquivo-fonte vetorial do logotipo (AI, SVG ou PDF). Só existe a máscara PNG. Recomenda-se que a CDC guarde o original vetorial junto deste pacote.

## 2. Fotografias do CT de Treinamento (fita de fotos)

Fotos reais enviadas pela CDC. Segundo o README do projeto: 10 de 11 fotos foram usadas (a da bancada da cozinha, a ~45°, ficou de fora), e três foram endireitadas com o maior recorte reto possível (quarto −14°, cozinha −6°, air fryer −10°).

| Nº | Caminho | Formato | Dimensões | Tamanho | Legenda no site |
|---|---|---|---|---|---|
| 01 | `public/fotos/ct-sala-de-informatica.webp` | WebP | 825 × 1100 | 82,9 KB | Sala de Documentos e Tratamento |
| 02 | `public/fotos/ct-sala-de-aula.webp` | WebP | 1467 × 1100 | 112,9 KB | Sala de Recertificação e Visual |
| 03 | `public/fotos/ct-sala-de-estudos.webp` | WebP | 1100 × 1100 | 61,4 KB | Estufas e Consumíveis e Acompanhamento |
| 04 | `public/fotos/ct-apoio.webp` | WebP | 825 × 1100 | 105,9 KB | Sala de Documentos e Tratamento |
| 05 | `public/fotos/ct-treino-pratico.webp` | WebP | 825 × 1100 | 87,6 KB | Acompanhamento e Soldagem |
| 06 | `public/fotos/ct-estufas-e-consumiveis.webp` | WebP | 825 × 1100 | 102,1 KB | Estufas e Consumíveis |
| 07 | `public/fotos/ct-hospedagem.webp` | WebP | 678 × 1100 | 85,7 KB | Hospedagem: quarto coletivo |
| 08 | `public/fotos/ct-cozinha.webp` | WebP | 770 × 1100 | 88,1 KB | Cozinha equipada |
| 09 | `public/fotos/ct-fogao.webp` | WebP | 825 × 1100 | 132,3 KB | Fogão de cinco bocas |
| 10 | `public/fotos/ct-air-fryer-e-misteira.webp` | WebP | 727 × 1100 | 58,5 KB | Air fryer e misteira |

Total: ≈ 917 KB, todas locais. Finalidade: seção 06 "Estrutura e hospedagem" (CEN-03). Textos alternativos na especificação mestre, §8.9.

> **Não está no repositório:** as fotos originais em resolução máxima (antes da conversão para WebP de 1100 px de altura e do endireitamento) e a 11.ª foto descartada. Se a CDC quiser reaproveitar as fotos em impressos ou em telas maiores, precisa guardar os originais por conta própria.

## 3. Materiais de estudo (área do aluno)

| Recurso | Caminho | Formato | Páginas / dimensões | Tamanho | Finalidade | Observação |
|---|---|---|---|---|---|---|
| Apostila teórica | `public/materiais/apostila-teorica.pdf` | PDF 1.5 | 168 páginas | 5,14 MiB | leitor e download | pesquisável (tem texto) |
| Procedimento de recertificação (IB-024 · FBTS) | `public/materiais/procedimento-recertificacao.pdf` | PDF 1.3 | 39 páginas | 7,19 MiB | leitor e download | **escaneado** (imagem, sem texto) |
| Procedimentos de provas práticas | `public/materiais/procedimentos-provas-praticas.pdf` | PDF 1.7 | 5 páginas | 595,6 KB | leitor e download | pesquisável |
| Capa da apostila | `public/materiais/capas/apostila-teorica.webp` | WebP | 560 × 725 | 19,5 KB | cartão e estante | |
| Capa da recertificação | `public/materiais/capas/procedimento-recertificacao.webp` | WebP | 560 × 787 | 22,9 KB | cartão e estante | |
| Capa das provas práticas | `public/materiais/capas/procedimentos-provas-praticas.webp` | WebP | 560 × 792 | 41,2 KB | cartão e estante | |
| Índice de busca | `public/materiais/indice.json` | JSON | chaves `apostila-teorica` (168 páginas de texto) e `procedimentos-provas-praticas` (5) | 273,6 KB | busca nos materiais (CEN-10) | gerado com `pdftotext -layout` (páginas separadas por `\f`). O script de geração **não está** no repositório. O comando está descrito no README do projeto |

Cadastro dos materiais (títulos, sumários, atalhos): `src/aluno/materiais.js` (`MATERIAIS`).

> **Direitos:** o procedimento IB-024 é um documento da FBTS. Confirmar com a CDC se a redistribuição pública desse PDF está autorizada. Isso é uma questão de conteúdo, não técnica, e não foi avaliada.

## 4. Leitor de PDF (biblioteca de terceiros servida localmente)

| Recurso | Caminho | Formato | Tamanho | Finalidade |
|---|---|---|---|---|
| *Worker* do pdf.js 5.7.284 | `public/vendor/pdfjs/pdf.worker.min.mjs` | JS (módulo) | 1,23 MiB | decodifica os PDFs fora da linha principal. O README registra que os caracteres de controle crus foram escritos como `\xNN` para o arquivo poder ser publicado como texto |
| Fontes padrão do PDF | `public/vendor/pdfjs/standard_fonts/` | 10 `.pfb` (Foxit) + 4 `.ttf` (Liberation Sans) + `LICENSE_FOXIT` + `LICENSE_LIBERATION` | ≈ 762 KB | fontes que os PDFs referenciam sem embutir |
| Módulo do pdf.js | vem do pacote npm `pdfjs-dist@5.7.284` (`legacy/build/pdf.min.mjs`) | JS | *chunk* `assets/pdf.min-CFgnYaI8.js` no site publicado | carregado sob demanda |

Tudo local. Licenças: pdf.js Apache-2.0; fontes Foxit e Liberation com as licenças incluídas na pasta.

## 5. Fontes tipográficas (EXTERNAS)

| Família | Eixos / pesos | Origem | Armazenamento |
|---|---|---|---|
| Archivo | `wdth` 62–125, `wght` 100–900 | Google Fonts (`fonts.googleapis.com` + `fonts.gstatic.com`) | **externo**: não há cópia das fontes no repositório |
| Instrument Sans | `wdth` 75–100, `wght` 400–700 | Google Fonts | **externo** |
| IBM Plex Mono | 400, 500 | Google Fonts | **externo** |

URL: `https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wdth,wght@75..100,400..700&display=swap`.

**Risco:** se o Google Fonts ficar inacessível (bloqueio de rede, mudança de política ou rede sem acesso), o site cai para as fontes de reserva ('Arial Narrow', system-ui, Menlo). O **fecho elástico** (TIP-06) perde o eixo de largura e a identidade tipográfica inteira muda. As três famílias são distribuídas pelo Google Fonts sob a SIL Open Font License, que permite guardar e servir cópias próprias (confirme a licença no momento do download; isso não foi verificado nesta análise). **Recomendação:** baixar os arquivos `woff2` variáveis e guardá-los junto do backup (ação a ser feita pela CDC ou num próximo trabalho; nada foi alterado agora).

## 6. Ícones e gráficos

| Recurso | Onde está | Formato | Armazenamento |
|---|---|---|---|
| Ícones (WhatsApp, recursos, vazio, *play*) | inline no `index.html` e em `src/aluno/videos.js` | SVG inline | local (no código) |
| Ícones de Instagram e Facebook | `src/redes.js` (`REDES[].icone`) | SVG inline | local |
| 8 ilustrações das provas | inline no `index.html` (seção `#provas`) | SVG inline, `viewBox 0 0 480 320` | local |
| Rota CDC → SENAI → FBTS | inline no `index.html` | SVG inline | local |
| Grão de filme | `src/estilo/base.css` (`.grao`) | SVG `feTurbulence` em *data URI* | local |
| Logo de partículas, faíscas, clarão | gerados em tempo real (`src/fogo/particulas.js`) | WebGL | local (código) |
| Brasas | geradas em tempo real (`src/fogo/brasas.js`) | Canvas 2D | local (código) |
| Sons | sintetizados em tempo real (`src/motor/som.js`) | Web Audio | local (código). **Não há arquivos de áudio** |
| Animações | todas em código (GSAP e CSS) | n/a | local. **Não há** Lottie, Rive nem vídeos de animação |

## 7. Mídia externa (vídeos)

| Recurso | Origem | Armazenamento | Risco |
|---|---|---|---|
| 3 aulas em vídeo (`F6voYaovgi4`, `31SkkrD4Lcs`, `EgpWC61ftYs`, canal Deiwson Ribeiro) | YouTube: capas em `https://i.ytimg.com/vi/<id>/sddefault.jpg`, player em `https://www.youtube-nocookie.com/embed/<id>` | **externo** | se um vídeo for removido ou ficar privado no YouTube, o cartão continua no site, mas o player mostra erro. Os arquivos de vídeo **não estão** no repositório. As capas responderam HTTP 200 em 3 nov. 2026 |

## 8. Componentes personalizados e configuração (código)

| Arquivo | Papel |
|---|---|
| `index.html` | toda a marcação e o conteúdo (64 KB) |
| `src/main.js` | orquestração e ordem de inicialização |
| `src/motor/carga.js` · `rolagem.js` · `texto.js` · `interacao.js` · `som.js` | abertura, rolagem e barra, tipografia animada, cursor e microinterações, som |
| `src/fogo/particulas.js` · `brasas.js` | logo de partículas com física, faíscas e clarão; brasas do fecho |
| `src/cenas/hero.js` · `provas.js` · `estrutura.js` · `depoimentos.js` · `contato.js` · `aplicativo.js` | cenas da página |
| `src/aluno/materiais.js` · `portal.js` · `leitor.js` · `busca.js` · `videos.js` | área do aluno |
| `src/redes.js` | links das redes (único lugar) |
| `src/estilo/*.css` (10 arquivos) | tokens e estilos |
| `package.json` · `package-lock.json` | dependências com versões travadas |
| `vite.config.js` | *build* (`base: './'`, modo "artefato" com CDN) |
| `.gitignore` | ignora `node_modules/`, `dist/`, `dist-artefato/`, `.DS_Store` |
| `README.md` (do projeto) | como rodar, onde mexer, origem do conteúdo |

Tamanho do `src/`: ~312 KB. Todos locais.

## 9. Serviços e links externos (dependências em tempo de execução)

| Serviço | Uso | Endereço | O que acontece se o serviço sair do ar |
|---|---|---|---|
| Google Fonts | 3 famílias tipográficas | fonts.googleapis.com / fonts.gstatic.com | fontes de reserva; perda da identidade tipográfica e do fecho elástico (ver §5) |
| WhatsApp | agendamento, pré-inscrição, botão flutuante | `wa.me/5521982570418` | os botões param de abrir a conversa. Telefone e e-mail continuam no site |
| Kiwify | compra do curso e login da área do curso | `pay.kiwify.com.br/b2fQ0VB`, `dashboard.kiwify.com.br/login` | a compra e o acesso ao curso gravado param. **O conteúdo do curso fica na Kiwify** e não neste backup |
| YouTube | 3 vídeos da área comum | youtube-nocookie.com, i.ytimg.com | cartões sem vídeo (ver §7) |
| Google Maps | "Abrir no mapa" | google.com/maps/search | o link não abre o mapa. O endereço continua escrito |
| Instagram / Facebook | perfis oficiais | instagram.com/deiwsonrosecdcoficial, facebook.com/cdctreinamentos.com.br | links quebrados |
| Aplicativo CDC (Lovable) | botão "Conhecer o aplicativo" | `cdc-capacita-o-em-qualidade.lovable.app` | link quebrado. O app é **outro projeto** (repositório privado `adrianlucaslops123-code/cdc-capacita-o-em-qualidade`, não analisado aqui). A prévia da questão no site **não** depende dele |
| Vercel | hospedagem do site | `cdc-cursos-kappa.vercel.app` | o site sai do ar. Pode ser republicado em qualquer hospedagem estática a partir do repositório (README, §6–7) |
| GitHub | guarda do código e dos recursos | github.com/adrianlucaslops123-code/landing-page-cdc | perda do histórico. **Manter cópias** fora do GitHub (README, §7) |
| jsDelivr (só no modo "artefato") | bibliotecas por CDN | cdn.jsdelivr.net | só afeta o *build* `npm run build:artefato`. O site publicado **não usa** CDN |

Todos responderam normalmente em 3 nov. 2026. **OBSERVADO.**

## 10. Dados guardados no navegador do visitante

| Chave | Conteúdo | Observação |
|---|---|---|
| `localStorage['cdc-som']` | `'1'` ou `'0'` | preferência de som |
| `localStorage['cdc-aluno-v1']` | `{ <id>: { pagina, total, quando } }` | progresso de leitura |

Não há servidor nem conta: esses dados existem só no aparelho de cada visitante e não precisam de backup.

## 11. Referências visuais desta análise (novas, incluídas no pacote)

Pasta `CDC_SITE_BACKUP/REFERENCIAS_VISUAIS/`: 36 capturas em WebP (qualidade 88, ≈ 4,9 MB no total), feitas no site publicado em 3 nov. 2026 com Chromium headless (Playwright). São referência de fidelidade, não recursos do site.

| Prefixo | Conteúdo |
|---|---|
| `d01`–`d25` | computador, 1440×900, DPR 1: abertura, hero, metal aquecido, sequência do arco (90 / 340 / 1 240 ms), estados do cursor, cursor "ABRIR" sobre o acesso, cordão em 50 %, manifesto, equipe, treinamentos, provas 01 / 04 / 08, material, estrutura, fita de fotos, depoimentos, área do aluno, dúvidas, aplicativo, fecho, contato e o efeito colateral da volta ao topo (1200×800) |
| `m01`–`m06` | celular, iPhone 13 emulado (390×664, DPR 3): hero, menu aberto, provas em lista, fita com rolagem nativa, treinamentos, fecho |
| `v01`–`v04` | tablet em pé (768×1024), tablet deitado (1024×768), notebook (1280×720), monitor (2560×1440) |
| `r01` | movimento reduzido: hero com o logo parado |

> **Atenção ao comparar:** o ambiente de captura usa WebGL por software. Como o relógio da física das partículas avança no máximo 1/30 s por quadro, a montagem do logo fica mais lenta que num aparelho real. Por isso `d02` e `v04` mostram a montagem ainda em andamento (metal espalhado e branco). O estado final do logo aparece em `d03`–`d06`, `d25` e `r01`.

## 12. O que precisa acompanhar o backup

**Indispensável (está no repositório `landing-page-cdc`):** `index.html`, `src/` inteiro, `public/` inteiro (marca, fotos, materiais, vendor, og), `package.json`, `package-lock.json`, `vite.config.js`.

**Recomendado guardar fora do repositório (não existe hoje em nenhum lugar deste projeto):**

1. Arquivo vetorial original do logotipo CDC.
2. Fotos originais em resolução máxima (incluindo a 11.ª).
3. Arquivos `woff2` das 3 famílias tipográficas.
4. Cópia dos 3 vídeos do YouTube (pelo dono do canal).
5. Exportação do conteúdo do curso na Kiwify.
6. Configuração do projeto na Vercel (domínios, *build*) e acesso ao registro do domínio `cdccursos.com.br`.
7. Código do aplicativo CDC (projeto Lovable separado), se ele também precisar de preservação.

**Recursos que deixam de funcionar se o serviço for descontinuado:** fontes (Google Fonts), vídeos (YouTube), compra e área do curso (Kiwify), botões de WhatsApp, mapa, links de redes sociais, link do aplicativo (Lovable) e a própria publicação (Vercel). Nenhum deles impede a página de carregar, exceto a hospedagem.
