# Relatório final — Ingrid Beauty

## Entrega

Site responsivo em português do Brasil para **INGRID BEAUTY / Ingrid Ferreira**, com catálogo completo, agenda acessível e geração local de Pix/QR. A primeira dobra foi redesenhada com retrato recortado da foto de Ingrid, tipografia dourada em camadas e movimento suave; a versão final inclui as 26 fotos do catálogo otimizadas para a web. O link de Instagram permanece acessível no cabeçalho, contato e rodapé.

### Arquivos

| Caminho | Conteúdo |
|---|---|
| `index.html` | Versão autônoma em arquivo único: CSS, JavaScript, fontes, logotipo, catálogo e retrato transparente do hero incorporados em base64. |
| `external-index.html` | Versão com imagens e fontes locais, recomendada para deploy e edições futuras. |
| `external/index.html` | Cópia externa com caminhos relativos para publicar dentro da pasta `external/`. |
| `build_variants.py` | Regera a versão autônoma, a cópia aninhada, o pacote Netlify e os ZIPs a partir de `external-index.html`. |
| `README.md` / `.gitignore` | Instruções de prévia/build/publicação e exclusões de temporários/artefatos gerados para o fluxo Git. |
| `img/hero-ingrid-cutout.webp` / `.png` | Recorte transparente derivado do JPEG enviado (1044 × 1280 px); WebP sem perdas e PNG de fallback, ambos preservando os valores RGB da fonte. |
| `img/hero-ingrid-source.jpeg` | Cópia byte a byte do JPEG enviado para versionamento/rastreabilidade; não é referenciada pelo site nem incluída no pacote de deploy. A cópia no upload também permanece intacta. |
| `img/procedimentos/` | PNGs originais preservados e WebPs quadrados otimizados (600 × 600 px) para os 26 procedimentos; o site entrega WebP com fallback para PNG. |
| `netlify-package/` | Site externo pronto para publicação, com arquivos e configuração na raiz do pacote. |
| `ingrid-beauty-netlify.zip` | Pacote pronto para publicação estática. |
| `ingrid-beauty-single-file.zip` | ZIP da versão autônoma. |
| `ingrid-beauty-git-ready.zip` | Arquivo-fonte para Git, com código, assets, relatório e capturas; sem temporários, pacote de deploy gerado ou diretório `.git`. |
| `ATUALIZACAO_CATALOGO.md` | Relação completa de IDs, procedimentos, PNGs e fotos originais associadas. |
| `screenshots/desktop-hero.png` | Hero desktop, 1440 × 1000 px, com a nova composição em camadas. |
| `screenshots/mobile-hero.png` | Hero móvel, 390 × 844 px, com retrato centralizado e conteúdo abaixo. |
| `screenshots/desktop-home.png` | Prévia desktop atualizada do topo do site e da nova composição do hero. |
| `screenshots/desktop-about.png` | Seção Sobre após remover a imagem selecionada e reorganizar o texto em uma coluna. |
| `screenshots/mobile-about.png` | Versão móvel da seção Sobre, sem a imagem selecionada. |
| `screenshots/desktop-space.png` | Seção do espaço após remover o cartão de foto e reorganizar o texto. |
| `screenshots/mobile-space.png` | Versão móvel da seção do espaço, sem cartão de foto. |
| `screenshots/desktop-procedures.png` | Prévia desktop do catálogo atualizado. |
| `screenshots/desktop-pix.png` | Checkout Pix desktop, 1440 × 1000 px, com QR, copia e cola e instruções. |
| `screenshots/mobile-home.png` | Prévia móvel do topo do site (390 × 844 px). |
| `screenshots/mobile-pix.png` | Checkout Pix móvel, 390 × 1100 px; o formato alto deixa visíveis QR, código, instruções e ação de WhatsApp. |

A pasta está preparada com `README.md` e `.gitignore`; nenhum `git init`, `git add` ou commit foi executado.

## Funcionalidades

- 26 registros com IDs estáveis `ingrid-01` a `ingrid-26`; cada card mantém seu preço, duração, foto, categoria e condições ao filtrar, pesquisar, abrir detalhes, agendar, gerar a mensagem de WhatsApp e calcular o Pix.
- Clique na imagem, no nome ou em “Ver procedimento” abre os detalhes e a ação de agendamento seleciona o serviço correspondente.
- Avaliação com valor interno `null` e exibição “A consultar”; não é tratada como gratuita nem aceita pagamento pelo Pix.
- Durações não informadas aparecem como “Duração a confirmar”; horários são preferências sujeitas à confirmação da Ingrid.
- Agenda lateral com prevenção de itens repetidos, armazenamento local e alternativa em memória, campos acessíveis e horários em intervalos específicos. Datas passadas e domingos são bloqueados. A quinta-feira respeita os três intervalos, e sábado distingue 08h30–12h00 e 12h00–16h00.
- WhatsApp abre somente por ação direta, em nova aba, com `noopener` e mensagem codificada. Nenhuma ação automática declara horário ou pagamento confirmado.
- Pix gerado localmente em JavaScript: payload BACEN/EMV, chave, valor com centavos, CRC16, QR SVG offline, cópia do código, cópia da chave, contador de 15 minutos e opção de regenerar. Nenhum dado do Pix é enviado a terceiros ou a um gateway.
- Instagram em destaque no topo: [@ingridbeauty.br](https://instagram.com/ingridbeauty.br), com nova aba e proteção `noopener`.
- Identidade visual, fontes locais, layout móvel, foco visível, uso por teclado, `aria` e respeito a `prefers-reduced-motion`.

## Otimização mobile, leveza e movimento

- O hero usa a paleta local `#F7F1E6`, `#B98A31` e `#2C211C`, sem alterar a paleta global restante. No desktop, texto e retrato ficam lado a lado; no celular, o retrato é centralizado e título, complemento e botões aparecem abaixo dele. O rosto permanece inteiro e visível.
- A tipografia preenchida “INGRID” desliza atrás do retrato por 31 s e o contorno “BEAUTY” percorre a parte inferior em sentido oposto por 34 s. Os trilhos duplicados fazem o movimento contínuo, recortado dentro da composição; são decorativos, não clicáveis e ocultos para leitores de tela. O contorno permanece abaixo do rosto.
- O hero agora usa a nova foto JPEG enviada (1044 × 1280 px, com fundo preto opaco) no lugar da foto anterior. A transparência foi derivada por segmentação não generativa, com opacidade total no interior e transição suave na borda; os valores RGB foram copiados exatamente da fonte, sem clareamento, ajuste de cor, retoque, síntese ou repintura. O fade CSS fica limitado à parte inferior; os filtros de brilho/saturação foram removidos. O retrato foi reduzido para 94% da altura do hero no desktop e 88% no mobile. O JPEG de origem permanece intacto no upload e foi copiado sem alteração para `img/hero-ingrid-source.jpeg` para versionamento; essa cópia não é servida pelo site. O upload anterior `image-1.png` e `img/IMG_3553.jpeg` continuam preservados. O site usa os derivados transparentes PNG/WebP (WebP lossless), ambos incorporados em base64 no `index.html` autônomo.
- Imagens com dimensões explícitas evitam mudanças de layout; fotos fora da primeira tela usam carregamento tardio e decodificação assíncrona. Navegadores compatíveis recebem WebP; os PNGs/JPEGs originais permanecem como alternativa, e os 26 caminhos PNG exigidos foram preservados. A imagem da seção Sobre e o cartão/lightbox selecionados da seção Espaço continuam removidos conforme solicitado.
- Os 26 WebPs do catálogo totalizam **1.204.994 bytes**, contra **3.819.333 bytes** dos PNGs: redução aproximada de **68%** no peso da galeria carregada. Com o hero atualizado em WebP lossless (**732.464 bytes**), os derivados WebP do projeto somam **2.274.638 bytes**.
- Há animação breve e suave de entrada para o retrato e o texto, além de microinterações existentes. Com `prefers-reduced-motion`, as entradas e trilhos param, a tipografia decorativa fica estática e centralizada, e o conteúdo permanece visível.
- A versão externa não depende de CDN para fontes, imagens ou QR. O arquivo autônomo incorpora imagens e fontes; Instagram e WhatsApp só são abertos pelos links/ações diretos da pessoa.

## Verificações

- Os 26 arquivos de imagem estão associados aos registros e podem ser carregados pelo site.
- A associação de cada imagem foi feita semanticamente conforme o conteúdo da foto; as imagens são ilustrativas e não são apresentadas como resultados de clientes da Ingrid. Consulte `ATUALIZACAO_CATALOGO.md` para o mapa completo.
- Teste em Chromium após o rebuild: site externo, pacote Netlify, versão externa aninhada e arquivo único; 26/26 cards e imagens carregaram (WebP nos formatos externos e imagens incorporadas no arquivo único), sem erros de JavaScript, console ou requisições. Bloqueando WebP de propósito, os 26 PNGs originais assumiram corretamente; bloqueando também um PNG, a imagem alternativa da categoria carregou.
- Chromium validou a nova dobra em 1440 px, 900 px, 390 px e 320 px; não há rolagem horizontal. A imagem transparente de 1044 × 1280 px carrega nos quatro formatos (externo, aninhado, Netlify e autônomo); todos mantêm 26/26 imagens do catálogo carregadas, sem erros de JavaScript, console, respostas HTTP ou requisições.
- O fallback PNG do hero foi validado bloqueando deliberadamente o WebP; o PNG transparente de 1044 × 1280 px carregou corretamente. Foram verificados os níveis da composição (`INGRID` atrás, retrato no meio, contorno à frente), o movimento em sentidos opostos, a distância do contorno ao rosto, o título e a ordem mobile. “Ver procedimentos” navega para `#procedimentos`; “Agendar horário” abre a agenda. Com movimento reduzido, as animações param e os textos decorativos ficam estáticos; o checkout Pix e o QR seguem validados em desktop e celular.
- O payload Pix e seu CRC são validados no navegador, e o QR é gerado em SVG local. Para Brow Lamination — R$ 150,00, o payload termina em `6304E2C5`; a leitura local do QR reconstruiu o payload completo sem divergência. A aceitação pelo banco depende de a chave Pix estar cadastrada corretamente e dos dados temporários do recebedor serem confirmados.
- A versão única não depende de imagens, fontes ou scripts hospedados externamente para renderizar o site e gerar o QR.

## Itens a confirmar — [A CONFIRMAR]

Os dados abaixo não são inventados nem publicados como informação confirmada no site:

1. Endereço completo e cidade/UF do espaço.
2. Formas de pagamento aceitas.
3. Valor da avaliação (apresentado no site como “A consultar”).
4. Domínio definitivo.
5. Nome do titular associado à chave Pix. O BRCode usa temporariamente `INGRID FERREIRA`.
6. Cidade do titular Pix. O BRCode usa temporariamente `SAO PAULO` por exigência funcional do payload.

## Referência de investimento do projeto

**R$ 4.500,00** como sugestão de preço do escopo entregue: direção visual, site responsivo, tratamento de assets fornecidos, catálogo com 26 serviços, agenda local, Pix BRCode/QR local, acessibilidade, SEO, testes, pacotes de publicação e documentação. Manutenção e evoluções posteriores podem ser orçadas à parte.

## Publicação

### Netlify

1. Publique o conteúdo de `netlify-package/` ou envie `ingrid-beauty-netlify.zip` pelo fluxo de deploy manual.
2. Conecte o domínio definitivo quando estiver disponível.
3. Confirme os dados Pix antes de divulgar o pagamento por QR.

### GitHub + Vercel

1. Crie um repositório novo para o site.
2. Copie o conteúdo de `netlify-package/` para a raiz, preservando `index.html`, `img/`, `fonts/`, `og.jpg` e `netlify.toml`.
3. Importe o repositório na Vercel; não há comando de build necessário para o site estático.
4. Configure o domínio definitivo quando confirmado. O script atualiza canonical e metadados sociais para a origem publicada.

## Alteração de imagens e dados Pix

- Para atualizar fotos, substitua os PNGs correspondentes em `img/procedimentos/` e atualize a versão externa. A versão autônoma deve ser gerada novamente para incorporar as imagens atualizadas.
- No JavaScript, as configurações do Pix estão reunidas no objeto `PIX` no topo do script. Atualize os campos somente após confirmação dos dados bancários; chave telefônica no BRCode deve conter `55` + DDD + número.
- O nome do recebedor e a cidade seguem os limites do formato BRCode: 25 caracteres e 15 caracteres, respectivamente.
