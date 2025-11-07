# 📧 Gerador de Newsletter - Inserir Imagens Fatiadas

Script automatizado para inserir imagens fatiadas (exportadas do Affinity Designer ou Photoshop) na newsletter HTML do Assaí.

## 🎯 O que faz?

O script lê todas as imagens da pasta `/images` e insere automaticamente no arquivo `index.html` dentro da tabela com id `CONTEUDO`, gerando o código:

```html
<tr><td><img src="images/nome-do-arquivo.png"/></td></tr>
```

## 📋 Pré-requisitos

### Para a versão Python:
- Python 3.x instalado

### Para a versão Node.js:
- Node.js instalado

## 🚀 Como usar

### 1. Prepare suas imagens

1. Fatia sua arte no **Affinity Designer/Photo**
2. Exporte as imagens fatiadas para a pasta `images/` no mesmo diretório do `index.html`
3. As imagens devem estar nomeadas na ordem que deseja que apareçam (ex: `01-header.png`, `02-banner.png`, etc)

### 2. Execute o script

#### Versão Python:
```bash
python gerar_newsletter.py
```

#### Versão Node.js:
```bash
node gerar_newsletter.js
```

### 3. Pronto! ✅

O script irá:
- Encontrar todas as imagens na pasta `images/`
- Ordenar alfabeticamente
- Inserir no HTML entre os comentários `<!-- CONTEUDO -->` e `<!--------------->`
- Atualizar o arquivo `index.html`

## 📁 Estrutura de pastas

```
calendario-nov/
├── index.html
├── gerar_newsletter.py
├── gerar_newsletter.js
├── README.md
└── images/
    ├── 01-header.png
    ├── 02-banner.png
    ├── 03-produtos.png
    └── ...
```

## ⚙️ Formatos de imagem suportados

- PNG
- JPG/JPEG
- GIF
- WEBP

## 💡 Dicas

- **Nomeie as imagens com números no início** (01-, 02-, 03-) para garantir a ordem correta
- O script **substitui** todo o conteúdo entre os marcadores, então você pode executá-lo múltiplas vezes
- Mantenha backup do seu `index.html` antes de executar pela primeira vez

## 🔧 Personalização

Se precisar alterar a pasta de imagens ou o arquivo HTML, edite as funções principais nos scripts:

**Python:**
```python
inserir_imagens_no_html(arquivo_html='index.html', pasta_imagens='images')
```

**Node.js:**
```javascript
inserirImagensNoHtml('index.html', 'images')
```

## 📝 Exemplo de saída

```
============================================================
   GERADOR DE NEWSLETTER - INSERIR IMAGENS FATIADAS
============================================================

✅ Encontradas 5 imagens:
   - images/01-header.png
   - images/02-banner.png
   - images/03-produtos.png
   - images/04-ofertas.png
   - images/05-footer.png

✅ Newsletter atualizada com sucesso!
📄 Arquivo: index.html

============================================================
```

## 🐛 Problemas comuns

**"Pasta 'images' não encontrada"**
- Certifique-se de criar a pasta `images/` no mesmo diretório do script

**"Nenhuma imagem encontrada"**
- Verifique se as imagens estão no formato correto (PNG, JPG, etc)
- Verifique se as imagens estão dentro da pasta `images/`

**"Marcadores de conteúdo não encontrados"**
- Certifique-se de que o HTML contém os comentários:
  - `<!-- CONTEUDO  -->`
  - `<!--------------->`

## 📄 Licença

Livre para uso interno da equipe.

# gerador-newsletter
