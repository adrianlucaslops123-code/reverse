# CRT-01 · Cartões que inclinam (`data-inclinar`) e luz que segue o mouse (`data-luz`)

> Legenda: **EXATO** · **CALCULADO** · **OBSERVADO** · **ESTIMATIVA** · **NÃO IDENTIFICADO**.

| Campo | Valor |
|---|---|
| Estado de implementação | **Implementado, parcialmente validado**: a aparência dos cartões foi capturada. A luz e a inclinação têm valores EXATOS do código, mas não foram medidas em execução |
| Portabilidade | Direta |
| Onde aparece | `data-inclinar` + luz: 2 credenciais (Equipe) e 3 planos (Treinamentos) = 5 · só `data-luz`: 5 recursos (Material e Estrutura), 3 acessos (Área do aluno), 1 janela do app = 9 |
| Arquivos de origem | `src/motor/interacao.js` (bloco "cartões", linhas 93–120) · `src/estilo/secoes.css` (`.credencial`, `.plano`, `.recurso`, `.acesso`) · `src/estilo/aplicativo.css` (`.janela-app::before`) |
| Dependências | GSAP 3.15.0 (`quickTo`, `set`) |

## 1. Lógica (EXATO)

```js
const inclina = el.hasAttribute('data-inclinar') && !reduzido
const rx = inclina ? gsap.quickTo(el, 'rotationX', { duration: 0.6, ease: 'power3.out' }) : null
const ry = inclina ? gsap.quickTo(el, 'rotationY', { duration: 0.6, ease: 'power3.out' }) : null
if (inclina) gsap.set(el, { transformPerspective: 1100 })
el.addEventListener('pointermove', (e) => {
  const r = el.getBoundingClientRect()
  const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height
  el.style.setProperty('--mx', `${(px * 100).toFixed(1)}%`)
  el.style.setProperty('--my', `${(py * 100).toFixed(1)}%`)
  el.style.setProperty('--brilho', '1')
  if (inclina) { rx(-(py - 0.5) * 7); ry((px - 0.5) * 9) }
})
el.addEventListener('pointerleave', () => { el.style.setProperty('--brilho', '0'); if (inclina) { rx(0); ry(0) } })
```

| Parâmetro | Valor |
|---|---|
| Inclinação máxima em X | ±3,5° (topo do cartão vem para a frente quando o mouse está em cima) |
| Inclinação máxima em Y | ±4,5° |
| Perspectiva | 1 100 px por elemento. Grades com `perspective: 1200px` (credenciais) e `1400px` (planos) + `transform-style: preserve-3d` nos cartões |
| Seguimento | 0,6 s `power3.out`. Volta a 0° com a mesma curva |
| Condição | só `(hover: hover) and (pointer: fine)`. A inclinação desliga no movimento reduzido. **A luz continua** no movimento reduzido |

## 2. A luz de cada tipo de cartão (`::before`, opacidade `var(--brilho)`)

| Cartão | Gradiente da luz | Transição |
|---|---|---|
| `.credencial` (holográfica) | `radial-gradient(420px circle at --mx --my, rgba(255,178,74,.16), transparent 60%)` + faixa `linear-gradient(115deg, transparent 30%, rgba(168,216,255,.1) 45%, rgba(201,159,83,.12) 55%, transparent 70%)` | 0,4 s |
| `.plano` | `radial-gradient(380px circle ..., rgba(251,120,30,.14), transparent 62%)` | 0,4 s |
| `.recurso` | `radial-gradient(300px circle ..., rgba(168,216,255,.12), transparent 60%)` **+ borda que acende** (`::after`, ver §3) | 0,35 s |
| `.acesso` | `radial-gradient(300px circle ..., rgba(251,120,30,.16), transparent 60%)` | 0,35 s |
| `.janela-app` | `radial-gradient(440px circle ..., rgba(251,120,30,.1), transparent 62%)` | 0,4 s |

## 3. Borda que acende perto do mouse (`.recurso::after`, EXATO)

```css
.recurso::after {
  content: ''; position: absolute; inset: 0; pointer-events: none; border-radius: inherit; padding: 1px;
  opacity: var(--brilho, 0); transition: opacity 0.35s;
  background: radial-gradient(240px circle at var(--mx, 50%) var(--my, 50%), var(--brasa), transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0);
}
```

O `padding: 1px` com a máscara "caixa de conteúdo **exclui** caixa inteira" deixa visível só o anel de 1 px da borda. O gradiente radial faz só o trecho da borda perto do mouse ficar laranja.

## 4. Anatomia dos cartões (EXATO)

| Cartão | Medidas e estilo |
|---|---|
| `.credencial` | padding `clamp(24px, 3vw, 40px)`, raio 18, fundo `linear-gradient(150deg, --aco-2, --aco-1 60%)`, contorno `fio` + sombra `0 30px 60px -40px #000`. Topo mono 12 px caixa alta. Chip dourado 38 × 28 px, raio 6, `linear-gradient(135deg, #e7c886, --ouro 45%, #8a6a32)`. Nome `760 clamp(30px, 3.2vw, 48px)/1`, largura 112 %. Registros em pílulas `500 13px` mono, sigla da entidade em brasa |
| `.plano` | padding `clamp(24px, 2.4vw, 34px)`, raio 18, fundo `--aco-1`, contorno `fio`. Destaque: `linear-gradient(165deg, #1f1610, --aco-1 55%)`, contorno `rgba(251,120,30,.38)`, sombra `0 40px 80px -50px rgba(251,120,30,.6)`. Preço `800 clamp(54px, 5.4vw, 84px)/0.9`, "R$" a 0,3 em em brasa |
| `.recurso` | padding `clamp(24px, 2.4vw, 34px)`, raio 18, fundo `--aco-1`. Ícone 44 px de traço laranja 1,6 px |
| `.acesso` | altura mínima 200 px (140 px em ≤ 860 px), padding 26 px, raio 18. Seta de 26 px que anda `4px −4px` no *hover* (0,4 s mola) |
| `.janela-app` | ver CEN-09 |

## 5. Como adaptar

- Inclinação de 3–5° é perceptível sem enjoar. Não passe de 10°.
- A luz usa variáveis CSS. Troque só as cores dos gradientes.
- A borda que acende (§3) é a técnica mais reutilizável. Ela funciona com qualquer raio de borda (`border-radius: inherit`).
