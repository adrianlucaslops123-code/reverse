# ARC-04 · Saída do hero: a câmera atravessa o logo e o texto se desfaz

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** (Chromium 1440×900) · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado e validado**, com **um efeito colateral observado** (§6) |
| Portabilidade | O padrão "seção presa + linha do tempo com *scrub*" é direto. A parte 3D depende de ARC-01 |
| Arquivos de origem | `src/cenas/hero.js` (`saidaHero`) · `src/fogo/particulas.js` (`saida(p)` e o fim de `passo`) · `src/estilo/topo.css` (`.hero::after`, variável `--vinheta`) · `src/main.js` |
| Dependências | GSAP 3.15.0 + ScrollTrigger, three.js |

## 1. O que é

O hero fica **preso na tela por uma altura de janela** enquanto a rolagem dirige uma linha do tempo:

- a câmera faz um *dolly* até o logo e entra nele. Os pontos se abrem em brasas e passam pela lente;
- o logo gira 0,2 rad em z;
- o texto sobe 50 px, desfoca e some;
- a vinheta escurece as bordas;
- na metade, toca o som "virada" (se ligado).

## 2. Configuração do ScrollTrigger (EXATO)

```js
gsap.timeline({ scrollTrigger: {
  trigger: hero, start: 'top top', end: () => `+=${innerHeight}`,
  pin: true, scrub: true, anticipatePin: 1,
  onUpdate(self) {
    logo.saida(self.progress)
    if (self.progress > 0.5 && !virou) { virou = true; som.tocar('virada') }
    else if (self.progress < 0.3) virou = false
  },
}})
.to('.hero__conteudo, .hero__lema, .hero__dica, .hero__rolar',
    { opacity: 0, y: -50, filter: 'blur(10px)', ease: 'power1.in', duration: 0.5, stagger: 0.02 }, 0)
.to(hero, { '--vinheta': 1, duration: 1 }, 0)
```

- Comprimento da trava: **1 altura de janela**. O espaçador fica com 2× a altura (1 800 px em 900 px de altura; 2 880 px em 1 440 px). **OBSERVADO.**
- `scrub: true`: a linha do tempo segue a rolagem sem atraso próprio. A suavidade vem do Lenis (ROL-02).
- O texto termina de sumir na **metade** da trava (duração 0,5 numa linha de 1). A vinheta cresce por toda a trava.
- No celular e no tablet a trava **também existe**: só o movimento reduzido desliga. **OBSERVADO** (iPhone 13: espaçador de 1 328 px para 664 px de altura).

## 3. Câmera e partículas, em função de `s` (0 a 1)

| Grandeza | Fórmula | Em s = 0,5 | Em s = 1 | Confiab. |
|---|---|---|---|---|
| Suavização | `e = s²(3 − 2s)` (*smoothstep*) | 0,5 | 1 | EXATO |
| Posição da câmera | `(grupo.x·e, grupo.y·e − 0,6·e, distância·(1 − 0,88·e))` | metade do caminho, 56 % da distância | centrada no logo, 12 % da distância original, 0,6 un. abaixo | EXATO |
| Abertura em brasas | `abre = s^1,5 × 15` un. ao longo de `dir` (cada ponto tem direção lateral de raio 0,4–1,0 e z de +0,3 a +1,5, isto é, vem para a câmera) | 5,3 un. | 15 un. | EXATO, CALCULADO |
| Calor mínimo (brasa) | `calorVis = max(calor, s × 0,5)` | 0,25 | 0,5 (laranja-amarelo) | EXATO |
| Giro z | `s × 0,2` rad | 5,7° | 11,5° | EXATO, CALCULADO |
| Inclinação pelo mouse | multiplicada por `(1 − s)` | metade | zero | EXATO |
| Sumiço | `uSome = clamp((s − 0,55)/0,45)^1,4` | 0 | 1 | EXATO |
| Física do mouse | desligada quando `s ≥ 0,2` | n/a | n/a | EXATO |
| Laço de render | para de desenhar com `s ≥ 0,999` | n/a | parado | EXATO |

## 4. Vinheta (CSS, EXATO)

```css
.hero::after {
  content: ''; position: absolute; inset: 0; pointer-events: none; z-index: 1;
  background: radial-gradient(ellipse 80% 70% at 50% 42%,
    transparent calc(52% - var(--vinheta, 0) * 30%),
    rgba(0, 0, 0, calc(0.62 + var(--vinheta, 0) * 0.38)));
}
```

Com `--vinheta` 0: centro limpo até 52 % e bordas a 62 % de preto. Com `--vinheta` 1: centro limpo só até 22 % e bordas pretas a 100 %.

## 5. Movimento reduzido

Sem trava e sem linha do tempo: um ScrollTrigger simples (`top top` → `bottom top`) chama `logo.saida(progresso)`, que só faz o canvas perder opacidade. **EXATO.**

## 6. Efeito colateral observado (não corrigir no site, só registrar)

Depois de **descer além do hero e voltar ao topo**, o lema "Capacitação em qualidade" e o indicador "Role" **ficam invisíveis** (opacidade 0, desfoque 8 px, deslocados 22 px). O título, o texto e os botões voltam normalmente. **OBSERVADO** (estilos inline lidos depois da volta: `opacity: 0; filter: blur(8px); translate3d(…, 22px, …)`).

Causa provável (inferência): `.hero__lema` e `.hero__rolar` são animados por duas animações ao mesmo tempo. Uma é a entrada (`entradaHero`, `fromTo` de opacidade 0 → 1). A outra é a saída (`.to` desta ficha). A saída gravou como "estado inicial" os valores do começo da entrada (opacidade 0). Ao rolar de volta para o progresso 0, ela restaura esses valores.

> Para uma reconstrução fiel ao **comportamento publicado**, isso é parte do estado atual. Para uma reconstrução fiel à **intenção**, faça a saída usar `fromTo` com estado inicial explícito (opacidade 1, y 0, sem desfoque) ou anime um contêiner diferente do da entrada. Registre a escolha.

## 7. Como reproduzir (sem 3D)

```js
gsap.timeline({ scrollTrigger: { trigger: '.hero', start: 'top top', end: () => `+=${innerHeight}`, pin: true, scrub: true, anticipatePin: 1 } })
  .fromTo('.hero__conteudo', { opacity: 1, y: 0, filter: 'blur(0px)' }, { opacity: 0, y: -50, filter: 'blur(10px)', ease: 'power1.in', duration: 0.5 }, 0)
  .to('.hero', { '--vinheta': 1, duration: 1 }, 0)
```

## 8. Como adaptar

- A trava de 1 tela é curta e enérgica. Para uma narrativa mais lenta, use `+=${innerHeight * 1.5}`.
- Sem cena 3D, a mesma linha do tempo pode escalar uma imagem (de 1 para 1,4) para simular o *dolly*.
- O som "virada" é opcional e só toca com o som ligado.
