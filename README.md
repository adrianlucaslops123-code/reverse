# reverse: engenharia reversa do site da CDC Capacitação em Qualidade

Este repositório guarda a **documentação técnica e visual** do site `https://cdc-cursos-kappa.vercel.app/`, feita por engenharia reversa do site publicado e do código-fonte (`adrianlucaslops123-code/landing-page-cdc`, commit `65c37e7`).

**Comece por [`LEIA-ME_PRIMEIRO.md`](LEIA-ME_PRIMEIRO.md).** Ele explica como pedir alterações numa conversa futura usando o [`MODELO_DE_PEDIDO.txt`](MODELO_DE_PEDIDO.txt).

Documentação em **[`CDC_SITE_BACKUP/`](CDC_SITE_BACKUP/README.md)**:

- [`CDC_SITE_MASTER_SPECIFICATION.md`](CDC_SITE_BACKUP/CDC_SITE_MASTER_SPECIFICATION.md): especificação completa do site
- [`CDC_SITE_RECONSTRUCTION_PROMPT.md`](CDC_SITE_BACKUP/CDC_SITE_RECONSTRUCTION_PROMPT.md): prompt mestre para reconstruir, reutilizar ou alterar
- [`CDC_DESIGN_SYSTEM.md`](CDC_SITE_BACKUP/CDC_DESIGN_SYSTEM.md): sistema visual
- [`CDC_DESIGN_LIBRARY_INDEX.md`](CDC_SITE_BACKUP/CDC_DESIGN_LIBRARY_INDEX.md) e [`CDC_DESIGN_LIBRARY/`](CDC_SITE_BACKUP/CDC_DESIGN_LIBRARY/): 42 fichas de experiências digitais
- [`ASSETS_INVENTORY.md`](CDC_SITE_BACKUP/ASSETS_INVENTORY.md) e [`TECHNICAL_DEPENDENCIES.md`](CDC_SITE_BACKUP/TECHNICAL_DEPENDENCIES.md): recursos e dependências
- [`REFERENCIAS_VISUAIS/`](CDC_SITE_BACKUP/REFERENCIAS_VISUAIS/): capturas de referência
- [`RELATORIO_DE_CONCLUSAO.md`](CDC_SITE_BACKUP/RELATORIO_DE_CONCLUSAO.md): relatório do trabalho

Na raiz: [`HISTORICO_DE_ALTERACOES.md`](HISTORICO_DE_ALTERACOES.md) (versões do pacote) e [`gerar_pacote_zip.py`](gerar_pacote_zip.py). O script junta esta documentação e o código do site num único ZIP para guardar no computador:

```bash
git clone https://github.com/adrianlucaslops123-code/landing-page-cdc.git
python3 gerar_pacote_zip.py --site landing-page-cdc --commit 65c37e7
```

Este repositório contém só documentação. O código e os recursos do site continuam no repositório `landing-page-cdc`, que não foi alterado.
