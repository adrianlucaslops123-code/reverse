# FUN-04 · Selo com ponto pulsante e rótulo de seção com filete de revenimento

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado** |
| Portabilidade | Direta |
| Arquivos de origem | `src/estilo/base.css` (bloco "rótulos e selos") · `src/estilo/aplicativo.css` (`.janela-app__estado i`) |

## 1. Selo `.selo` (EXATO)

- Pílula de 32 px de altura, `padding: 0 14px`, `gap: 10px`, vidro (`--vidro` + `backdrop-filter`), contorno `fio`.
- Texto `500 12px/1` mono, `letter-spacing .08em`, caixa alta, `--texto`.
- Ponto: 7 × 7 px, brasa, brilho `0 0 12px 2px rgba(251,120,30,.7)`, `animation: pulsar 2.4s ease-in-out infinite`. Em 50 % do ciclo: opacidade 0,35 e brilho `0 0 4px 0 rgba(251,120,30,.4)`.
- Mesma pulsação no estado "Modo estudo" da janela do app.
- Movimento reduzido: sem pulsação.

## 2. Rótulo de seção `.rotulo` (EXATO)

- Ex.: "**01** A CDC", "**02** Nossa equipe" … "**10** Aplicativo".
- `display: flex; align-items: center; gap: 12px`. `500 12px/1` mono, `letter-spacing .14em`, caixa alta, `--texto-2`. O número (`span`) em brasa.
- Filete depois do texto (`::after`): 48 × 1 px com o gradiente de revenimento `--revenido` (palha `#d9b46a` → bronze `#a8632e` 30 % → roxo `#6c4f9e` 62 % → azul `#3f72d4`), opacidade 0,8.

## 3. Como adaptar

O filete de 48 px com gradiente é uma assinatura discreta da marca. Troque o gradiente por 3–4 cores da nova identidade.
