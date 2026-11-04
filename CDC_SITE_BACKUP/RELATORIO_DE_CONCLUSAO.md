# Relatório de conclusão: engenharia reversa e preservação do site CDC

**Site:** https://cdc-cursos-kappa.vercel.app/ · **Código:** `adrianlucaslops123-code/landing-page-cdc`, commit `65c37e7` · **Período:** 3 e 4 nov. 2026 · **Natureza do trabalho:** só análise, documentação e organização. Nada foi alterado no site, no repositório do site ou na hospedagem. Nenhuma migração foi executada.

---

## 1. O que foi analisado

| Item | Como |
|---|---|
| Código-fonte inteiro | leitura de `index.html` (845 linhas), dos 10 arquivos CSS, dos 20 módulos JS, de `vite.config.js`, `package.json`, `package-lock.json` e do README do projeto |
| Correspondência com o site publicado | o `<body>` publicado é idêntico ao do repositório. O *build* refeito fora da Vercel gerou HTML, JS, CSS, *chunk* do pdf.js e os 38 arquivos públicos **idênticos byte a byte** aos publicados |
| Comportamento real | Chromium headless (Playwright) no site publicado: 1440×900, 1200×800, 1280×720, 1024×768, 768×1024, 2560×1440, iPhone 13 e movimento reduzido. Medidos: estados e latência do cursor, rótulo "ABRIR", sequência do arco (90 / 340 / 1 240 ms), cordão de solda em 9 posições, cenas presas (alturas e deslocamentos), barra (sumiço e retorno), tipografia por largura, fecho elástico, abertura (contador e cortina), classes de estado, densidade do canvas, efeitos colaterais |
| Cálculos | número real de partículas (algoritmo replicado sobre a máscara real), conversão das unidades 3D em px, contrastes WCAG, escalas `clamp()` por largura, constantes de mola, meia-vida do clarão |
| Recursos e serviços | dimensões e tamanhos de todos os arquivos de `public/`, disponibilidade dos serviços externos, cabeçalhos da hospedagem, domínio antigo |

## 2. Documentos criados (todos em `CDC_SITE_BACKUP/` do repositório `adrianlucaslops123-code/reverse`)

| # | Documento | Conteúdo |
|---|---|---|
| 1 | `CDC_SITE_MASTER_SPECIFICATION.md` | as 18 seções pedidas, mais fatos × inferências e limitações. Conteúdo institucional literal (conferido por script: os 435 textos e os 44 atributos `alt`/`placeholder`/`aria-label` do `index.html` estão no documento) |
| 2 | `CDC_SITE_RECONSTRUCTION_PROMPT.md` | prompt mestre autônomo com 3 modos (reconstrução fiel, reutilização com outra identidade, alteração controlada), regras, anti-padrões, decisões a pedir e apêndice de parâmetros |
| 3 | `CDC_DESIGN_SYSTEM.md` | tokens, cores com contraste, tipografia com escala por tela, espaço, forma, sombras, estados, ícones, imagens, *motion*, responsividade, camadas |
| 4 | `ASSETS_INVENTORY.md` | todos os recursos com caminho, formato, dimensões, finalidade, armazenamento e risco |
| 5 | `TECHNICAL_DEPENDENCIES.md` | pilha, versões, licenças, serviços, requisitos, Lovable/Supabase/Vercel e o teste de reprodução |
| 6 | `README.md` | estrutura, ambiente, instalação, execução, serviços, nova publicação, migração, domínio, preservação |
| 7 | `CDC_DESIGN_LIBRARY_INDEX.md` | índice das 42 experiências, estados reais, efeitos colaterais, ideias futuras, receitas e mapa dos "12 sistemas" |
| 8 | `CDC_DESIGN_LIBRARY/` | 42 fichas técnicas individuais |
| 9 | `REFERENCIAS_VISUAIS/` | 36 capturas do site publicado (WebP, ≈ 4,9 MB) |
| 10 | `RELATORIO_DE_CONCLUSAO.md` | este relatório |

## 3. Experiências interativas pedidas: o que foi encontrado de fato

| Pedido | O que o código implementa | Ficha |
|---|---|---|
| Cursor "pequena esfera com ponta de arco elétrico na parte superior" | **Ponto de 6 px** (`mix-blend-mode: difference`) + **anel de 38 px** com 0,38 s de atraso. Estados: link 58 px, rótulo 76 px, calor 120 px no hero. **Não existe** ponta de arco desenhada no código. O efeito de "ponta incandescente" vem das partículas do logo aquecidas sob o cursor. Sobre o laranja, o ponto aparece azul (`#0d79d6`, efeito `difference`) | CUR-01 |
| Indicador circular laranja com "ABRIR" | disco de 76 px `#fb781e` com texto mono de 10 px. Aparece em 7 elementos: "Abrir" (Vídeos, Material), "Entrar" (login), "Ler" (3 materiais), "Som"/"Mudo" (botão de som). Linha do tempo completa de entrada, clique, saída e retorno documentada | CUR-02 |
| Interação especial com o logo CDC | anel de calor de 120 px (≈ alcance de 127 px do maçarico), aquecimento, faíscas ao passar rápido, inclinação do bloco, arco no clique | CUR-01 §6, ARC-01 a ARC-03 |
| Aquecimento do metal e abertura do arco | física por ponto (raio 1,05; aquece 2,4/s; esfria τ 1,1 s; mola 55; atrito 2,6) e clique com clarão WebGL + flash CSS + explosão + 240 faíscas + tremor + som. Arco automático aos 2,15 s | ARC-01, ARC-02, ARC-03 |
| Scroll inspirado em eletrodo | **cordão de solda**: trilho de 10 px × 34vh à direita, escamas a cada 7 px, cores de revenimento junto da ponta, ponta incandescente de 9 px tremulando, número 00–100 | ROL-01 |
| Botões | brasa (varredura de luz), vidro, magnéticos (0,28 / 0,36), onda no clique, WhatsApp que se expande | BOT-01 a BOT-06 |

## 4. Comportamentos que diferem da intenção do código (registrados; nada foi corrigido)

1. O anel do cursor **não encolhe** ao clicar: o GSAP grava `scale: none` inline (CUR-01 §10).
2. O WhatsApp flutuante **deixa de se esconder** no topo depois do primeiro *hover*: o GSAP grava `translate: none` (BOT-02 §4).
3. O lema "Capacitação em qualidade" e o indicador "Role" **somem** depois de descer e voltar ao topo (ARC-04 §6).
4. O contador da abertura pode **parar em 090** quando o logo demora mais de 1 s (CAR-01 §5).
5. A rota da seção Estrutura **anima mesmo com movimento reduzido** (CEN-04).
6. A centralização vertical do texto do hero vira um valor fixo em px no primeiro quadro (−180,07 px em 1440×900) e não acompanha redimensionamentos (ARC-04, `CDC_DESIGN_LIBRARY_INDEX.md` §4).

## 5. Confirmações pedidas

| Pergunta | Resposta |
|---|---|
| Os cinco documentos do pacote de preservação foram criados? | **Sim**: `CDC_SITE_MASTER_SPECIFICATION.md`, `CDC_SITE_RECONSTRUCTION_PROMPT.md`, `CDC_DESIGN_SYSTEM.md`, `ASSETS_INVENTORY.md`, `TECHNICAL_DEPENDENCIES.md`, mais o `README.md`. Também foram criados o `CDC_DESIGN_LIBRARY_INDEX.md` e a pasta `CDC_DESIGN_LIBRARY/` (42 fichas), pedidos na missão seguinte |
| Os recursos necessários foram inventariados? | **Sim**: marca (4), fotos (10), materiais (7 arquivos), pdf.js (*worker* + 16 arquivos de fontes e licenças), fontes externas (3 famílias), ícones e gráficos, vídeos externos (3), código e configuração, serviços externos (10) e dados locais (2 chaves) |
| As dependências externas foram identificadas? | **Sim**: Google Fonts, WhatsApp, Kiwify, YouTube, Google Maps, Instagram, Facebook, app no Lovable e a hospedagem na Vercel. **Lovable Cloud e Supabase não são usados** pelo site |
| Existe informação pendente? | **Sim** (§6) |
| A documentação permite orientar uma reconstrução em outro ambiente? | **Sim.** O *build* foi refeito fora da Vercel com o procedimento do `README.md` e saiu idêntico ao publicado. A especificação, o Design System, as fichas e o prompt descrevem o site com valores exatos para quem não tiver o código |
| Os arquivos estão organizados e incluídos no repositório? | **Sim**: todos em `CDC_SITE_BACKUP/` no repositório `adrianlucaslops123-code/reverse`, branch `claude/cdc-site-reverse-engineering-ttnzg5` |

## 6. Pendências e informações que não puderam ser verificadas

1. **FPS e tempo de quadro** reais: não medidos (o ambiente usa WebGL por software).
2. **Som**: não ouvido (sem saída de áudio). Valores do código.
3. **Não acionados em execução** (código lido por inteiro): área de transferência, envio ao WhatsApp, abertura do portal, leitor de PDF, vídeos, acordeão, pop-up de redes, troca automática de 7 s dos depoimentos e resposta da prévia do app.
4. **Configuração do projeto na Vercel** (Node, comando de *build*, domínios, integração com o GitHub): não está no repositório.
5. **Contador da abertura chegando a 100** em máquinas rápidas: não verificado.
6. **Endereços das páginas do site antigo** (Wix), necessários para redirecionamentos numa troca de domínio: não levantados.
7. **Direito de redistribuir** o PDF do procedimento IB-024 (FBTS) publicamente: questão de conteúdo, não avaliada.
8. **Licenças** das fontes e da GSAP: registradas como declaradas pelos pacotes. Confirmar nos termos atuais antes de reutilizar fora da CDC.
9. O **aplicativo** no Lovable é um projeto separado e não foi analisado.

## 7. Recursos que ainda precisam ser preservados fora dos repositórios

1. Arquivo vetorial original do logotipo CDC (só existe a máscara PNG).
2. Fotos originais em alta resolução (e a 11.ª foto não usada).
3. Arquivos `woff2` das fontes Archivo, Instrument Sans e IBM Plex Mono (hoje vêm do Google Fonts).
4. Cópia dos 3 vídeos do YouTube.
5. Conteúdo do curso na Kiwify.
6. Acesso de titular ao domínio `cdccursos.com.br` (Registro.br) e às contas da Vercel, Kiwify, YouTube, Instagram e Facebook.
7. Cópias do repositório `landing-page-cdc` fora do GitHub (procedimento no `README.md` §7).

## 8. Serviços externos que precisam continuar ativos

Vercel (ou outra hospedagem), Google Fonts (ou fontes próprias), WhatsApp, Kiwify, YouTube, Google Maps, Instagram, Facebook e o app no Lovable. Sem eles a página **continua carregando**, mas perde a tipografia original, os vídeos, a compra e a área do curso, os botões de WhatsApp, o mapa e os links. Sem a hospedagem, o site sai do ar até ser republicado a partir do repositório.

## 9. Fatos × inferências

- **Fatos** (EXATO / OBSERVADO): valores lidos no código e medidos no site, a identidade do *build* e a disponibilidade dos serviços.
- **Cálculos** (CALCULADO): conversões e grandezas derivadas, sempre indicadas.
- **Inferências** (marcadas no texto): as causas dos efeitos colaterais, as recomendações "Como adaptar" das fichas e as ideias futuras (que **não** existem no site e estão separadas no índice da biblioteca, §5).
