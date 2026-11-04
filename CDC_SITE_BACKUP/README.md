# CDC_SITE_BACKUP: pacote de preservação e portabilidade do site da CDC

Pacote de documentação técnica e visual do site da **CDC Capacitação em Qualidade** (`https://cdc-cursos-kappa.vercel.app/`), criado por engenharia reversa do site publicado e do código-fonte em 3 e 4 nov. 2026. O objetivo é que a identidade, a estrutura e as experiências do site **não dependam de uma plataforma** e possam ser reconstruídas, migradas ou reaproveitadas.

> **Nada foi alterado** no site publicado, no repositório do site (`landing-page-cdc`) nem na hospedagem. Nenhuma migração foi executada. Este pacote só documenta e organiza.

---

## 1. O que há neste pacote

| Arquivo / pasta | Para que serve |
|---|---|
| `README.md` (este) | visão geral, como usar o pacote, migração, publicação e preservação |
| `CDC_SITE_MASTER_SPECIFICATION.md` | especificação completa: estrutura, **conteúdo literal**, catálogo de 56 animações, funcionalidades, arquitetura, regras, critérios de fidelidade e checklist |
| `CDC_SITE_RECONSTRUCTION_PROMPT.md` | **prompt mestre autônomo** para outra IA ou ferramenta: reconstruir o site (modo A), reutilizar experiências noutro projeto (modo B) ou alterar o site sem perder a identidade (modo C) |
| `CDC_DESIGN_SYSTEM.md` | tokens, cores (com contraste), tipografia (com escala por tela), espaços, sombras, estados, *motion*, responsividade, camadas |
| `CDC_DESIGN_LIBRARY_INDEX.md` | índice da biblioteca: 42 experiências, estado real, portabilidade, efeitos colaterais, ideias futuras, receitas de combinação |
| `CDC_DESIGN_LIBRARY/` | 42 fichas técnicas individuais (cursor, rótulo "ABRIR", partículas, arco, faíscas, cordão de solda, tipografia, botões, cenas, fundos, som) |
| `ASSETS_INVENTORY.md` | inventário de recursos (logo, fotos, PDFs, fontes, ícones, mídia, serviços externos) com caminhos e riscos |
| `TECHNICAL_DEPENDENCIES.md` | pilha, versões, licenças, serviços, requisitos e o **teste de reprodução fora da Vercel** |
| `REFERENCIAS_VISUAIS/` | 36 capturas do site publicado (computador, celular, tablet, monitor, movimento reduzido), para comparar reconstruções |
| `RELATORIO_DE_CONCLUSAO.md` | relatório final: o que foi analisado, criado, verificado e o que ficou pendente |

**Ordem de leitura sugerida:** este README → especificação mestre → design system → índice da biblioteca → fichas que interessarem → inventário e dependências.

---

## 2. Documentação × backup real × serviços externos

Não considere o site preservado só porque estes documentos existem. São três coisas diferentes:

| Camada | O que é | Onde está hoje | Situação |
|---|---|---|---|
| **Documentação** (este pacote) | descreve como o site é e funciona | repositório `adrianlucaslops123-code/reverse`, pasta `CDC_SITE_BACKUP/` | **criada** |
| **Backup real dos arquivos** | o código e os recursos que de fato reconstroem o site (HTML, CSS, JS, logo, fotos, PDFs, pdf.js) | repositório `adrianlucaslops123-code/landing-page-cdc` (GitHub, público), commit `65c37e7` | **existe, mas só num lugar (GitHub)**. Faça cópias (§7) |
| **Serviços externos** | o que precisa continuar ativo para o site funcionar por completo | Vercel (hospedagem), Google Fonts, WhatsApp, Kiwify, YouTube, Google Maps, Instagram, Facebook, app no Lovable | **dependem de terceiros** (riscos em `ASSETS_INVENTORY.md` §9) |

O que **não existe em nenhum dos dois repositórios** e precisa ser guardado pela CDC: arquivo vetorial do logotipo, fotos originais em alta resolução, arquivos das fontes, cópias dos vídeos, conteúdo do curso na Kiwify, acesso ao domínio `cdccursos.com.br` e às contas da Vercel e da Kiwify (lista completa em `ASSETS_INVENTORY.md` §12).

---

## 3. Entender a estrutura do projeto do site

O site é uma **página única estática** feita com HTML, CSS e JavaScript puro (ES Modules), empacotada com Vite. Não tem framework, servidor, banco de dados, login próprio nem variáveis de ambiente.

```
landing-page-cdc/
  index.html            todas as seções, o portal da área do aluno e o pop-up
  package.json          gsap 3.15.0 · lenis 1.3.27 · three 0.186.1 · pdfjs-dist 5.7.284 · vite 8.3.5
  vite.config.js        base './' (funciona na raiz ou numa subpasta)
  public/               copiado como está para o site: marca/, fotos/, materiais/, vendor/pdfjs/, og.jpg
  src/main.js           liga tudo na ordem certa
  src/motor/            rolagem, tipografia, cursor e microinterações, som, abertura
  src/fogo/             logo de partículas (three.js) e brasas (canvas)
  src/cenas/            hero, provas, estrutura, depoimentos, contato, aplicativo
  src/aluno/            portal, leitor de PDF, busca, vídeos, cadastro dos materiais
  src/estilo/           10 arquivos CSS (tokens primeiro)
```

Onde mexer (do README do próprio projeto): textos, preços, links e contatos em `index.html`; cores, fontes, raios e curvas em `src/estilo/tokens.css`; o logo de partículas no bloco `AJUSTE` de `src/fogo/particulas.js`; o formato do logo em `public/marca/cdc-mascara.png`; provas em `index.html` + `src/cenas/provas.js`; som em `src/motor/som.js`; fotos em `public/fotos/`; redes em `src/redes.js`; materiais e vídeos em `src/aluno/materiais.js`.

---

## 4. Preparar o ambiente e instalar

1. Instale o **Node.js 22.13 ou mais novo** (o teste deste pacote usou o Node 22.23.4 com o npm 10.9.9).
2. Instale o Git.
3. Clone e instale exatamente as versões travadas:

```bash
git clone https://github.com/adrianlucaslops123-code/landing-page-cdc.git
cd landing-page-cdc
git checkout 65c37e7      # opcional: a versão exata documentada aqui
npm ci                    # usa o package-lock.json; não atualiza nada
```

Use `npm ci`, e não `npm install` nem `npm update`, para não trocar versões.

## 5. Executar localmente

```bash
npm run dev          # desenvolvimento: http://localhost:5174
npm run build        # gera dist/ (o site completo)
npm run preview      # serve dist/ em http://localhost:4174 para conferir
```

Não há `.env` nem serviços a configurar para rodar.

**Verificado em 4 nov. 2026:** o `npm run build` feito fora da Vercel gerou arquivos **idênticos byte a byte** aos publicados (HTML, JS, CSS, *chunk* do pdf.js e os 38 arquivos de `public/`). Detalhes em `TECHNICAL_DEPENDENCIES.md` §11.

## 6. Configurar os serviços externos (opcional)

Nenhum serviço exige chave ou conta para o site funcionar. Para trocar algum endereço:

| Serviço | Onde se configura |
|---|---|
| WhatsApp (número e mensagens) | links `wa.me/5521982570418?text=…` em `index.html` e a constante `ZAP` em `src/cenas/contato.js` |
| Kiwify (checkout e login) | `index.html` (`pay.kiwify.com.br/b2fQ0VB`) e `KIWIFY_LOGIN` em `src/aluno/materiais.js` |
| Vídeos | `VIDEOS` em `src/aluno/materiais.js` (ID do YouTube e início em segundos) |
| Redes sociais | `REDES` em `src/redes.js` (único lugar) |
| Aplicativo | botão "Conhecer o aplicativo" em `index.html` |
| Fontes | `<link>` do Google Fonts no `<head>` do `index.html`. Para não depender do Google, baixe os `woff2` e sirva-os pela pasta `public/` com `@font-face` (mudança futura: **não foi feita**) |

## 7. Preservar o backup real (recomendações)

1. **Cópia completa com histórico, num único arquivo:**
   ```bash
   git clone --mirror https://github.com/adrianlucaslops123-code/landing-page-cdc.git
   cd landing-page-cdc.git && git bundle create ../cdc-site-65c37e7.bundle --all
   ```
   O `.bundle` restaura o repositório inteiro com `git clone cdc-site-65c37e7.bundle`. Tamanho esperado: a partir de ~11 MB (medido num clone raso; com o histórico completo pode ser maior).
2. **Cópia do site pronto:** guarde também a pasta `dist/` gerada pelo `npm run build`, compactada. É o site que pode ir para qualquer hospedagem sem Node.
3. **Regra 3-2-1:** três cópias, em dois tipos de mídia, uma fora do GitHub (ex.: nuvem da CDC + disco externo).
4. **Guarde junto:** este pacote (`CDC_SITE_BACKUP/`) e os itens do `ASSETS_INVENTORY.md` §12 que não estão em repositório nenhum.
5. Não há segredos no repositório. Os dados de contato que aparecem nele já são públicos no site.
6. Os dois repositórios (`landing-page-cdc` e `reverse`) estão **públicos** no GitHub. Avalie se o PDF do procedimento IB-024 (da FBTS) pode continuar público.

## 8. Fazer uma nova publicação

### 8.1 Na Vercel (hospedagem atual)

A configuração do projeto na Vercel não está no repositório (NÃO IDENTIFICADO). Para um projeto novo ou para conferir o atual:

1. Na Vercel, importe o repositório `landing-page-cdc`.
2. *Framework preset*: **Vite** (detectado sozinho). *Build command*: `npm run build`. *Output directory*: `dist`. *Install command*: `npm ci`.
3. Versão do Node nas configurações do projeto: 22.x ou mais nova.
4. Sem variáveis de ambiente.
5. Publique. Se a integração com o GitHub estiver ligada, cada `push` no branch de produção gera uma publicação nova.

### 8.2 Em qualquer outra hospedagem estática

| Hospedagem | Como |
|---|---|
| Netlify | *build* `npm run build`, pasta `dist` |
| Cloudflare Pages | *framework* Vite, *build* `npm run build`, pasta `dist` |
| GitHub Pages | publicar a pasta `dist/` (funciona numa subpasta porque `base: './'`) |
| Servidor próprio (Apache, Nginx) ou S3 + CDN | enviar o conteúdo de `dist/` para a raiz (ou uma subpasta) |

Cuidados técnicos em qualquer hospedagem:

- Servir `.mjs` com tipo JavaScript (`text/javascript`). O *worker* do leitor é `vendor/pdfjs/pdf.worker.min.mjs`. Servidores antigos às vezes não conhecem a extensão `.mjs`, e aí o leitor de PDF não abre.
- Servir as fontes `.pfb` e `.ttf` de `vendor/pdfjs/standard_fonts/`.
- Não é preciso regra de reescrita: a página é única e a navegação interna usa `#`.
- Cache: os arquivos de `assets/` têm *hash* no nome e podem ter cache longo. O `index.html` deve ter cache curto (na Vercel: `max-age=0, must-revalidate`).

## 9. Migrar para outra hospedagem, passo a passo (procedimento; não executado)

1. Faça o backup do §7.
2. Gere `dist/` com `npm ci && npm run build` (ou conecte o repositório na nova hospedagem, como no §8).
3. Publique no endereço provisório da nova hospedagem.
4. Valide com o checklist da `CDC_SITE_MASTER_SPECIFICATION.md` §18 e compare com `REFERENCIAS_VISUAIS/` em 1440×900 e no celular.
5. Aponte o domínio (§10).
6. Mantenha a publicação antiga ativa por alguns dias, até a propagação do DNS terminar.
7. Depois de confirmar, desative a publicação antiga.

## 10. Preservar e apontar o domínio

- **Situação observada em 3 nov. 2026:** `cdccursos.com.br` redireciona para `www.cdccursos.com.br`, que é servido pelo **Wix** (o site antigo). O site novo está só em `cdc-cursos-kappa.vercel.app`.
- Domínios `.com.br` são registrados no **Registro.br**. Antes de mexer, descubra **onde estão os servidores de DNS** do domínio: no Registro.br ou no Wix. A mudança é feita nesse lugar.
- Para apontar o domínio para o site novo na Vercel: adicione `cdccursos.com.br` e `www.cdccursos.com.br` no projeto da Vercel. Ela mostra os registros de DNS exatos a criar (normalmente um registro A no domínio principal e um CNAME no `www`). Crie esses registros onde o DNS estiver. O HTTPS é emitido pela Vercel depois que o DNS propagar.
- **Antes de desligar o Wix:** guarde uma cópia do conteúdo do site antigo e anote os endereços das páginas antigas. Se for preciso redirecionar endereços antigos para as seções novas (ex.: uma página "contato" para `/#contato`), isso exige um arquivo de configuração na hospedagem (ex.: `vercel.json` com `redirects`). Isso seria uma alteração futura e **não foi feito**. Os endereços do site antigo não foram levantados nesta análise.
- Garanta que a CDC tenha o acesso de titular ao domínio no Registro.br.

## 11. Preservar imagens e demais recursos

- Os recursos do site estão em `public/` no repositório. Não renomeie nem mova: os caminhos são usados no HTML, no CSS e no JS (`ASSETS_INVENTORY.md`).
- `public/marca/cdc-mascara.png` é o recurso mais crítico: o logo de partículas, a abertura e todos os logos dependem dele.
- Para trocar uma foto: mesmo nome, formato WebP e mesma proporção. Ou atualize `width`, `height` e `--ar` no `index.html`.
- Para trocar ou acrescentar um PDF: siga o README do projeto (colocar em `public/materiais/`, cadastrar em `MATERIAIS`, gerar o texto para `indice.json` com `pdftotext -layout`).

## 12. Usar a documentação em projetos futuros

- **Jeito mais simples:** guarde o ZIP `CDC_PACOTE_COMPLETO_<data>.zip`, que tem esta documentação **e** o código do site. Numa conversa nova, anexe o ZIP, preencha o `MODELO_DE_PEDIDO.txt` (na raiz do ZIP) com as alterações e cole o texto. Instruções no `LEIA-ME_PRIMEIRO.md` da raiz do ZIP. Para refazer o ZIP: `gerar_pacote_zip.py` (raiz do repositório `reverse` ou do ZIP).
- **Reconstruir o site:** entregue à ferramenta o `CDC_SITE_RECONSTRUCTION_PROMPT.md` com os anexos que ele lista, e peça o **modo A**.
- **Reutilizar uma experiência** (ex.: o cursor com "ABRIR" ou o cordão de solda) com outra identidade: mesmo prompt, **modo B**, citando os IDs das fichas (ex.: "use CUR-01, CUR-02 e ROL-01 com a paleta do projeto X").
- **Alterar o site da CDC** sem perder a identidade: **modo C**.
