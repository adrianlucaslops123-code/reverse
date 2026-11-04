# CDC Capacitação em Qualidade · Pacote completo do site (LEIA-ME PRIMEIRO)

Este pacote reúne **tudo** o que é preciso para reconstruir, alterar ou reaproveitar o site da CDC (`https://cdc-cursos-kappa.vercel.app/`) sem depender de nenhuma plataforma:

| Pasta / arquivo | O que é |
|---|---|
| `LEIA-ME_PRIMEIRO.md` | este guia |
| `MODELO_DE_PEDIDO.txt` | **modelo para você preencher** com as alterações que quer e colar na conversa com a IA |
| `HISTORICO_DE_ALTERACOES.md` | registro das versões do pacote e de cada alteração feita no site |
| `VERSAO.txt` | de qual commit do site e da documentação este pacote foi gerado, e quando |
| `MANIFESTO_SHA256.txt` | lista de todos os arquivos com a impressão digital SHA-256, para conferir se nada se corrompeu |
| `gerar_pacote_zip.py` | script que monta este ZIP de novo, com a mesma estrutura, depois de uma alteração (`python3 gerar_pacote_zip.py` na raiz do pacote) |
| `CDC_SITE_BACKUP/` | documentação completa: especificação mestre, prompt mestre, design system, 42 fichas de experiências, inventário de recursos, dependências, guia de migração, capturas de referência e relatório |
| `landing-page-cdc/` | **o código-fonte real do site** (commit `65c37e7`), com logo, fotos, PDFs e o leitor de PDF. Não tem `node_modules/` nem `dist/` (são gerados pelos comandos abaixo) |

> No repositório `adrianlucaslops123-code/reverse` a pasta `landing-page-cdc/` não fica junto: o código está no repositório `adrianlucaslops123-code/landing-page-cdc`. O script `gerar_pacote_zip.py` junta os dois e gera este ZIP.

---

## Como pedir alterações numa conversa futura (para você)

1. Abra uma conversa nova com o Claude (ou com outra IA ou ferramenta de desenvolvimento).
2. **Anexe este ZIP.** Se ele for grande demais para anexar, anexe só a pasta `CDC_SITE_BACKUP/` e informe o link do repositório `https://github.com/adrianlucaslops123-code/landing-page-cdc`. Numa sessão do Claude Code, conecte os repositórios `reverse` e `landing-page-cdc`.
3. Abra o `MODELO_DE_PEDIDO.txt` (no Bloco de Notas ou em qualquer editor), **preencha** o que quer e **cole o texto** na conversa.
4. A IA lê este guia e o prompt mestre, aplica **só** o que você pediu, testa e devolve um ZIP novo (ou os arquivos alterados) com um relatório "antes → depois".
5. Guarde o ZIP novo no computador. Ele substitui este e já traz o histórico atualizado.

---

## Instruções para a IA que receber este pacote

Siga estas regras antes de qualquer outra coisa:

1. **Leia, nesta ordem:** este arquivo → o pedido do usuário (feito a partir do `MODELO_DE_PEDIDO.txt`) → `CDC_SITE_BACKUP/CDC_SITE_RECONSTRUCTION_PROMPT.md` (siga o bloco "PROMPT" inteiro) → `HISTORICO_DE_ALTERACOES.md` → os documentos e as fichas que o prompt indicar.
2. **Fontes de verdade:** o código em `landing-page-cdc/` vence a documentação. A documentação vence suposições. Nunca invente textos, números, preços, links ou efeitos.
3. **Modo:** use o modo marcado no pedido (A reconstrução fiel · B reutilização com outra identidade · C alteração controlada). Se não estiver marcado e não der para deduzir, **pergunte**.
4. **Escopo:** mude **só** o que foi pedido. Não refatore, não atualize dependências, não "melhore" nada por conta própria. No modo C, não corrija os efeitos colaterais conhecidos (lista no prompt, §4.10), a não ser que o pedido mande.
5. **Onde mexer:** nos arquivos de `landing-page-cdc/`. O mapa "onde fica cada coisa" está no `CDC_SITE_BACKUP/README.md` §3 e na especificação mestre §13.
6. **Testar:** Node 22.13+ → `cd landing-page-cdc && npm ci && npm run build`, sem erro. Se puder abrir o site (`npm run dev` ou `npm run preview`), confira as partes afetadas com o checklist da especificação mestre §18.
7. **Manter a documentação coerente:** se a alteração mudar algo documentado (texto, token, parâmetro de ficha), atualize o documento correspondente em `CDC_SITE_BACKUP/` e acrescente uma entrada no `HISTORICO_DE_ALTERACOES.md`.
8. **Entregar** no formato pedido (campo "COMO QUERO RECEBER"). Para um ZIP novo:
   - atualize o `HISTORICO_DE_ALTERACOES.md` primeiro;
   - na raiz do pacote, rode `python3 gerar_pacote_zip.py --saida <pasta>`. O script copia `landing-page-cdc/` sem `node_modules/` e sem `dist/`, refaz o `VERSAO.txt` e o `MANIFESTO_SHA256.txt` e gera `CDC_PACOTE_COMPLETO_<AAAA-MM-DD>.zip` com a mesma estrutura;
   - sem Python, monte o ZIP à mão com a mesma estrutura e o manifesto refeito.
9. **Nunca** publique na Vercel, nunca envie para o branch principal e nunca apague arquivos sem autorização explícita no pedido.
10. **Relatório final:** o que mudou (arquivo e valores antigos → novos), o que foi testado, decisões tomadas e o que ficou pendente.

---

## Rodar o site no computador

1. Instale o Node.js 22.13 ou mais novo (https://nodejs.org).
2. Abra um terminal na pasta `landing-page-cdc/` e rode:

```bash
npm ci            # instala as versões exatas (não atualiza nada)
npm run dev       # abre em http://localhost:5174
npm run build     # gera a pasta dist/ com o site pronto para qualquer hospedagem
```

O `npm run build` deste código gera arquivos **idênticos** aos do site publicado (verificado em 4 nov. 2026).

## Conferir a integridade dos arquivos

- Linux ou macOS, na raiz do pacote: `sha256sum -c MANIFESTO_SHA256.txt` (no macOS: `shasum -a 256 -c MANIFESTO_SHA256.txt`).
- Windows (PowerShell): `Get-FileHash -Algorithm SHA256 <arquivo>` e compare com a linha do arquivo no manifesto.

## Guardar com segurança

Mantenha este ZIP em pelo menos dois lugares (por exemplo, o computador e uma nuvem). O que **não** está no pacote e precisa ser guardado à parte (logo vetorial, fotos originais, vídeos, conteúdo do curso na Kiwify, acessos ao domínio e às contas) está listado em `CDC_SITE_BACKUP/ASSETS_INVENTORY.md` §12.
