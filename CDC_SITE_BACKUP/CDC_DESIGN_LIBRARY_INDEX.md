# CDC Design Library: índice da biblioteca de experiências digitais

Biblioteca de **componentes, técnicas e comportamentos** extraídos do site da CDC Capacitação em Qualidade (`https://cdc-cursos-kappa.vercel.app/`, código em `github.com/adrianlucaslops123-code/landing-page-cdc`, commit `65c37e7`). Não é uma biblioteca de *templates*. Cada ficha descreve **uma** experiência, com valores técnicos, origem no código, estado real e como reaproveitá-la sozinha, com outra identidade visual.

As fichas ficam em `CDC_DESIGN_LIBRARY/`. Data da análise: 3 nov. 2026.

---

## 1. Como ler as fichas

### 1.1 Grau de confiabilidade de cada valor

| Marca | Significado |
|---|---|
| **EXATO** | lido diretamente no código-fonte (CSS, JS ou HTML) |
| **CALCULADO** | derivado de uma fórmula ou configuração do código (ex.: px por unidade 3D, meia-vida de um decaimento) |
| **OBSERVADO** | medido no site publicado com Chromium headless (Playwright), em 1440×900 e DPR 1, salvo indicação. Também em 1280×720, 1024×768, 768×1024, 2560×1440, iPhone 13 (390×664, DPR 3) e com movimento reduzido. O WebGL do ambiente é por software (SwiftShader), então tempo de quadro e FPS **não** são representativos |
| **ESTIMATIVA** | aproximação que precisa de validação |
| **NÃO IDENTIFICADO** | não foi possível extrair |

### 1.2 Estado de implementação

| Estado | Significado |
|---|---|
| **Implementado e validado** | código lido **e** comportamento confirmado no site publicado |
| **Implementado, parcialmente validado** | código lido. Só parte do comportamento foi observada |
| **Implementado, não validado** | código lido. O comportamento não foi acionado ou medido em execução |
| **Ideia futura** | não existe no site. Aparece só na §5, separada |

"Com divergência" ou "com efeito colateral" indica que o comportamento publicado é diferente do que o código parece pretender. A ficha descreve os dois, e **nada foi corrigido no site**.

### 1.3 Portabilidade

- **Direta**: copiar o trecho e trocar tokens (cores, fontes).
- **Depende de adaptação**: precisa de um recurso próprio do novo projeto (máscara do logotipo, fonte variável com eixo de largura, conteúdo, dados).

---

## 2. Catálogo completo (42 fichas)

| ID | Experiência | Caráter | Estado | Portabilidade | Dependências |
|---|---|---|---|---|---|
| [CUR-01](CDC_DESIGN_LIBRARY/CUR-01_cursor-proprio.md) | Cursor próprio: ponto exato + anel com atraso, estados link e calor | expressivo | validado, com divergência (`is-apertado` sem efeito) | direta | GSAP |
| [CUR-02](CDC_DESIGN_LIBRARY/CUR-02_rotulo-contextual-abrir.md) | Rótulo contextual do cursor: disco laranja "ABRIR", "ENTRAR", "LER", "SOM/MUDO" | expressivo | validado | direta | CUR-01 |
| [ARC-01](CDC_DESIGN_LIBRARY/ARC-01_logo-de-particulas-macarico.md) | Logo de partículas 3D com "maçarico" (aquecimento pelo mouse) | expressivo | validado | depende de adaptação (máscara do logo) | three.js |
| [ARC-02](CDC_DESIGN_LIBRARY/ARC-02_abertura-do-arco-clique.md) | "Abrir o arco": clarão, explosão, tremor, som no clique | expressivo | validado | depende de ARC-01 (o clarão CSS é direto) | three.js, GSAP |
| [ARC-03](CDC_DESIGN_LIBRARY/ARC-03_faiscas-com-gravidade.md) | Faíscas com gravidade, rastro e quique | expressivo | parcialmente validado | direta (three.js) | three.js |
| [ARC-04](CDC_DESIGN_LIBRARY/ARC-04_saida-do-hero-camera-atravessa.md) | Saída do hero: câmera atravessa o logo, texto se desfaz, vinheta | expressivo | validado, com efeito colateral (lema e "Role" somem ao voltar) | direta (sem 3D) | GSAP ScrollTrigger |
| [CAR-01](CDC_DESIGN_LIBRARY/CAR-01_abertura-metal-fundido.md) | Abertura: logo enche de metal fundido, contador, cortina | expressivo | validado, com variação (contador pode parar em 090) | depende de adaptação (máscara) | GSAP |
| [ROL-01](CDC_DESIGN_LIBRARY/ROL-01_cordao-de-solda-progresso.md) | Cordão de solda: progresso da rolagem com ponta incandescente | expressivo | validado | direta | ScrollTrigger (só leitura) |
| [ROL-02](CDC_DESIGN_LIBRARY/ROL-02_rolagem-suave-e-ancoras.md) | Rolagem suave Lenis + âncoras com *ease-in-out quart* de 1,7 s | minimalista | validado | direta | Lenis, GSAP |
| [ROL-03](CDC_DESIGN_LIBRARY/ROL-03_navegacao-inteligente.md) | Barra de vidro que some ao descer, volta ao subir, seção acesa | minimalista | validado | direta | GSAP ScrollTrigger |
| [TIP-01](CDC_DESIGN_LIBRARY/TIP-01_titulos-mascarados-por-linha.md) | Títulos que sobem por linha saindo de máscara | minimalista | validado | direta | GSAP SplitText |
| [TIP-02](CDC_DESIGN_LIBRARY/TIP-02_blocos-que-surgem.md) | Blocos que surgem do desfoque, em lotes | minimalista | validado | direta | GSAP ScrollTrigger |
| [TIP-03](CDC_DESIGN_LIBRARY/TIP-03_manifesto-que-acende.md) | Manifesto que acende palavra por palavra (*scrub*) | expressivo | validado | depende de adaptação (palavras-chave) | GSAP SplitText |
| [TIP-04](CDC_DESIGN_LIBRARY/TIP-04_numeros-que-contam.md) | Números que contam com dígitos embaralhando | minimalista | validado | direta | GSAP |
| [TIP-05](CDC_DESIGN_LIBRARY/TIP-05_letras-embaralhadas.md) | Letras embaralhadas no *hover* e no contador | minimalista | validado | direta | GSAP ScrambleText |
| [TIP-06](CDC_DESIGN_LIBRARY/TIP-06_fecho-tipografico-elastico.md) | Fecho elástico: largura da fonte 62 % → 116 % com a rolagem | expressivo | validado | depende de adaptação (fonte com eixo `wdth`) | GSAP |
| [TIP-07](CDC_DESIGN_LIBRARY/TIP-07_metal-fundido-gradiente.md) | Metal fundido: gradiente que corre no texto e no logo | expressivo | validado | direta | CSS |
| [BOT-01](CDC_DESIGN_LIBRARY/BOT-01_botoes-brasa-e-vidro.md) | Botões brasa (varredura de luz) e vidro, com estados | minimalista | validado | direta | CSS |
| [BOT-02](CDC_DESIGN_LIBRARY/BOT-02_botao-magnetico.md) | Botões magnéticos com soltura elástica | expressivo | validado, com efeito colateral (`.zap` deixa de se esconder) | direta | GSAP |
| [BOT-03](CDC_DESIGN_LIBRARY/BOT-03_onda-no-clique.md) | Onda no clique (*ripple*) | minimalista | não validado | direta | CSS + JS |
| [BOT-04](CDC_DESIGN_LIBRARY/BOT-04_botao-whatsapp-flutuante.md) | Pílula flutuante do WhatsApp que se expande, com anel pulsante | minimalista | validado | direta | CSS |
| [BOT-05](CDC_DESIGN_LIBRARY/BOT-05_botao-de-som.md) | Botão de som com barras que dançam | minimalista | validado (botão) | direta | CSS |
| [BOT-06](CDC_DESIGN_LIBRARY/BOT-06_copiar-e-aviso.md) | Botão "Copiar" + aviso flutuante | minimalista | não validado | direta | Clipboard API |
| [CRT-01](CDC_DESIGN_LIBRARY/CRT-01_cartoes-inclinacao-e-luz.md) | Cartões que inclinam e luz que segue o mouse (e borda que acende) | expressivo | parcialmente validado | direta | GSAP |
| [CEN-01](CDC_DESIGN_LIBRARY/CEN-01_prova-por-prova-cena-presa.md) | Cena presa que troca um módulo por passo de rolagem | expressivo | validado | direta | GSAP ScrollTrigger |
| [CEN-02](CDC_DESIGN_LIBRARY/CEN-02_ilustracoes-svg-animadas.md) | 8 ilustrações técnicas SVG com linha do tempo | expressivo | validado | depende de adaptação (desenhos) | GSAP |
| [CEN-03](CDC_DESIGN_LIBRARY/CEN-03_fita-de-fotos-horizontal.md) | Fita de fotos horizontal com inclinação pela velocidade | expressivo | validado | direta | GSAP ScrollTrigger |
| [CEN-04](CDC_DESIGN_LIBRARY/CEN-04_rota-animada.md) | Rota com tracejado que anda | minimalista | não validado | direta | GSAP |
| [CEN-05](CDC_DESIGN_LIBRARY/CEN-05_depoimentos-carrossel.md) | Carrossel de depoimentos palavra por palavra | minimalista | validado (estado inicial) | direta | GSAP SplitText |
| [CEN-06](CDC_DESIGN_LIBRARY/CEN-06_acordeao-duvidas.md) | Acordeão com altura animada | minimalista | não validado | direta | GSAP |
| [CEN-07](CDC_DESIGN_LIBRARY/CEN-07_menu-celular-cortina.md) | Menu de tela cheia em cortina | minimalista | validado | direta | GSAP |
| [CEN-08](CDC_DESIGN_LIBRARY/CEN-08_pre-inscricao-whatsapp.md) | Pré-inscrição que monta a mensagem do WhatsApp | minimalista | não validado | direta | nenhuma |
| [CEN-09](CDC_DESIGN_LIBRARY/CEN-09_previa-questao-aplicativo.md) | Prévia interativa de questão (janela de app) | expressivo | parcialmente validado | depende de adaptação (conteúdo) | GSAP |
| [CEN-10](CDC_DESIGN_LIBRARY/CEN-10_portal-area-do-aluno.md) | Portal com cortina circular, biblioteca, busca, progresso | expressivo | não validado | depende de adaptação (dados) | GSAP |
| [CEN-11](CDC_DESIGN_LIBRARY/CEN-11_leitor-de-pdf.md) | Leitor de PDF próprio com virtualização | minimalista | não validado | direta | pdf.js |
| [CEN-12](CDC_DESIGN_LIBRARY/CEN-12_videos-capa-para-player.md) | Capa que vira player do YouTube sem cookies | minimalista | não validado | direta | YouTube |
| [CEN-13](CDC_DESIGN_LIBRARY/CEN-13_redes-sociais.md) | Redes: canto, rodapé e pop-up `dialog` | minimalista | validado (canto) | direta | nenhuma |
| [FUN-01](CDC_DESIGN_LIBRARY/FUN-01_grao-de-filme.md) | Grão de filme em SVG animado | expressivo | validado | direta | CSS |
| [FUN-02](CDC_DESIGN_LIBRARY/FUN-02_brasas-subindo-canvas.md) | Brasas subindo em canvas 2D determinístico | expressivo | validado | direta | nenhuma |
| [FUN-03](CDC_DESIGN_LIBRARY/FUN-03_atmosfera-e-sinalizacao-do-hero.md) | Atmosfera do hero, lema, dica, indicador "Role" | minimalista | validado | direta | CSS |
| [FUN-04](CDC_DESIGN_LIBRARY/FUN-04_selo-e-rotulo-de-secao.md) | Selo com ponto pulsante e rótulo de seção com filete | minimalista | validado | direta | CSS |
| [SOM-01](CDC_DESIGN_LIBRARY/SOM-01_som-sintetizado.md) | Som sintetizado (ambiente, arco, cliques) | expressivo | não validado (sem áudio no teste) | direta | Web Audio |

---

## 3. Classificação por estado real

**Implementados e validados (30):** CUR-01\*, CUR-02, ARC-01, ARC-02, ARC-04\*, CAR-01\*, ROL-01, ROL-02, ROL-03, TIP-01, TIP-02, TIP-03, TIP-04, TIP-05, TIP-06, TIP-07, BOT-01, BOT-02\*, BOT-04\*, BOT-05 (botão; o som está em SOM-01), CEN-01, CEN-02, CEN-03, CEN-05 (estado inicial e controles; a troca de 7 s não foi cronometrada), CEN-07, CEN-13 (canto; o pop-up não foi aberto), FUN-01, FUN-02, FUN-03 e FUN-04.
\* com divergência ou efeito colateral documentado.

**Implementados, parcialmente validados (3):** ARC-03, CRT-01, CEN-09.

**Implementados, não validados em execução (9):** BOT-03, BOT-06, CEN-04, CEN-06, CEN-08, CEN-10, CEN-11, CEN-12, SOM-01.

Total: 30 + 3 + 9 = 42 fichas.

**Documentados que dependem de adaptação para reuso (9, classificação independente do estado):** ARC-01, ARC-02, CAR-01, TIP-03, TIP-06, CEN-02, CEN-09, CEN-10 e, pelo conteúdo, CEN-04.

---

## 4. Divergências e efeitos colaterais encontrados (resumo)

| # | Onde | O que acontece no site publicado | Ficha |
|---|---|---|---|
| 1 | Cursor | `is-apertado` deveria encolher o anel para 80 %, mas o GSAP grava `scale: none` inline e nada muda | CUR-01 §10 |
| 2 | Botão flutuante do WhatsApp | depois do primeiro *hover* (magnetismo), o GSAP grava `translate: none` e o botão não se esconde mais no topo | BOT-02 §4 |
| 3 | Hero | depois de descer e voltar ao topo, o lema "Capacitação em qualidade" e o indicador "Role" ficam invisíveis | ARC-04 §6 |
| 4 | Abertura | se o logo de partículas demorar mais de 1 s, o contador sobe a 095, volta para 090 e a cortina sobe em 090 | CAR-01 §5 |
| 5 | Rota (Estrutura) | as animações da rota também rodam no movimento reduzido | CEN-04 §2 |
| 6 | Hero (texto) | o GSAP converte o `translate: 0 −44%` em px no primeiro quadro (−180,07 px em 1440×900) e não recalcula ao redimensionar | ARC-04, OBSERVADO |

Regra geral para qualquer reconstrução: **não misture** as propriedades CSS `translate`/`scale`/`rotate` com animações de `x/y/scale` do GSAP no mesmo elemento (GSAP 3.15).

---

## 5. Ideias futuras (NÃO implementadas no site)

Listadas só para não serem confundidas com recursos existentes:

| Ideia | Origem |
|---|---|
| Cursor com uma "ponta de arco elétrico" desenhada acima da esfera | Descrição recebida no pedido. **Não existe no código** (o cursor é ponto + anel). Seria uma extensão nova de CUR-01 |
| Versão 2D (canvas) das faíscas de ARC-03 | Sugerida em ARC-03 §6 |
| Lupa com ampliação real (escala) na ilustração "Visual e dimensional" | Sugerida em CEN-02 §5 |
| Estado "desativado" para `.botao` | Não existe. Precisaria ser desenhado (sugestão: opacidade 0,45, sem varredura, `cursor: not-allowed`) |
| Fontes servidas pelo próprio site (sem Google Fonts) | Recomendação de portabilidade (`TECHNICAL_DEPENDENCIES.md`) |

---

## 6. Como combinar recursos (receitas)

**Conjunto minimalista** (sóbrio, rápido, funciona sem 3D): ROL-02 + ROL-03 + TIP-01 + TIP-02 + BOT-01 + BOT-04 + CEN-06 + CEN-07 + FUN-04. Opcional: CUR-01 só com repouso e `is-link`.

**Conjunto expressivo** (assinatura CDC): CAR-01 → ARC-01/02/03 → ARC-04 → TIP-03 → CEN-01/02 → CEN-03 → TIP-06 + TIP-07 + FUN-02 → ROL-01 + CUR-01/02 + BOT-02 + CRT-01 + FUN-01 + SOM-01.

**Misturar** é possível: o minimalista como base e 1 ou 2 peças expressivas (ex.: só ROL-01 e CUR-02). Regras de convivência:

1. Lenis (ROL-02) e cenas presas (ARC-04, CEN-01, CEN-03) devem partilhar o mesmo relógio (`gsap.ticker` → `lenis.raf`), como na CDC.
2. Toda peça expressiva precisa de uma saída para `prefers-reduced-motion` (todas as da CDC têm, exceto CEN-04).
3. Cursores e magnetismo só com `(hover: hover) and (pointer: fine)`.
4. Um clarão forte (ARC-02) por cena, no máximo.
5. Mantenha a **ordem de inicialização** da CDC: abertura → rolagem → cenas presas na ordem da página → o resto → `ScrollTrigger.refresh()`.

---

## 7. Mapa para os "12 sistemas" de edição

| Sistema | Fichas da CDC que o compõem |
|---|---|
| 01 Visual Engine | `CDC_DESIGN_SYSTEM.md` (tokens), FUN-01, FUN-03, TIP-07 |
| 02 Motion Engine | tokens de curva (`--entrada`, `--mola`, `--suave`), TIP-01, TIP-02, BOT-02, CRT-01 |
| 03 Transition Engine | CAR-01 (cortina), CEN-01 (troca de prova), CEN-07 (cortina do menu), CEN-10 (cortina circular) |
| 04 Camera Engine | ARC-01 §5 (enquadramento), ARC-04 (*dolly* com a rolagem) |
| 05 Typography Engine | TIP-01 a TIP-07 |
| 06 Lighting Engine | ARC-02 (clarão), CRT-01 (luz que segue o mouse), TIP-07, FUN-03 (vinheta, manchas) |
| 07 Particle Engine | ARC-01, ARC-03, FUN-02 |
| 08 Interaction Engine | CUR-01, CUR-02, BOT-01 a BOT-06, CRT-01, CEN-09 |
| 09 Scroll Engine | ROL-01 a ROL-03, ARC-04, CEN-01, CEN-03, TIP-03, TIP-06 |
| 10 Audio Engine | SOM-01, BOT-05 |
| 11 Rendering Engine | ARC-01 §8 (qualidade adaptativa, DPR ≤ 2, pausa fora da tela), CEN-11 (virtualização) |
| 12 Quality Engine | `CDC_SITE_MASTER_SPECIFICATION.md` §17–18 (critérios e checklist) |
