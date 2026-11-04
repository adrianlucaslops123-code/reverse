# TECHNICAL_DEPENDENCIES: tecnologias, dependências e portabilidade

Levantamento técnico do site `https://cdc-cursos-kappa.vercel.app/` a partir do repositório `adrianlucaslops123-code/landing-page-cdc` (commit `65c37e7`), do `package-lock.json` (formato 3) e do site publicado.

Legenda: **EXATO** (arquivo do projeto) · **OBSERVADO** (site publicado) · **NÃO IDENTIFICADO** (fora do repositório).

---

## 1. Resumo de portabilidade

| Pergunta | Resposta |
|---|---|
| Framework | **Nenhum** framework de componentes (sem React, Vue, Svelte, Next etc.). HTML + CSS + JavaScript com ES Modules |
| *Bundler* | **Vite 8.3.5** (com Rolldown 1.2.16 e LightningCSS 1.33.0) |
| Tipo de site | **estático**: o *build* gera arquivos HTML/CSS/JS/mídia que qualquer hospedagem serve |
| Backend / API própria | **nenhum** |
| Banco de dados | **nenhum** |
| Autenticação | **nenhuma** no site (o login do curso é na Kiwify) |
| Variáveis de ambiente | **nenhuma**. Só `import.meta.env.MODE`, definido pelo próprio Vite (`production` ou `artefato`) |
| Chaves, tokens, segredos | **nenhum** no código |
| Dependência do **Lovable Cloud** | **nenhuma**. O site não foi gerado pelo Lovable nem roda nele. Há só um *link* para o aplicativo separado `cdc-capacita-o-em-qualidade.lovable.app` |
| Dependência do **Supabase** | **nenhuma** (sem `@supabase/*`, sem URL de projeto, sem chamadas de API) |
| Dependência da **Vercel** | só como hospedagem. Não há `vercel.json`, funções *serverless*, *edge middleware* nem SDK da Vercel no código |
| Pode rodar fora da plataforma atual? | **Sim**, em qualquer hospedagem estática (Vercel, Netlify, Cloudflare Pages, GitHub Pages, S3 + CDN, servidor Apache/Nginx) ou numa subpasta, porque `base: './'` gera caminhos relativos |

---

## 2. Dependências diretas (`package.json`, EXATO)

| Pacote | Versão travada | Tipo | Licença (do `package-lock`) | Uso no site |
|---|---|---|---|---|
| `gsap` | 3.15.0 | produção | "Standard 'no charge' license" (`https://gsap.com/standard-license`) | animações, ScrollTrigger (cenas presas, *scrub*), SplitText (títulos, manifesto, depoimentos), ScrambleTextPlugin (letras e contadores), `quickTo`/`quickSetter` (cursor, magnetismo, cartões) |
| `lenis` | 1.3.27 | produção | MIT | rolagem suave no computador |
| `three` | 0.186.1 | produção | MIT | logo de partículas WebGL, faíscas e clarão |
| `pdfjs-dist` | 5.7.284 | produção | Apache-2.0 | leitor de PDF (versão *legacy*, importada sob demanda) |
| `vite` | 8.3.5 | desenvolvimento | MIT | servidor de desenvolvimento e *build* |

Scripts (EXATO):

```json
"dev": "vite --port 5174",
"build": "vite build",
"preview": "vite preview --port 4174",
"build:artefato": "vite build --mode artefato"
```

## 3. Dependências indiretas relevantes (`package-lock.json`, EXATO)

| Pacote | Versão | Observação |
|---|---|---|
| `rolldown` | 1.2.16 | *bundler* do Vite 8 (binários nativos por plataforma: `@rolldown/binding-*`) |
| `lightningcss` | 1.33.0 (MPL-2.0) | minificação do CSS (binários nativos `lightningcss-*`) |
| `postcss` | 8.5.32 | |
| `tinyglobby` 0.2.17, `fdir` 6.5.0, `picomatch` 4.0.7, `nanoid` 3.3.20, `picocolors` 1.1.1, `source-map-js` 1.2.2, `detect-libc` 2.1.2, `@oxc-project/types` 0.156.0, `@rolldown/pluginutils` 1.0.1 | | utilitários do Vite |
| `@napi-rs/canvas` | 0.1.100 | dependência **opcional** do `pdfjs-dist` (só para usar o pdf.js no Node; o site não precisa) |
| `fsevents` | 2.3.3 | opcional, só no macOS |

## 4. Requisitos do ambiente

| Requisito | Valor | Origem |
|---|---|---|
| Node.js | **22.13 ou mais novo** (ou 24 LTS) | `vite`: `^20.19.0 \|\| >=22.12.0`; `pdfjs-dist`: `>=22.13.0 \|\| >=24`. Com Node 20 o Vite roda, mas o `npm` avisa sobre a versão do `pdfjs-dist` |
| npm | qualquer versão que leia `lockfileVersion: 3` (npm 7+) | `package-lock.json` |
| Sistema | Linux, macOS ou Windows (os binários nativos do Rolldown e do LightningCSS cobrem as três) | `package-lock.json` |
| Navegador (visitante) | moderno, com ES Modules, WebGL (o logo tem reserva sem WebGL), `IntersectionObserver`, `ResizeObserver`, CSS `mask`, `clip-path`, `backdrop-filter`, `svh` e fontes variáveis. O *target* do *build* é `es2020` | `vite.config.js` |
| Versão do Node usada na Vercel | **NÃO IDENTIFICADO** (fica nas configurações do projeto na Vercel) | n/a |

## 5. Configuração de *build* (`vite.config.js`, EXATO)

```js
export default defineConfig(({ mode }) => ({
  base: './',                       // caminhos relativos: funciona na raiz ou numa subpasta
  plugins: mode === 'artefato' ? [bibliotecasDoCdn()] : [],
  build: {
    target: 'es2020',
    outDir: mode === 'artefato' ? 'dist-artefato' : 'dist',
    assetsInlineLimit: 0,           // nenhum arquivo vira data URI: todos saem como arquivo
  },
}))
```

Dois modos:

| Modo | Comando | Saída | Bibliotecas | Uso |
|---|---|---|---|---|
| normal (publicado) | `npm run build` | `dist/` | dentro do pacote (o JS principal publicado tem 758 KB; o pdf.js é um *chunk* separado) | **é o que está na Vercel** (OBSERVADO: o *bundle* publicado contém o three.js e não faz chamadas ao jsDelivr) |
| artefato | `npm run build:artefato` | `dist-artefato/` | por CDN (jsDelivr), versões travadas: `three@0.186.1`, `gsap@3.15.0` (+ `ScrollTrigger`, `SplitText`, `ScrambleTextPlugin`), `lenis@1.3.27`, `pdfjs-dist@5.7.284` | versão para publicar como "artefato" (o leitor não oferece download; as fontes `.pfb` do pdf.js não são servidas) |

Arquivos gerados no site publicado (OBSERVADO): `index.html`, `assets/index-DsBXkgpX.js`, `assets/index-D7O1k9YW.css`, `assets/pdf.min-CFgnYaI8.js` e a cópia de `public/`.

## 6. Publicação atual (Vercel)

| Item | Valor |
|---|---|
| Endereço | `https://cdc-cursos-kappa.vercel.app/` |
| Servidor | `server: Vercel`, região de resposta `iad1` (OBSERVADO) |
| Cache do HTML | `cache-control: public, max-age=0, must-revalidate` (OBSERVADO) |
| HSTS | `strict-transport-security: max-age=63072000; includeSubDomains; preload` (OBSERVADO) |
| Configuração no repositório | **nenhuma** (`vercel.json` ausente). A Vercel detecta o Vite e usa `npm run build` → `dist/` como padrão para projetos Vite (comportamento padrão da plataforma; a configuração real do projeto é NÃO IDENTIFICADO) |
| Domínio próprio | **não configurado** para este site. `cdccursos.com.br` responde com redirecionamento para `www.cdccursos.com.br`, servido pelo **Wix** (site antigo) (OBSERVADO) |
| Integração GitHub → Vercel (publicação automática) | **NÃO IDENTIFICADO** (não há arquivos de CI no repositório; pode estar ligada no painel da Vercel) |

## 7. Serviços externos e integrações

| Serviço | Tipo | Chamada | Precisa de conta ou chave no site? |
|---|---|---|---|
| Google Fonts | CSS e fontes | `<link>` no `<head>` | não |
| WhatsApp | link `wa.me` | `href` montado no cliente | não |
| Kiwify | links de checkout e login | `href` | não (a conta é da CDC na Kiwify) |
| YouTube | `iframe` (`youtube-nocookie.com`) e capas (`i.ytimg.com`) | no clique | não |
| Google Maps | link de busca | `href` | não |
| Instagram, Facebook | links | `href` | não |
| Aplicativo CDC | link para `cdc-capacita-o-em-qualidade.lovable.app` | `href` | não |

O site **não envia dados** a nenhum serviço. A única leitura de rede feita pelo JS é `fetch('materiais/indice.json')` (arquivo do próprio site) e o carregamento dos PDFs (também do próprio site).

## 8. APIs do navegador usadas

WebGL (three.js) · Canvas 2D (brasas, PDF) · Web Audio (`AudioContext`) · `IntersectionObserver` · `ResizeObserver` · `MutationObserver` · `matchMedia` · Pointer Events · Clipboard API (`navigator.clipboard.writeText`, com reserva por seleção) · `localStorage` · History API (`replaceState`, `hashchange`) · `<dialog>` (`showModal`) · `document.fonts` · `requestAnimationFrame`.

## 9. Partes independentes × partes dependentes de serviços

| Parte | Independente? | Depende de |
|---|---|---|
| Layout, conteúdo, estilos, imagens, PDFs, leitor, busca, progresso de leitura | **sim** (tudo no repositório) | nada além de uma hospedagem estática |
| Logo de partículas, abertura, cordão, cursor, animações, brasas, som | **sim** | WebGL e Web Audio do navegador (com reservas) |
| Tipografia | **não** | Google Fonts (reserva: fontes do sistema) |
| Vídeos da área comum | **não** | YouTube |
| Agendamento e pré-inscrição | **não** | WhatsApp |
| Compra e área do curso | **não** | Kiwify |
| Aplicativo | **não** | projeto separado no Lovable |
| Publicação | **não** | uma hospedagem (hoje Vercel) |

## 10. Licenças a observar numa reconstrução ou migração

- **GSAP 3.15.0:** licença padrão "sem custo" da GSAP (inclui SplitText e ScrambleText). Leia os termos em `https://gsap.com/standard-license` antes de reutilizar em outros projetos.
- **three.js, Lenis, Vite:** MIT. **pdf.js:** Apache-2.0. **LightningCSS:** MPL-2.0 (só no *build*).
- **Fontes:** Google Fonts (ver `ASSETS_INVENTORY.md` §5).
- **Conteúdo:** textos, fotos, logotipo e PDFs pertencem à CDC. O IB-024 é um documento da FBTS.

## 11. Teste de reprodução fora da Vercel (feito em 4 nov. 2026)

Para confirmar que o site não depende da plataforma, o *build* foi refeito numa cópia isolada do commit `65c37e7` (`git archive`), fora da Vercel, sem alterar o repositório:

| Etapa | Resultado |
|---|---|
| Ambiente | Linux, Node **22.23.4**, npm **10.9.9** |
| `npm ci` | 24 pacotes instalados em 5 s, sem erro |
| `npm run build` | concluído em 1,31 s: `index.html` 64,95 kB · `index-D7O1k9YW.css` 78,28 kB · `index-DsBXkgpX.js` 758,71 kB · `pdf.min-CFgnYaI8.js` 497,40 kB. Só um aviso informativo do Vite sobre *chunks* acima de 500 kB (não é erro) |
| Comparação com o site publicado | `index.html`, o JS, o CSS e o *chunk* do pdf.js **idênticos byte a byte** · os 38 arquivos de `public/` **idênticos** (SHA-256) |

Conclusão: o site publicado é exatamente o *build* do commit `65c37e7`, e o *build* é **reproduzível e determinístico** fora da Vercel. **OBSERVADO.**

## 12. Requisitos para executar fora da plataforma original

1. Node 22.13+ e npm.
2. `git clone https://github.com/adrianlucaslops123-code/landing-page-cdc.git && cd landing-page-cdc`
3. `npm ci` (instala exatamente as versões do `package-lock.json`).
4. `npm run dev` → `http://localhost:5174`, ou `npm run build` → pasta `dist/` pronta para qualquer hospedagem.
5. Nenhum `.env`, nenhuma chave e nenhum serviço a configurar.

Passo a passo de migração e publicação: `README.md` deste pacote.
