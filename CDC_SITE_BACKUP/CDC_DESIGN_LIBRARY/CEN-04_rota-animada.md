# CEN-04 · Rota animada CDC → SENAI → FBTS

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado em execução** (a figura foi vista na captura da seção; a animação do tracejado não foi medida) |
| Portabilidade | Direta (troque nós e textos) |
| Onde aparece | Seção 06 "Estrutura e hospedagem", à direita do texto (`figure.rota`) |
| Arquivos de origem | `index.html` (linhas 472–483) · `src/cenas/estrutura.js` (bloco "rota") · `src/estilo/secoes.css` (`.rota*`) |

## 1. Desenho (EXATO)

- SVG `viewBox 0 0 420 300` num cartão (`padding: 24px`, raio 18, fundo `--aco-1`, contorno `fio`).
- Dois caminhos curvos (`.rota__linha`): `stroke: var(--brasa)`, 2,5 px, pontas redondas, **tracejado `6 9`**.
- Nós: CDC (r 12, laranja com contorno `--brasa-quente` e brilho `drop-shadow(0 0 10px rgba(251,120,30,.8))`), SENAI e FBTS (r 9, fundo `--aco-0`, contorno `--texto` 2 px). Rótulos `700 15px` Archivo 112 %, `letter-spacing .06em`.
- Distâncias em `--brasa-quente`, `500 13px` mono: "1 quarteirão" e "10 min".
- Legenda: "A um quarteirão do SENAI de solda, onde as provas são realizadas, e a 10 minutos da FBTS." (15 px) + "Rua Jorge Rudge, 180 · Maracanã" (12 px mono).

## 2. Animação (EXATO)

Gatilho: topo da figura a 78 % da tela, uma vez.

1. Linhas: de opacidade 0 em 0,8 s, cascata de 0,3 s.
2. Nós e distâncias: de `scale: 0.6` e opacidade 0 para 1, 0,6 s `back.out(2.4)`, cascata de 0,14 s, atraso de 0,2 s.
3. Para sempre: `strokeDashoffset → −60` em 4 s, linear, `repeat: −1`. O tracejado "anda" de CDC para os destinos, como um fluxo.

Movimento reduzido: o bloco de animação ainda é registrado (não está dentro do `if (!reduzido)`), então o tracejado também anda no movimento reduzido. **EXATO** (lido em `iniciarEstrutura`, que é chamada sempre).

## 3. Como adaptar

Troque nós, rótulos e curvas. O tracejado infinito (`dashoffset` negativo e linear) é a técnica que dá a ideia de caminho ativo.
