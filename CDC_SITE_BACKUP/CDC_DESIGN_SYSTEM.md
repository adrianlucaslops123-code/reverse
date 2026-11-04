# CDC Design System

Sistema visual do site da **CDC Capacitação em Qualidade**, extraído do código publicado (`landing-page-cdc`, commit `65c37e7`, arquivos `src/estilo/*.css`) e conferido no site `https://cdc-cursos-kappa.vercel.app/`.

Legenda de confiabilidade: **EXATO** (código) · **CALCULADO** (fórmula do código) · **OBSERVADO** (medido no site publicado, Chromium) · **ESTIMATIVA** · **NÃO IDENTIFICADO**. Salvo indicação, todos os valores deste documento são **EXATOS**.

> Conceito declarado no próprio código (`tokens.css`): *"Palco escuro de oficina (o brilho do arco só aparece no escuro), coluna de 1240 px, tipografia expandida de chapa industrial, números em mono. Um tema só, de propósito: é o mundo da solda vista pela máscara."*

---

## 1. Princípios da identidade

1. **Um tema só, escuro.** Não há tema claro nem alternância. O fundo é aço quase preto (`#07090c`) e `color-scheme: dark`.
2. **A luz é o material.** Laranja de brasa (cor do logo), dourado da placa e o azul do arco elétrico só aparecem como luz sobre o escuro: brilhos, gradientes e partículas.
3. **Tipografia de chapa industrial.** Archivo expandida (largura 102–125 %) e pesada (600–820) nos títulos. Instrument Sans no texto corrido. IBM Plex Mono em rótulos, números técnicos e metadados, sempre em caixa alta e com espaçamento aberto.
4. **Cores de revenimento** (palha, bronze, roxo, azul: as cores que o aço ganha em volta da solda) como gradiente-assinatura em filetes, sublinhados e no cordão de progresso.
5. **Movimento com física e propósito.** Entradas saem de máscara ou de desfoque. Interações têm inércia, molas e ímã. Tudo tem saída para o movimento reduzido.

---

## 2. Paleta oficial (tokens em `:root`)

### 2.1 Aço (fundos e superfícies)

| Token | HEX / valor | Aplicação | Usos no CSS |
|---|---|---|---|
| `--aco-0` | `#07090c` | fundo da página, `theme-color`, fundo da abertura, núcleos de SVG | 12 |
| `--aco-1` | `#0d1116` | superfície de cartões (plano, recurso, acesso, canal, rota), painel do leitor, opções de selects | 18 |
| `--aco-2` | `#141a21` | superfície elevada: início do gradiente das credenciais, *hover* de itens, fundo da foto enquanto carrega | 5 |
| `--aco-3` | `#1d252e` | **definido e não usado** | 0 |
| `--fio` | `rgba(168,194,222,.12)` | contornos de 1 px (`box-shadow inset`), divisórias | 40 |
| `--fio-forte` | `rgba(168,194,222,.22)` | contornos de campos, botões de vidro, pop-ups | 34 |

### 2.2 Texto

| Token | HEX | Aplicação | Contraste sobre `#07090c` (CALCULADO, WCAG) |
|---|---|---|---|
| `--texto` | `#eef1f4` | títulos, texto forte, ponto do cursor | 17,58:1 |
| `--texto-2` | `#a3adb8` | texto corrido secundário, introduções, legendas | 8,76:1 |
| `--texto-3` | `#6b7682` | metadados, rodapé, placeholders, índice inativo | 4,31:1 (abaixo de 4,5: só para texto auxiliar) |

### 2.3 Marca

| Token | HEX | Aplicação |
|---|---|---|
| `--brasa` | `#fb781e` | laranja do logo: botão principal, números de seção, destaques, cursor em rótulo, setas, contornos de *hover* (77 usos) |
| `--brasa-quente` | `#ffb24a` | brasa clara: ponta do cordão, legendas de status, cotas, texto de tag em destaque (33 usos) |
| `--brasa-escura` | `#c2410c` | início dos gradientes de metal fundido e do líquido da abertura |
| `--brasa-texto` | `#1a0a02` | texto sobre fundo brasa (contraste 7,17:1) |
| `--ouro` | `#c99f53` | dourado da placa: lema do hero, fim do gradiente fundido, chip das credenciais |
| `--arco` | `#a8d8ff` | azul do arco elétrico: anel de foco (`:focus-visible`), foco de campos, estado "Copiado" |

### 2.4 Revenimento

| Token | HEX |
|---|---|
| `--revenido-palha` | `#d9b46a` |
| `--revenido-bronze` | `#a8632e` |
| `--revenido-roxo` | `#6c4f9e` |
| `--revenido-azul` | `#3f72d4` |
| `--revenido` | `linear-gradient(90deg, palha, bronze 30%, roxo 62%, azul)` |

Aplicações: filete de 48 × 1 px do rótulo de seção, sublinhado dos links da barra, marcadores de lista dos recursos (8 × 2 px), faixa colorida do cordão de solda.

### 2.5 Vidro

| Token | Valor | Aplicação |
|---|---|---|
| `--vidro` | `rgba(20,26,33,.62)` | selo, ícones de redes |
| `--vidro-forte` | `rgba(14,18,24,.86)` | formulário, aviso, pop-up de redes |
| `--desfoque` | `blur(18px) saturate(1.25)` | `backdrop-filter` da barra, vidros e botões vidro |

### 2.6 Cores literais (fora dos tokens, usadas no CSS e no JS)

| Valor | Onde |
|---|---|
| `#ff8a36` | *hover* do botão brasa |
| `#fff3d6` | ponto claro do gradiente de metal fundido |
| `#fff4dc` | topo do líquido da abertura |
| `#fff6e0` | ponta do cordão de solda |
| `#fff3dc` | ponto que corre nas ilustrações |
| `#ffd38a` → `#fb781e` → `#b23a0c` | gradiente do logo de partículas e do logo de reserva sem WebGL |
| `#2c3d52` | "aço" das laterais do logo de partículas |
| `#56616d`, `#7d8995` | cordão de solda frio |
| `#0a0d12` | topo do gradiente do hero |
| `#050608` | fundo do rodapé |
| `#121a23` → `#0b0f14` | fundo das figuras das provas |
| `#10141a` → `#0b0e12` | fundo da janela do app |
| `#1f1610`, `#22160d`, `#24170d` | início dos gradientes quentes (plano em destaque, acesso ao curso, "continuar") |
| `#e7c886`, `#8a6a32` | chip dourado das credenciais |
| `#10161d`, `#18202a`, `#3b4652`, `#56636f` | papel, chapa e cordão das ilustrações |
| `#0f3b2c`, `#1d6b4e`, `#0a1f18`, `#6fb898`, `#a9b4bf` | estufa, mostrador e eletrodos das ilustrações |
| `#3fbf86`, `#5fdca4`, `#04140c` | alternativa correta (prévia do app) |
| `#f0584a`, `#ff7b6e`, `#ff8a7e`, `#1a0503` | alternativa errada (prévia do app) |
| `#b9c0c8` | número da página do PDF enquanto não carrega |

---

## 3. Tipografia

### 3.1 Famílias (Google Fonts, `display=swap`)

| Token | Família | Eixos carregados | Reservas | Papel |
|---|---|---|---|---|
| `--display` | **Archivo** | `wdth` 62–125, `wght` 100–900 (variável) | 'Arial Narrow', 'Helvetica Neue', sans-serif | títulos, números, preços, nomes, lema |
| `--ui` | **Instrument Sans** | `wdth` 75–100, `wght` 400–700 (variável) | system-ui, -apple-system, 'Segoe UI', sans-serif | texto corrido, botões, links, campos |
| `--mono` | **IBM Plex Mono** | 400, 500 | ui-monospace, 'SFMono-Regular', Menlo, monospace | rótulos, metadados, contadores, legendas técnicas |

URL exata: `https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wdth,wght@75..100,400..700&display=swap`. Fontes carregadas no site publicado: Archivo 100–900 / 62–125 %, IBM Plex Mono 400 e 500, Instrument Sans 400–700 / 75–100 %. **OBSERVADO.**

Corpo: `font-family: var(--ui); font-size: 17px; line-height: 1.55; -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility`.

### 3.2 Tokens de escala

| Token | Valor | Uso real |
|---|---|---|
| `--t-mega` | `clamp(52px, 10.4vw, 176px)` | **definido e não usado** (o fecho usa `--fecho`, medido em JS) |
| `--t-h2` | `clamp(38px, 5.8vw, 96px)` | `.titulo` |
| `--t-h2-menor` | `clamp(32px, 4.2vw, 68px)` | `.titulo--menor` |
| `--t-h3` | `clamp(21px, 1.8vw, 28px)` | títulos de cartão, formulário, pop-up |
| `--t-corpo` | `17px` | corpo |
| `--t-pequeno` | `14px` | legendas, aviso, condições de pagamento |
| `--t-mono` | `12px` | rótulos mono |

### 3.3 Hierarquia completa (peso · tamanho/altura de linha · largura · espaçamento)

| Estilo | Família | Peso | Tamanho / linha | `font-stretch` | `letter-spacing` | Outros |
|---|---|---|---|---|---|---|
| Fecho do contato (h2) | Archivo | 820 | `var(--fecho)` (medido: 115,17 px em telas ≥ 1 400 px) / 0,9 | 116 % (anima de 62 %) | −0,035 em | caixa alta |
| Hero h1 | Archivo | 780 | `clamp(34px, 4.4vw, 70px)` / 0,98 | 108 % | −0,025 em | `text-wrap: balance`, sombra `0 2px 30px rgba(0,0,0,.6)` |
| Título de seção `.titulo` | Archivo | 760 | `clamp(38px, 5.8vw, 96px)` / 0,96 | 110 % | −0,028 em | `max-width: 18ch`, `margin-top: 26px`, `balance` |
| `.titulo--menor` | Archivo | 760 | `clamp(32px, 4.2vw, 68px)` / 0,96 | 110 % | −0,028 em | `max-width: 20ch` |
| Título da biblioteca | Archivo | 760 | `clamp(34px, 5vw, 72px)` / 0,96 | 110 % | −0,028 em | |
| Manifesto | Archivo | 640 | `clamp(30px, 4.4vw, 70px)` / 1,06 | 104 % | −0,022 em | `max-width: 26ch`, `pretty` |
| Número grande | Archivo | 800 | `clamp(48px, 6vw, 96px)` / 0,9 | 112 % | −0,03 em | `tabular-nums` |
| Preço do plano | Archivo | 800 | `clamp(54px, 5.4vw, 84px)` / 0,9 | 112 % | −0,03 em | "R$" a 0,3 em, 600, brasa |
| Preço em lista | Archivo | 760 | 26 px / 1 | 108 % | n/a | `tabular-nums` |
| Título de prova | Archivo | 760 | `clamp(34px, 3.8vw, 60px)` / 0,98 | 112 % | −0,025 em | |
| Dado de prova (95 %) | Archivo | 800 | `clamp(44px, 4.6vw, 72px)` / 0,9 | 112 % | −0,03 em | brasa |
| Contador das provas | Archivo | 800 | `clamp(40px, 4vw, 64px)` / 0,8 | 112 % | n/a | |
| Citação de depoimento | Archivo | 600 | `clamp(28px, 3.8vw, 60px)` / 1,1 | 102 % | −0,02 em | `max-width: 30ch` |
| Nome em credencial | Archivo | 760 | `clamp(30px, 3.2vw, 48px)` / 1 | 112 % | −0,02 em | |
| Título de acesso | Archivo | 760 | `clamp(26px, 2.6vw, 38px)` / 1 | 110 % | −0,015 em | |
| Link do menu (celular) | Archivo | 750 | `clamp(30px, 9vw, 52px)` / 1,05 | 112 % | −0,02 em | |
| Título de cartão (`--t-h3`) | Archivo | 720 | `clamp(21px, 1.8vw, 28px)` / 1,1 | 106 % | −0,01 em | |
| Pergunta (summary) | Archivo | 640 | `clamp(18px, 1.5vw, 22px)` / 1,3 | 104 % | n/a | |
| Valor de contato | Archivo | 650 | `clamp(18px, 1.6vw, 24px)` / 1,3 | 104 % | n/a | `overflow-wrap: anywhere` |
| Lema do hero | Archivo | 600 | `clamp(11px, 1vw, 14px)` / 1 | 125 % | 0,42 em | caixa alta, ouro |
| Corpo | Instrument Sans | 400 | 17 px / 1,55 | n/a | n/a | |
| Introdução de seção | Instrument Sans | 400 | `clamp(16px, 1.2vw, 19px)` | n/a | n/a | `--texto-2`, `max-width: 58ch`, `margin-top: 24px` |
| Texto do hero | Instrument Sans | 400 | `clamp(15px, 1.15vw, 18px)` | n/a | n/a | `max-width: 52ch` |
| Botão | Instrument Sans | 600 | 15 px / 1,1 (16 px grande, 14 px barra) | n/a | −0,005 em | |
| Link da barra | Instrument Sans | 500 | 14 px / 1 | n/a | n/a | |
| Enunciado (app) | Instrument Sans | 600 | `clamp(17px, 1.3vw, 20px)` / 1,45 | n/a | −0,005 em | |
| Rótulo de seção | IBM Plex Mono | 500 | 12 px / 1 | n/a | 0,14 em | caixa alta |
| Selo | IBM Plex Mono | 500 | 12 px / 1 | n/a | 0,08 em | caixa alta |
| Tag de plano | IBM Plex Mono | 500 | 11 px / 1 | n/a | 0,1 em | caixa alta |
| Rótulo do cursor | IBM Plex Mono | 500 | 10 px / 1 | n/a | 0,1 em | caixa alta |
| Indicador "Role" | IBM Plex Mono | 500 | 10 px / 1 | n/a | 0,2 em | caixa alta |
| Número do cordão | IBM Plex Mono | 500 | 11 px / 1 | n/a | 0,08 em | `tabular-nums` |
| Rodapé legal | IBM Plex Mono | 500 | 12 px / 1,5 | n/a | n/a | `--texto-3` |

### 3.4 Escala calculada por largura de tela (px, CALCULADO a partir dos `clamp`)

| Estilo | 390 | 768 | 1024 | 1280 | 1440 | 1920 | 2560 |
|---|---|---|---|---|---|---|---|
| h1 hero | 34 | 34 | 45,1 | 56,3 | 63,4 | 70 | 70 |
| `.titulo` | 38 | 44,5 | 59,4 | 74,2 | 83,5 | 96 | 96 |
| `.titulo--menor` | 32 | 32,3 | 43 | 53,8 | 60,5 | 68 | 68 |
| manifesto | 30 | 33,8 | 45,1 | 56,3 | 63,4 | 70 | 70 |
| número grande | 48 | 48 | 61,4 | 76,8 | 86,4 | 96 | 96 |
| preço do plano | 54 | 54 | 55,3 | 69,1 | 77,8 | 84 | 84 |
| título de prova | 34 | 34 | 38,9 | 48,6 | 54,7 | 60 | 60 |
| citação | 28 | 29,2 | 38,9 | 48,6 | 54,7 | 60 | 60 |
| `--t-h3` | 21 | 21 | 21 | 23 | 25,9 | 28 | 28 |
| introdução | 16 | 16 | 16 | 16 | 17,3 | 19 | 19 |
| texto do hero | 15 | 15 | 15 | 15 | 16,6 | 18 | 18 |
| link do menu | 35,1 | 52 | 52 | 52 | 52 | 52 | 52 |

Conferências OBSERVADAS: `.titulo` = 44,544 px (768), 59,392 (1024), 74,24 (1280), 96 (2560); h1 = 34 (390 e 768), 45,056 (1024), 56,32 (1280), 70 (2560).

---

## 4. Espaço, grade e proporções

| Token / regra | Valor | Em 390 · 1024 · 1440 (CALCULADO) |
|---|---|---|
| `--gutter` | `max(16px, min(5vw, 64px))` | 19,5 · 51,2 · 64 px |
| `--largura` (coluna) | 1240 px | `.secao__miolo { max-width: calc(1240px + 2 × gutter) }`, centrada, com *padding* lateral igual ao *gutter* (e *safe-area*) |
| Seção | `padding-block: clamp(96px, 15vh, 180px)` | 99,6 px (altura 664) · 135 px (900) · 180 px (≥ 1 200) |
| Contato | `padding-block: clamp(110px, 18vh, 220px) clamp(80px, 12vh, 140px)` | |
| Barra de navegação | largura `min(100% − 2·gutter, 1320px)`, altura 60 px, topo 12 px | 351 · 921,6 · 1 312 px |
| Biblioteca | `max-width: calc(1180px + 2·gutter)` | |
| Espaços recorrentes | 10, 12, 14, 16, 18, 24, 26, 28, 34 px; `margin-top` de grades `clamp(48px, 8vh, 88px)`; separação entre blocos `clamp(32px, 6vw, 96px)` | |
| Larguras de leitura | 18–20ch (títulos), 26ch (manifesto), 30ch (citação), 52–62ch (textos) | |

---

## 5. Forma: raios, bordas e sombras

### 5.1 Raios

| Token | Valor | Uso |
|---|---|---|
| `--r-pilula` | 999 px | selo, tags, WhatsApp, contagens |
| `--r-cartao` | 18 px | todos os cartões, figuras, formulário, pop-up, janela do app |
| `--r-botao` | 12 px | botões, campos, aviso, alternativas |
| `--r-peca` | 10 px | registros das credenciais, fotos da fita |
| Literais | 16 px (barra), 9 px (letra da alternativa), 8 px (copiar), 6 px (chip, cordão, capas), 2 px (página do PDF) | |

### 5.2 Bordas

Nenhum componente usa `border` para contorno. O padrão é **`box-shadow: inset 0 0 0 1px <cor>`** com `--fio` (12 %) ou `--fio-forte` (22 %). Divisórias de 1 px com `--fio`. Estados de destaque trocam a cor do contorno: brasa a 35–55 % ou arco a 45 %.

### 5.3 Sombras (profundidade)

| Nível | Valor | Onde |
|---|---|---|
| Brilho de ação | `0 10px 30px -12px rgba(251,120,30,.7)` | botão brasa |
| Brilho de ação flutuante | `0 14px 34px -12px rgba(251,120,30,.8)` | WhatsApp |
| Cartão | `0 30px 60px -40px #000` | credencial |
| Cartão elevado | `0 40px 80px -50px #000` | figuras das provas |
| Destaque quente | `0 40px 80px -50px rgba(251,120,30,.6)` | plano em destaque |
| Vidro flutuante | `0 40px 90px -50px #000` (formulário) · `0 40px 90px -30px #000` (pop-up) · `0 20px 50px -20px #000` (aviso) | |
| Janela do app | `0 60px 110px -60px #000, 0 40px 90px -70px rgba(251,120,30,.55)` | |
| Barra sólida | `0 18px 40px -24px #000` | navegação depois de 40 px de rolagem |
| Foto | `0 30px 60px -36px #000` | fita de fotos |

Regra: sombras **longas e com *spread* negativo**, que escurecem embaixo sem halo cinza nas laterais.

---

## 6. Gradientes e efeitos

| Nome | Receita | Ficha |
|---|---|---|
| Metal fundido | `linear-gradient(100deg, #c2410c, #fb781e 30%, #ffb24a 46%, #fff3d6 50%, #ffb24a 54%, #fb781e 70%, #c99f53)`, 220 %, 7 s | TIP-07 |
| Revenimento | `--revenido` | §2.4 |
| Atmosfera do hero | radiais azul `rgba(63,114,212,.13)` e brasa `rgba(251,120,30,.12)` + `#0a0d12 → #07090c` | FUN-03 |
| Vinheta | radial dirigida por `--vinheta` | ARC-04 |
| Clarão do arco | radial `rgba(214,236,255,.85) → rgba(120,180,255,.25) 40% → transparente 72%`, `screen` | ARC-02 |
| Luz que segue o mouse | radiais de 240–440 px em `--mx/--my` | CRT-01 |
| Gradação de foto | `grayscale(.35) contrast(1.08) saturate(.9) brightness(.92)` + `soft-light` azul → laranja | CEN-03 |
| Grão de filme | `feTurbulence` a 7 % | FUN-01 |

---

## 7. Componentes

| Componente | Especificação | Ficha |
|---|---|---|
| Botão brasa / vidro / grande | §8 | BOT-01 |
| Selo / rótulo de seção | pílula de vidro com ponto pulsante · mono com número em brasa e filete | FUN-04 |
| Cartão credencial | gradiente 150° aço-2 → aço-1, chip dourado, registros em pílulas, luz holográfica, inclinação | CRT-01 |
| Cartão de plano | aço-1. Destaque quente com tag brasa. Preço gigante. Lista com visto em L de 10 × 5 px (bordas de 1,5 px giradas −45°) | CRT-01 |
| Cartão de recurso | aço-1, ícone de traço de 44 px, borda que acende | CRT-01 |
| Cartão de acesso | altura mínima de 200 px, tipo mono, título grande, seta | CUR-02 / CRT-01 |
| Estante de material | grade `56px 1fr auto`, capa 3:4, barra de lido de 3 px | CEN-10 |
| Figura de prova | moldura com marcas de canto de visor | CEN-02 |
| Formulário de vidro | campos de 50 px, foco em azul do arco, erro com tremor | CEN-08 |
| Canal de contato | cartão aço-1, tipo mono, valor em Archivo, botão copiar | BOT-06 |
| Acordeão | divisórias de 1 px, ícone + / − em brasa | CEN-06 |
| Janela de app | barra com logo e estado, alternativas de 54 px | CEN-09 |
| Pop-up | `dialog` de vidro, 380 px | CEN-13 |
| Aviso | vidro forte, embaixo no centro | BOT-06 |

### 7.1 Cabeçalho (barra de navegação)

Pílula de vidro flutuante, 60 px, raio 16, centrada, 12 px do topo. Logo em máscara (70 px). Seis links com sublinhado de revenimento. Botões à direita. Some ao descer e volta ao subir. Ficha ROL-03.

### 7.2 Rodapé

- `padding: clamp(56px, 9vh, 96px) gutter calc(28px + safe-area)`, fundo `#050608`, `border-top: 1px solid var(--fio)`.
- Logo grande de **metal fundido**: `width: min(64vw, 620px)`.
- Grade de 3 colunas (`1fr 1.2fr 1fr`, `gap: 28px`, 15 px, `--texto-2`; 1 coluna em ≤ 860 px): nome "CDC Capacitação em Qualidade" + "Deiwson Ribeiro ME · desde 2005" · links das seções (*hover* brasa, letras embaralhadas) · telefones e endereço · linha de redes sociais (coluna 3).
- Linha final: "© 2026 CDC Capacitação em Qualidade. Todos os direitos reservados." (mono 12 px, `--texto-3`, `border-top`, `margin-top: 48px`) e crédito "Site desenvolvido por Adrian Lucas Lopes Maximiano." (mono 11 px).

---

## 8. Estados de interação

| Estado | Regra geral | Exemplos |
|---|---|---|
| **Hover** | só sem toque (`:where(html:not(.toque))`). Transições de 0,2–0,4 s. Mudança de fundo e contorno para brasa ou arco | botão brasa → `#ff8a36` + varredura · vidro → contorno azul do arco · cartões → luz e borda · setas andam 4–6 px com a mola |
| **Focus** | `:focus-visible { outline: 2px solid var(--arco); outline-offset: 3px; border-radius: 6px }`. Campos: contorno arco + halo `0 0 0 4px rgba(168,216,255,.14)` | todos os focáveis |
| **Active (pressionado)** | sem `:active` nos `.botao`: o retorno é a **onda** (BOT-03). Alternativas do app: `translate 2px 0` e fundo mais quente | BOT-03, CEN-09 |
| **Pressionado (toggle)** | `aria-pressed="true"`: fundo `rgba(251,120,30,.16)`, contorno `rgba(251,120,30,.55)`, texto brasa quente | barra do leitor, botão de som (barras dançam) |
| **Selecionado** | `aria-selected="true"`: texto `--texto` + sublinhado brasa de 2 px que cresce (`scale 0 → 1`, 0,45 s) | abas da biblioteca |
| **Atual** | `.is-aqui` (link da seção), `.is-ativa` (prova, depoimento), `.is-atual` (miniatura, achado) | |
| **Erro** | contorno brasa + halo brasa + tremor de 0,42 s | pré-inscrição |
| **Sucesso** | verde `#3fbf86` / `#5fdca4` só na prévia do app. "Copiado" em azul do arco | CEN-09, BOT-06 |
| **Desativado** | **não existe estilo de desativado** para botões. Só a prévia do app usa `aria-disabled` + opacidade 0,42 nas alternativas não escolhidas | CEN-09 |

---

## 9. Ícones e elementos gráficos

- **Ícones**: SVG inline de traço (`fill: none; stroke: currentColor` ou brasa, 1,6 px, pontas e junções redondas), `viewBox` 24 ou 48. Tamanhos: 18 px (redes), 20 px (em botões), 24 px (WhatsApp), 44 px (recursos), 52 px (estado vazio). Não há biblioteca de ícones: são todos desenhados no próprio HTML ou JS.
- **Logo**: sempre aplicado como **máscara** de `public/marca/cdc-mascara.png` (1400 × 717), pintado com `background`. Isso permite qualquer cor ou gradiente.
- **Setas tipográficas**: → ↗ ← ‹ › × (texto, não ícone).
- **Ilustrações técnicas**: SVG inline das provas (CEN-02).
- **Marcadores**: visto em L (planos), traço de revenimento (recursos), brasa redonda com brilho (itens da estrutura).

---

## 10. Imagens

- Formato **WebP**. Altura fixa na fita (`clamp(300px, 54vh, 520px)`) e largura pela proporção real (`aspect-ratio` = largura/altura da foto).
- Tratamento uniforme: leve dessaturação, mais contraste, um pouco mais escuro, e gradação azul nas sombras e laranja nas luzes (`soft-light`).
- Raio de 10 px. Sombra longa. Contorno interno de 1 px branco a 6 %.
- Capas dos PDFs: fundo branco, `object-fit: cover; object-position: top`, proporção 3:4.
- Não há fotos de banco de imagens. Só fotos reais do CT (o README registra que as fotos de banco do modelo Wix antigo não foram usadas).

---

## 11. Motion design

### 11.1 Tokens de curva

| Token | Curva | Uso |
|---|---|---|
| `--entrada` | `cubic-bezier(0.16, 1, 0.3, 1)` (≈ *expo-out*) | crescimento do cursor, sublinhados, onda, WhatsApp, redes, abas (19 usos) |
| `--mola` | `cubic-bezier(0.34, 1.4, 0.64, 1)` (com *overshoot*) | setas, aviso, WhatsApp aparecendo, ícone do acordeão, *play* (7 usos) |
| `--suave` | `cubic-bezier(0.65, 0, 0.35, 1)` | indicador "Role" (1 uso) |
| `--saida` | `cubic-bezier(0.55, 0, 0.75, 0.2)` | **definido e não usado** |

### 11.2 Curvas do GSAP usadas

`expo.out` (entradas de texto e blocos) · `expo.inOut` (cortinas e revelações) · `power2.in` (saídas) · `power2.out`/`power3.out` (seguimento do mouse) · `power2.inOut` (traços e animações de ilustração) · `elastic.out(1, 0.4)` (soltura magnética) · `elastic.out(1.2, 0.25)` (tremor do arco) · `back.out(2–3)` (carimbos e nós) · `none` (*scrub*).

### 11.3 Tabela de durações (EXATO)

| Faixa | Valores | Onde |
|---|---|---|
| Instantâneo | 0,12 s (tremulação da ponta), 0,2 s (rótulo do cursor, copiar) | |
| Microinteração | 0,25–0,45 s | *hover* de botões (0,25), cursor (0,35), barra escondendo (0,45), acordeão fechando (0,45), magnetismo (0,5), letras embaralhadas (0,55) |
| Transição | 0,6–1,15 s | cursor anel (0,38), soltura magnética (0,9), blocos (1,05), títulos (1,15), cortina do portal (0,9 / 0,6), cortina da abertura (1,0), barra voltando (0,7) |
| Navegação | 1,7 s | rolagem até âncora (*ease-in-out quart*) |
| Ambiente | 2–7 s | contagem dos números (2), "Role" (2), ponto pulsante (2,4), anel do WhatsApp (2,6), rota (4), metal fundido (7), troca de depoimento (7) |

### 11.4 Padrões de movimento

1. **Entrada**: de baixo (22–40 px) com desfoque (6–10 px) e opacidade 0, `expo.out`, em cascata de 25–100 ms.
2. **Saída**: para cima, rápida (0,3 s), `power2.in`.
3. **Revelação**: `clip-path: inset(...)` ou `circle(...)` com `expo.inOut`.
4. **Seguimento**: `quickTo` com 0,38–0,6 s.
5. **Física**: molas pouco amortecidas (ζ 0,18–0,64) e gravidade nas partículas.
6. ***Scrub***: suavização 0,6–0,8 s nas cenas ligadas à rolagem.

### 11.5 Movimento reduzido (`prefers-reduced-motion: reduce`)

Sem abertura, sem cursor próprio, sem Lenis, sem cenas presas (altura da página 17 445 px em vez de 22 456 px, OBSERVADO), sem física nas partículas, sem entradas de texto, sem grão animado, sem pulsações nem anéis, sem tremulação do cordão. As fitas e provas viram listas. **Exceção:** a rota da seção Estrutura continua animada (CEN-04).

---

## 12. Responsividade

### 12.1 Pontos de quebra (todos `max-width`, EXATOS)

| Largura | Mudanças principais |
|---|---|
| ≤ 1080 px | some a lista de links da barra, aparece o botão de menu. Planos em 2 colunas (destaque na largura toda) |
| ≤ 1000 px | estante em 1 coluna |
| ≤ 960 px | aplicativo em 1 coluna |
| ≤ 900 px | números em 2 × 2, recursos, estrutura, dúvidas, provas e contato em 1 coluna. Provas em lista (via JS) |
| ≤ 899 px **ou** proporção < 11/10 | texto do hero desce para baixo do logo. Lema some. Leitor com painel em gaveta |
| ≤ 860 px | dica do hero some, botões do hero na largura toda, acessos em 1 coluna, rodapé em 1 coluna |
| ≤ 860 px **e** altura ≤ 700 px | parágrafo do hero some |
| ≤ 760 px | cordão some, credenciais em 1 coluna, fita de fotos vira rolagem horizontal com encaixe, WhatsApp e redes menores. Logo de partículas com densidade de celular (também em `hover: none`) |
| ≤ 680 px | planos em 1 coluna |
| ≤ 640 px | biblioteca compacta (sem resumo) |
| ≤ 560 px | barra de 56 px, sem "Área do aluno", logo de 60 px. Busca da seção em coluna |
| ≤ 520 px | leitor sem nome do documento |
| ≤ 480 px | alternativas do app menores |
| ≤ 380 px | some o botão de som |
| altura ≤ 760 px (provas presas) | títulos das provas menores |
| altura < 620 px | provas em lista |

### 12.2 Por tipo de aparelho (OBSERVADO)

| Aparelho | Comportamento |
|---|---|
| Celular (iPhone 13, 390×664, DPR 3) | toque (`html.toque`), sem Lenis, sem cursor, sem cordão, hero preso por 1 tela, provas em lista, fita com rolagem nativa, canvas a DPR 2 (780 × 1328), fecho em 32,6 px |
| Tablet em pé (768×1024, toque) | menu, provas em lista, hero e fita presos |
| Tablet deitado (1024×768, toque) | menu, **provas presas**, hero e fita presos |
| Notebook (1280×720) | tudo ativo, cursor próprio, Lenis, fecho em 106,99 px |
| Monitor grande (2560×1440) | tipos no máximo dos `clamp`, coluna de 1 240 px centrada, fecho em 115,17 px, cordão de 490 px |

---

## 13. Camadas (`z-index`, EXATO)

| Valor | Elemento |
|---|---|
| 100 | link "Pular para os treinamentos" |
| 99 | abertura (`.carga`) |
| 96 | aviso |
| 95 | cursor |
| 90 | grão de filme |
| 80 | portal da área do aluno |
| 50 | barra de navegação |
| 45 | menu do celular |
| 44 | WhatsApp, redes do canto |
| 40 | cordão de solda |
| 1–4 | camadas internas (hero, leitor) |

---

## 14. Regras para criar novos componentes "no padrão CDC"

1. Superfície `--aco-1` com contorno `inset 1px var(--fio)`, raio 18 px, *padding* `clamp(24px, 2.4–3vw, 34–40px)`.
2. Título em Archivo 700–780 com `font-stretch` 104–112 % e espaçamento negativo. Rótulo em mono 11–12 px, caixa alta, 0,1–0,14 em.
3. Destaque sempre em `--brasa`. Foco sempre em `--arco`.
4. *Hover* com luz (radial que segue o mouse ou mudança de contorno), nunca com mudança brusca de tamanho.
5. Entrada com `data-surgir`. Títulos com `data-titulo`.
6. Prever o estado de toque (`html.toque`) e o movimento reduzido.
7. Não criar tema claro.
