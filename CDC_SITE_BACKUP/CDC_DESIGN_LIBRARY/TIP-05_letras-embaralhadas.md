# TIP-05 · Letras embaralhadas (links da navegação, rodapé e contador das provas)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** (meio do efeito capturado: "A CDC" → "PHCET") |
| Portabilidade | Direta |
| Onde aparece | (a) `.nav__links a` e `.rodape__links a` no `mouseenter` · (b) contador `.provas__contador b` ao trocar de prova |
| Arquivos de origem | `src/motor/texto.js` (último bloco) · `src/cenas/provas.js` (`mostrar`) |
| Dependências | GSAP 3.15.0 + ScrambleTextPlugin |

## 1. Parâmetros (EXATO)

| Uso | Duração | Caracteres sorteados | `speed` | `revealDelay` | Observação |
|---|---|---|---|---|---|
| Links (nav e rodapé) | 0,55 s | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` | 0,9 | 0,08 s | `overwrite: true`. Toca o som "passe" (se ligado) |
| Contador das provas | 0,5 s | `0123456789` | 1 | n/a | texto final `01` a `08` |

O texto original é lido **uma vez** na inicialização (`const texto = a.textContent`) e o efeito sempre volta a ele.

## 2. Condições

- Só sem toque (`html:not(.toque)`) e com movimento (dentro de `iniciarTexto`, que não roda no movimento reduzido).
- Os links da barra continuam mudando de cor e sublinhado pelo CSS, mesmo sem o embaralhamento.

## 3. Efeito colateral possível (observado uma vez, não reproduzido de forma consistente)

Durante o embaralhamento, a largura do link muda (letras diferentes têm larguras diferentes na fonte proporcional). Num teste, depois do efeito, o cursor estava no estado neutro mesmo com o ponteiro parado sobre o link. Num segundo teste ficou corretamente em `is-link`. Classificação: **OBSERVADO uma vez, não confirmado**.

## 4. Como adaptar

- Troque o alfabeto (`chars`) por símbolos da nova marca (ex.: `'01'` para uma marca de tecnologia).
- Em fontes de largura fixa (mono), o efeito não muda a largura do link.
