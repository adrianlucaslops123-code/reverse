# SOM-01 · Som da página sintetizado na hora (Web Audio, nenhum arquivo de áudio)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, não validado por audição** (o ambiente de verificação não tem saída de áudio. Todos os valores abaixo são EXATOS do código) |
| Portabilidade | Direta. Módulo isolado |
| Arquivos de origem | `src/motor/som.js` |
| Dependências | Web Audio API (`AudioContext`, com reserva `webkitAudioContext`) |

## 1. Cadeia de saída

`mestre` (ganho 0,7) → `DynamicsCompressor` (limiar −16 dB, razão 4) → saída. Um único *buffer* de **2 s de ruído branco** é reaproveitado por todos os efeitos (começando em posição aleatória).

Envelope padrão: `0,0001 → pico` (exponencial, tempo de ataque) `→ 0,0001` (exponencial, tempo de queda).

## 2. Efeitos (EXATO)

| Nome | Quando toca | Receita |
|---|---|---|
| `ambiente` | enquanto o som está ligado | zumbido de máquina de solda: seno de **60 Hz** + triângulo de **120,4 Hz** (ganho 0,35) + ruído (ganho 0,25), por um passa-baixa de **220 Hz** (Q 3). Ganho geral sobe de 0,0001 a **0,05** em 1,2 s. **O filtro abre com a velocidade da rolagem**: alvo `220 + min(1, v/3000) × 1600` Hz (até 1 820 Hz), constante de tempo de 0,12 s. Ao desligar, cai a 0,0001 em 0,5 s |
| `arco` | clique que abre o arco e arco de abertura | (1) estalo: ruído por passa-alta de **1 800 Hz** com **14 degraus** de ganho aleatório (0,05–0,19) a cada **30 ms**, caindo até 0,62 s · (2) zumbido: dente-de-serra de **118 Hz** por passa-baixa de 900 Hz, pico 0,05, ataque 10 ms, queda 0,45 s · (3) pancada grave: seno de **90 → 38 Hz** em 0,35 s, pico 0,32, ataque 6 ms, queda 0,4 s |
| `clique` | âncoras, ondas de botão, prévia do app, inscrição | triângulo de **1 500 → 650 Hz** em 50 ms, pico 0,07, ataque 4 ms, queda 60 ms |
| `passe` | entrar num botão magnético, *hover* dos links da barra, troca de depoimento, zoom do leitor | seno de **2 600 Hz**, pico 0,022, ataque 3 ms, queda 30 ms. **No máximo 1 a cada 60 ms** |
| `virada` | troca de prova, metade da saída do hero, abertura do portal | ruído por passa-faixa (Q 1,2) de **380 → 2 400 Hz** em 0,42 s, pico 0,09, ataque 0,12 s, queda 0,4 s |

## 3. Regras

- Começa desligado. Só liga com o botão da barra (BOT-05), que é um gesto da pessoa, como os navegadores exigem.
- Lembra a escolha (`localStorage['cdc-som']`) e religa no primeiro gesto da visita seguinte.
- `tocar(nome)` não faz nada com o som desligado.

## 4. Como adaptar

- Para outra marca, troque as frequências do ambiente (60/120 Hz é a rede elétrica e combina com solda). Para uma marca de natureza: ruído por passa-banda a ~800 Hz, sem osciladores.
- Mantenha os picos baixos (≤ 0,1 nos efeitos de interface) e o compressor no fim da cadeia.
