# Ingrid Beauty

Site estático responsivo em português para **INGRID BEAUTY / Ingrid Ferreira**. Não requer framework, servidor de aplicação nem dependências de runtime; imagens, fontes e QR Pix são locais.

## Arquivos principais

- `external-index.html` — versão externa editável e fonte principal do site.
- `img/` e `fonts/` — imagens e fontes locais utilizadas pelo site. `img/hero-ingrid-source.jpeg` preserva uma cópia byte a byte da foto original enviada; o site usa os recortes transparentes PNG/WebP.
- `index.html` — versão autônoma gerada, com recursos incorporados.
- `build_variants.py` — gera novamente as variantes externas, autônoma, Netlify e ZIPs de publicação.
- `RELATORIO_FINAL.md` — escopo, verificações e dados ainda pendentes de confirmação.

## Prévia local

Na raiz do projeto, execute:

```bash
python3 -m http.server 8080
```

Abra `http://localhost:8080/` para a versão autônoma ou `http://localhost:8080/external-index.html` para a versão externa.

## Regenerar os artefatos

```bash
python3 build_variants.py
```

O script usa apenas a biblioteca padrão do Python e atualiza `index.html`, `external/index.html`, `netlify-package/` e os dois ZIPs de publicação.

## Publicação

- **Netlify:** publique `netlify-package/` ou envie `ingrid-beauty-netlify.zip`.
- **Arquivo único:** use `index.html` ou `ingrid-beauty-single-file.zip`.

Antes de divulgar o Pix, confira no `RELATORIO_FINAL.md` os itens marcados como **[A CONFIRMAR]**, especialmente titular e cidade temporários do BRCode. O site não afirma confirmação automática de agendamento ou pagamento.
