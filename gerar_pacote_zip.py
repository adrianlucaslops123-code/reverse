#!/usr/bin/env python3
"""Gera o pacote CDC_PACOTE_COMPLETO_<AAAA-MM-DD>.zip.

O ZIP junta, numa pasta só:
  - LEIA-ME_PRIMEIRO.md, MODELO_DE_PEDIDO.txt, HISTORICO_DE_ALTERACOES.md,
    este script, VERSAO.txt e MANIFESTO_SHA256.txt (gerados agora);
  - CDC_SITE_BACKUP/ (documentação);
  - landing-page-cdc/ (código-fonte do site, sem node_modules/ e sem dist/).

Uso no repositório "reverse" (código vindo do Git):
    python3 gerar_pacote_zip.py --site <clone do landing-page-cdc ou URL> --commit 65c37e7

Uso dentro de um pacote já descompactado (código vindo da pasta landing-page-cdc/):
    python3 gerar_pacote_zip.py

Só usa a biblioteca padrão do Python 3.8+ e o Git (quando a origem é um repositório).
"""
import argparse
import datetime
import hashlib
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
URL_SITE = 'https://github.com/adrianlucaslops123-code/landing-page-cdc.git'
ARQUIVOS_RAIZ = ['LEIA-ME_PRIMEIRO.md', 'MODELO_DE_PEDIDO.txt', 'HISTORICO_DE_ALTERACOES.md', 'gerar_pacote_zip.py']
PASTA_DOCS = 'CDC_SITE_BACKUP'
PASTA_SITE = 'landing-page-cdc'
IGNORAR = {'node_modules', 'dist', 'dist-artefato', '.git', '.DS_Store', 'Thumbs.db', '__pycache__'}


def git(*args, cwd=None):
    return subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def eh_repositorio(pasta):
    try:
        return git('rev-parse', '--is-inside-work-tree', cwd=pasta) == 'true' and git('rev-parse', '--show-toplevel', cwd=pasta) == str(Path(pasta).resolve())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def copiar_pasta(origem, destino):
    shutil.copytree(origem, destino, ignore=lambda _d, nomes: [n for n in nomes if n in IGNORAR])


def main():
    ap = argparse.ArgumentParser(description='Gera o ZIP do pacote completo do site CDC.')
    ap.add_argument('--site', help='pasta do código do site (repositório Git ou pasta comum) ou URL Git. '
                    'Padrão: ./landing-page-cdc se existir; senão, clona ' + URL_SITE)
    ap.add_argument('--commit', default='HEAD', help='commit, branch ou tag (só quando a origem é Git). Padrão: HEAD')
    ap.add_argument('--saida', default='.', help='pasta onde salvar o ZIP. Padrão: pasta atual')
    ap.add_argument('--data', default=datetime.date.today().isoformat(), help='data no nome do pacote (AAAA-MM-DD)')
    a = ap.parse_args()

    nome = f'CDC_PACOTE_COMPLETO_{a.data}'
    origem = a.site or (str(RAIZ / PASTA_SITE) if (RAIZ / PASTA_SITE).is_dir() else URL_SITE)

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        pacote = tmp / nome
        pacote.mkdir()

        # 1. código do site
        if Path(origem).is_dir() and not eh_repositorio(origem):
            copiar_pasta(origem, pacote / PASTA_SITE)
            info_site = f'pasta local sem Git ({Path(origem).resolve().name}); ver HISTORICO_DE_ALTERACOES.md'
        else:
            repo = Path(origem) if Path(origem).is_dir() else tmp / 'clone'
            if not Path(origem).is_dir():
                git('clone', '--quiet', origem, str(repo))
            commit = git('rev-parse', a.commit + '^{commit}', cwd=repo)
            assunto = git('log', '-1', '--format=%s', commit, cwd=repo)
            arquivo = tmp / 'site.zip'
            git('archive', '--format=zip', '-o', str(arquivo), commit, cwd=repo)
            with zipfile.ZipFile(arquivo) as z:
                z.extractall(pacote / PASTA_SITE)
            info_site = f'commit {commit} ("{assunto}")'

        # 2. documentação e arquivos da raiz
        copiar_pasta(RAIZ / PASTA_DOCS, pacote / PASTA_DOCS)
        for arq in ARQUIVOS_RAIZ:
            shutil.copy2(RAIZ / arq, pacote / arq)

        # 3. versão
        if eh_repositorio(RAIZ):
            docs = git('rev-parse', 'HEAD', cwd=RAIZ)
            if git('status', '--porcelain', cwd=RAIZ):
                docs += ' (com alterações ainda não registradas em commit)'
        else:
            docs = 'pasta local sem Git'
        agora = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
        (pacote / 'VERSAO.txt').write_text(
            f'Pacote: {nome}\nGerado em: {agora}\nSite (landing-page-cdc): {info_site}\n'
            f'Documentação (reverse): {docs}\nGerado por: gerar_pacote_zip.py\n', encoding='utf-8')

        # 4. manifesto SHA-256 (formato do sha256sum, caminhos relativos à raiz do pacote)
        arquivos = sorted(p for p in pacote.rglob('*') if p.is_file())
        linhas = [f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(pacote).as_posix()}' for p in arquivos]
        (pacote / 'MANIFESTO_SHA256.txt').write_text('\n'.join(linhas) + '\n', encoding='utf-8')

        # 5. ZIP
        destino = Path(a.saida).resolve() / f'{nome}.zip'
        destino.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for p in sorted(q for q in pacote.rglob('*') if q.is_file()):
                z.write(p, (Path(nome) / p.relative_to(pacote)).as_posix())

    print(f'ZIP gerado: {destino} ({destino.stat().st_size / 1_048_576:.1f} MB, {len(linhas) + 1} arquivos)')
    print(f'Site: {info_site}')


if __name__ == '__main__':
    main()
