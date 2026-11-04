# Histórico de alterações do pacote e do site CDC

Cada alteração feita no site ou na documentação ganha uma entrada aqui, **da mais nova para a mais antiga**. Formato de cada entrada: data · versão do pacote · pedido · commit do site · arquivos alterados · valores antigos → novos · testes · pendências.

---

## v1 · 2026-11-04 · Pacote inicial

- **Pedido:** engenharia reversa completa do site, documentação, biblioteca de experiências, prompt mestre e pacote de preservação.
- **Site:** `landing-page-cdc` no commit `65c37e7` ("Adiciona três vídeos à área comum de vídeos", 3 nov. 2026), o mesmo publicado em `https://cdc-cursos-kappa.vercel.app/`.
- **Alterações no site:** nenhuma.
- **Documentação criada:** `CDC_SITE_BACKUP/` (especificação mestre, prompt mestre, design system, índice e 42 fichas da biblioteca, inventário de recursos, dependências, guia de migração, 36 capturas de referência, relatório de conclusão), `LEIA-ME_PRIMEIRO.md`, `MODELO_DE_PEDIDO.txt`, este histórico e `gerar_pacote_zip.py`.
- **Testes:** `npm ci` + `npm run build` (Node 22.23.4) geraram arquivos idênticos byte a byte aos publicados. 435 textos e 44 atributos do `index.html` conferidos na especificação. Links internos e IDs das fichas conferidos.
- **Pendências conhecidas:** ver `CDC_SITE_BACKUP/RELATORIO_DE_CONCLUSAO.md` §6 e §7.
